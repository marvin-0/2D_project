import game_framework
import server
from pico2d import *
import play_state
import pickle
image = None
bgm = None
select_sound = None
chose_sound = None
mod = 0
font = None
font2 = None
def enter():
    global image, font, bgm, select_sound, chose_sound, font2
    image = load_image('sprite/title_screen.png')
    font = load_font('font/neodgm.ttf', 40)
    font2 = load_font('font/neodgm.ttf', 30)
    bgm = load_music('music/title_bgm.mp3')
    bgm.set_volume(32)
    bgm.repeat_play()
    select_sound = load_wav('sound/select.wav')
    select_sound.set_volume(50)
    chose_sound = load_wav('sound/chose.wav')
    chose_sound.set_volume(50)
    try:
        with open('score.pickle', 'rb') as f:
            server.score = pickle.load(f)
    except FileNotFoundError:
        create_save()
    server.score.sort(key=lambda x:x[1])


def exit():

    global image, font, bgm
    bgm.stop()
    del image, font, bgm

def handle_events():
    global mod
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, mod) == (SDL_KEYDOWN, 0):
                mod = 1
            elif event.type == SDL_KEYDOWN and mod > 0:
                match event.key:
                    case pico2d.SDLK_UP:
                        if mod - 1 > 0 and mod != 4:
                            chose_sound.play()
                            mod -= 1
                    case pico2d.SDLK_DOWN:
                        if mod + 1 < 4 and mod != 4:
                            chose_sound.play()
                            mod += 1
                    case pico2d.SDLK_z:
                        if mod == 1:
                            select_sound.play()
                            game_framework.change_state(play_state)
                        elif mod == 2:
                            select_sound.play()
                            mod = 4
                        elif mod == 3:
                            select_sound.play()
                            game_framework.quit()
                    case pico2d.SDLK_x:
                        if mod == 4:
                            mod = 2

def update():
    pass

def draw():
    global image
    clear_canvas()
    if mod == 0:
        image.draw(500,450, 1000, 900)
    elif mod == 1:
        image = load_image('sprite/title_screen2.png')
        image.draw(500, 450, 1000, 900)
        font2.draw(500, 850, 'z : select, esc : quit, x : back', (255, 255, 255))
    elif mod == 2:
        image = load_image('sprite/title_screen3.png')
        image.draw(500, 450, 1000, 900)
        font2.draw(500, 850, 'z : select, esc : quit, x : back', (255, 255, 255))
    elif mod == 3:
        image = load_image('sprite/title_screen4.png')
        image.draw(500, 450, 1000, 900)
        font2.draw(500, 850, 'z : select, esc : quit, x : back', (255, 255, 255))
    elif mod == 4:
        image = load_image('sprite/ranking_screen.png')
        image.draw(500, 450)
        if server.score != []:
            for i in range(len(server.score)):
                if i > 5:
                    break
                font.draw(550, 670 - i * 153, 'Time  : %d' % (server.score[i][0]), (255, 255, 255))
                font.draw(300, 670 - i * 153, 'Death : %d' % (server.score[i][1]), (255, 255, 255))
    update_canvas()

def create_save():
    with open('score.pickle', 'wb') as f:
        pickle.dump(server.score, f)
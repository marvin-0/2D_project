from pico2d import *
import game_framework
import play_state
import title_state
import game_world
import server

image1 = None
image2 = None
mod = None
sound = None
select_sound = None
chose_sound = None
def enter():
    global image1, image2, sound, mod, select_sound, chose_sound
    image1 = load_image('sprite/Pause1.png')
    image2 = load_image('sprite/Pause2.png')
    sound = load_wav('sound/pause.wav')
    sound.set_volume(32)
    sound.play()
    select_sound = load_wav('sound/select.wav')
    select_sound.set_volume(50)
    chose_sound = load_wav('sound/chose.wav')
    chose_sound.set_volume(50)
    mod = 1

def exit():
    if mod == 2:
        game_world.clear()
        server.back_ground.stage_bgm.stop()
    global image1, image2
    del image1, image2

def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    if mod == 1:
        image1.draw(500,400)
    else:
        image2.draw(500,400)
    update_canvas()
def pause():
    pass

def resume():
    pass
def handle_events():
    global mod
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_UP:
                    chose_sound.play()
                    mod = 1
                case pico2d.SDLK_DOWN:
                    chose_sound.play()
                    mod = 2
                case pico2d.SDLK_z:
                    select_sound.play()
                    if mod == 1:
                        game_framework.pop_state()
                    else:
                        game_framework.change_state(title_state)

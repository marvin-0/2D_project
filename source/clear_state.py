import game_framework
import server
from pico2d import *
import play_state
import title_state
import game_world
import pickle

image = None
bgm = None
font = None
mod = 0
def enter():
    global image, font
    image = load_image('sprite/title_screen.png')
    font = load_font('font/neodgm.ttf', 100)
    server.score.append([server.time, server.rockman.death_count])
    with open('score.pickle', 'wb') as f:
        pickle.dump(server.score, f)

def exit():
    game_world.clear()
    server.back_ground.stage_bgm.stop()
    server.rockman = None
    server.back_ground = None
    server.ground = None
    server.ground_amount = 0
    server. spike = None
    server.boss = None
    server.time = None
    play_state.stage = 1
    play_state.save_x, play_state.save_y = 100, 90
    global image
    del image

def handle_events():
    global mod
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
                game_framework.change_state(title_state)



def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    font.draw(150, 750, 'Congratulations', (0, 0, 0))
    font.draw(270, 500, 'Time  : %d' % (server.time), (0, 0, 0))
    font.draw(270, 300, 'Death : %d' % (server.rockman.death_count), (0, 0, 0))
    update_canvas()

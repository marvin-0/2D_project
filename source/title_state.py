import game_framework
from pico2d import *
import play_state
image = None

def enter():
    global image
    image = load_image('sprite/title_screen.png')

def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(play_state)

def update():
    pass

def draw():
    clear_canvas()
    image.draw(500,450, 1000, 1000)
    update_canvas()

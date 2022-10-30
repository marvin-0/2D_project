from pico2d import *
import game_framework
import play_state

image1 = None
image2 = None
mod = None


def enter():
    global image1, image2, mod
    image1 = load_image('Pause1.png')
    image2 = load_image('Pause2.png')
    mod = 1

def exit():
    global image1, image2
    del image1, image2

def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_char()
    if mod == 1:
        image1.draw(500,400)
    else:
        image2.draw(500,400)
    update_canvas()

def handle_events():
    global mod
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_UP:
                    mod = 1
                case pico2d.SDLK_DOWN:
                    mod = 2
                case pico2d.SDLK_z:
                    if mod == 1:
                        game_framework.pop_state()
                    else:
                        game_framework.quit()







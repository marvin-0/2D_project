from pico2d import*
from character import *
from monster1 import *

open_canvas()

rockman = Main_char()
monster1 = Monster_I()

while rockman.on:
    clear_canvas()
    rockman.move_dir()
    monster1.draw()
    monster1.update()
    update_canvas()


close_canvas()


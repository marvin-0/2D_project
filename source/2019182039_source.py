from pico2d import*
from character import *

open_canvas()

rockman = Main_char()

while rockman.on:
    clear_canvas()
    rockman.move_dir()
    update_canvas()


close_canvas()


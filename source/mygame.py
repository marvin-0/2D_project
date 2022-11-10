from pico2d import*
import character_class
import play_state
import title_state
from monster1_class import *
import game_framework

open_canvas(1000, 900)
game_framework.run(title_state)
close_canvas()

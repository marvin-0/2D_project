from pico2d import *
from character_class import *
import play_state

class Bullet:
    def __init__(self):
        self.image = load_image('bullet.png')
        self.x, self.y = play_state.rockman.x, play_state.rockman.y
        self.dir = play_state.rockman.stand
        self.speed = 10

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.speed * self.dir


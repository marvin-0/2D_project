from pico2d import *

class Monster_I:
    def __init__(self):
        self.image = load_image('monster1.png')
        self.x, self.y  = 500, 90
        self.dir = 1
        self.frame = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 45, 35 * 1, 45, 35, self.x, self.y, 100, 100)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 45, 35 * 3, 45, 35, self.x, self.y, 100, 100)

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x += self.dir * 5
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1
        delay(0.01)
from pico2d import *

class Ground:
    def __init__(self):
        self.image = load_image('ground.png')
        self.x, self.y = 2000, 1000
    def draw(self):
        self.image.draw(self.x, self.y)

class Spike:
    def __init__(self):
        self.image_up = load_image('spike1.png')
        self.image_right = load_image('spike2.png')
        self.image_left = load_image('spike3.png')
        self.image_down = load_image('spike4.png')
        self.x, self.y = 2000, 1000
        self.dir = 1
        self.shot = 0
    def draw(self):
        if self.dir == 1:
            self.image_up.draw(self.x, self.y)

    def update(self):
        if self.shot == 1:
            self.y += 20

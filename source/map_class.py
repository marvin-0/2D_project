from pico2d import *

class Ground:
    def __init__(self):
        self.image = load_image('ground.png')
        self.x, self.y = 2000, 1000
    def draw(self):
        self.image.draw(self.x, self.y)

class Spike_up:
    def __init__(self):
        self.image = load_image('spike1.png')
        self.x, self.y

class Spike_down:
    def __init__(self):
        self.image = load_image('spike4.png')
        self.x, self.y

class Spike_right:
    def __init__(self):
        self.image = load_image('spike2.png')
        self.x, self.y

class Spike_left:
    def __init__(self):
        self.image = load_image('spike3.png')
        self.x, self.y
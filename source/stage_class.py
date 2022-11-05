from pico2d import *

class Stage:
    def __init__(self):
        self.image = load_image('map.png')

    def draw(self):
        self.image.draw(500, 450)
    def update(self):
        pass

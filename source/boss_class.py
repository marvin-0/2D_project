from pico2d import *
import game_framework
import game_world

class Boss:
    image = None
    def __init__(self):
        if Boss.image == None:
            Boss.image = None
        Boss.x, Boss.y = 800, 90
        Boss.hp = 100

    def update(self):
        pass
    def draw(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_collision(self, other, group):
        pass

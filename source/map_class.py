from pico2d import *

class Ground:
    image = None
    def __init__(self):
        if Ground.image == None:
            Ground.image = load_image('sprite/ground.png')
        self.x, self.y = 2000, 1000
    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def handle_collision(self, other, group):
        pass

    def ground_collision(self, type, other):
        pass

class Spike:
    image = None
    def __init__(self):
        if Spike.image == None:
            Spike.image = load_image('sprite/spike1.png')
        self.x, self.y = 2000, 1000
        self.dir = 1
        self.shot = 0
    def draw(self):
        if self.dir == 1:
            self.image.draw(self.x, self.y)
            draw_rectangle(*self.get_bb())

    def update(self):
        if self.shot == 1:
            self.y += 20
            if self.y >= 950:
                self.shot = 0
        if self.shot == 2:
            self.x += 1
            if self.x == 875 - 450:
                self.shot = 1
        if self.shot == 3:
            self.y -= 25
            if self.y <= -50:
                self.shot = 0

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, other, group):
        pass

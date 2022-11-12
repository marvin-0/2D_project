from pico2d import *
import play_state


class Ground:
    image = None
    count = 0
    def __init__(self):
        if Ground.image == None:
            Ground.image = load_image('sprite/ground.png')
        if Ground.count >= 100:
            Ground.count = 0
        self.x, self.y = 2000, 1000
        self.num = Ground.count
        Ground.count += 1
        self.show = 1
        self.angle = 0
    def draw(self):
        if self.show == 1:
            self.image.clip_composite_draw(0, 0, 50, 50, self.angle * 3.141592 / 180, '', self.x, self.y)
            # draw_rectangle(*self.get_bb())
    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def handle_collision(self, other, group):
        pass

    def ground_collision(self, type, other):
        if type == 1:
            if play_state.stage == 1:
                if self.num == 55:
                    self.show = 1
                    self.x = 10000
                elif self.num == 57:
                    play_state.spike_up[6].shot = 1
                elif self.num == 62:
                    play_state.spike_up[16].shot = 2
            if play_state.stage == 2:
                if self.num == 3:
                    play_state.spike_up[6].shot = 2
        elif type == 2:
            if play_state.stage == 1:
                if self.num == 55:
                    self.show = 1
        elif type == 3:
            if play_state.stage == 1:
                if self.num == 55 and self.show == 1:
                    self.x = 875 - 150
            pass
        elif type == 4:
            if play_state.stage == 1:
                if self.num == 55 and self.show == 1:
                    self.x = 875 - 150
            pass


class Spike:
    image = None
    def __init__(self):
        if Spike.image == None:
            Spike.image = load_image('sprite/spike1.png')
        self.x, self.y = 2000, 1000
        self.shot = 0
        self.angle = 0
    def draw(self):
        self.image.clip_composite_draw(0, 0, 50, 50, self.angle * 3.141592 / 180, '', self.x, self.y)
        # draw_rectangle(*self.get_bb())
        # if self.dir == 1:
        #     self.image.draw(self.x, self.y)
        #     draw_rectangle(*self.get_bb())

    def update(self):
        if play_state.stage == 1:
            if self.shot == 1:
                self.y += 25
                if self.y >= 950:
                    self.shot = 0
            if self.shot == 2:
                self.x += 1
                if self.x == 875 - 450:
                    self.shot = 1
        elif play_state.stage == 2:
            if self.shot == 1:
                self.x += 1
            elif self.shot == 2:
                self.y += 25
                if self.y >= 950:
                    self.shot = 0


    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, other, group):
        pass

from pico2d import *
import game_framework
import game_world

PIXEL_PER_METER = (6.0 / 0.1)
SHOT_SPEED_KMPH = 50.0
SHOT_SPEED_MPM = (SHOT_SPEED_KMPH * 1000.0 / 60.0)
SHOT_SPEED_MPS = (SHOT_SPEED_MPM / 60.0)
SHOT_SPEED_PPS = (SHOT_SPEED_MPS * PIXEL_PER_METER)



class Bullet:
    image = None
    count = 0

    def __init__(self, x = 1000, y = 1000, velocity = 1):
        if Bullet.image == None:
            Bullet.image = load_image('sprite/bullet.png')
        self.x, self.y = x, y
        self.dir = velocity
        self.speed = 10
        Bullet.count += 1
        self.amount = Bullet.count

    def draw(self):
        self.image.draw(self.x, self.y, 20, 10)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += SHOT_SPEED_PPS * game_framework.frame_time * self.dir
        if self.x < 0 or self.x > 1000:
            game_world.remove_object(self)
            Bullet.count -= 1
        if self.amount > 5:
            game_world.remove_object(self)
            Bullet.count -= 1
    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def handle_collision(self, other, group):
        if group == 'bullet:ground':
            if other.show == 1:
                game_world.remove_object(self)
                Bullet.count -= 1


from pico2d import *
import game_world
class Bullet:
    image = None
    count = 0

    def __init__(self, x = 400, y = 300, velocity = 1):
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
        self.x += self.speed * self.dir
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
            game_world.remove_object(self)
            Bullet.count -= 1


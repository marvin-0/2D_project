from pico2d import *
import game_framework
import game_world
import random
import server
import clear_state

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

PIXEL_PER_METER = (6.0 / 0.1)
SHOT_SPEED_KMPH = 40.0
SHOT_SPEED_MPM = (SHOT_SPEED_KMPH * 1000.0 / 60.0)
SHOT_SPEED_MPS = (SHOT_SPEED_MPM / 60.0)
SHOT_SPEED_PPS = (SHOT_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 16
class Boss:
    def __init__(self):
        self.image = load_image('sprite/mario.png')
        self.hp_bar_image = load_image('sprite/boss_hp_bar.png')
        self.x, self.y = 800, 120
        self.dir = -1
        self.up = 1
        self.hp = 1000
        self.pattern = 0
        self.frame = 0
        self.hit_on = 0
        self.timer = 0.0
        self.shot_timer = 0.0
        self.speed = 1
        self.hit_sound = load_wav('sound/boss_hit.wav')
        self.hit_sound.set_volume(20)

    def update(self):
        if self.hp <= 0:
            game_world.remove_object(self)
            server.time = int(get_time() - server.back_ground.start_time)
            game_framework.push_state(clear_state)

        self.bounce()
        if self.pattern >= 1:
            self.x += self.dir * self.speed * RUN_SPEED_PPS * game_framework.frame_time / random.randint(1, 4)
            self.y += self.up * RUN_SPEED_PPS * game_framework.frame_time
        if self.timer > 0:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
            self.timer -= game_framework.frame_time
            if self.timer < 0:
                self.frame = 0
        if self.hp <= 900:
            self.shot_fire()
        if self.hp == 300 and self.pattern == 1:
            monster = Monster(1000, 80)
            game_world.add_object(monster, 2)
            game_world.add_collision_pairs(server.rockman, monster, 'rockman:monster')
            self.pattern = 2

    def bounce(self):
        if self.x < 50:
            self.dir = 1
        elif self.x > 950:
            self.dir = -1
        if self.y > 300:
            self.up = -1
        elif self.y < 125:
            self.up = 1

    def shot_fire(self):
        self.shot_timer -= game_framework.frame_time
        if self.shot_timer <= 0:
            fire = Boss_Fire(self.x, self.y)
            game_world.add_object(fire, 3)
            game_world.add_collision_pairs(server.rockman, fire, 'rockman:fire')
            if self.hp >= 700:
                self.shot_timer = 10.0
                self.speed = 1.2
            elif self.hp >= 500:
                self.shot_timer = 8.0
                self.speed = 1.5
            elif self.hp > 300:
                self.shot_timer = 8.0
                fire = Boss_Fire(self.x, self.y, 0.1)
                game_world.add_object(fire, 3)
                game_world.add_collision_pairs(server.rockman, fire, 'rockman:fire')
            elif self.hp >= 100:
                self.shot_timer = 6.0
            elif self.hp > 0:
                self.shot_timer = 0.5



    def draw(self):
        if self.pattern == 0:
            self.image.clip_composite_draw(0, 0, 16, 32, 0, 'h', self.x, self.y, 100, 150)
        elif self.dir > 0:
            self.hp_bar_image.clip_draw(0, 0, 1000, 30, 500, 900, self.hp, 30)
            self.image.clip_composite_draw((int(self.frame) + 1) * 16, 0, 16, 32, 0, '', self.x, self.y, 100, 150)
        elif self.dir < 0:
            self.hp_bar_image.clip_draw(0, 0, 1000, 30, 500, 900, self.hp, 30)
            self.image.clip_composite_draw((int(self.frame) + 1) * 16, 0, 16, 32, 0, 'h', self.x, self.y, 100, 150)
    def get_bb(self):
        return self.x - 50, self.y - 75, self.x + 50, self.y + 75

    def reset(self):
        self.x, self.y = 800, 120
        self.dir = -1
        self.up = 1
        self.hp = 1000
        self.pattern = 0
        self.frame = 0
        self.hit_on = 0
        self.timer = 0.0
        self.shot_timer = 0.0
    def handle_collision(self, other, group):
        if group == 'bullet:boss':
            if self.pattern == 0:
                self.pattern = 1
            elif self.pattern >= 1:
                self.hp -= 10
                self.timer = 0.5
            self.hit_sound.play()
    def cheat_on(self):
        self.hp = 10


class Boss_Fire:
    image = None
    sound = None
    def __init__(self, x = 1000, y = 1000, v = 0):
        if Boss_Fire.image == None:
            Boss_Fire.image = load_image('sprite/boss_fire.png')
        if Boss_Fire.sound == None:
            Boss_Fire.sound = load_wav('sound/boss_shot.wav')
        self.x, self.y = x, y
        self.dir = math.atan2(server.rockman.y - self.y, server.rockman.x - self.x) + v
        self.frame = 0
        self.speed = SHOT_SPEED_PPS
        Boss_Fire.sound.play()


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        if self.x < 0 or self.x > 1000 or self.y < 0 or self.y > 900:
            game_world.remove_object(self)
    def draw(self):
        self.image.clip_draw(int(self.frame) * 8, 0, 8, 8, self.x, self.y, 50, 50)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16
    def handle_collision(self, other, group):
        if group == 'rockman:fire':
            game_world.remove_object(self)

    def reset(self):
        game_world.remove_object(self)


class Monster:
    def __init__(self, x, y):
        self.image = load_image('sprite/monster1.png')
        self.x, self.y = x, y
        self.dir = 1
        self.frame = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 45, 35 * 1, 45, 35, self.x, self.y, 70, 70)
        elif self.dir == -1:
            self.image.clip_draw(int(self.frame) * 45, 35 * 3, 45, 35, self.x, self.y, 70, 70)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 1000:
            self.dir = -1
        elif self.x < 0:
            self.dir = 1

    def get_bb(self):
        return self.x - 15, self.y - 25, self.x + 15, self.y + 25
    def handle_collision(self, other, group):
        pass

from pico2d import *
import game_world
import game_framework
import server
import play_state
from boss_class import Boss

PIXEL_PER_METER = (6.0 / 0.1)
SPIKE_SPEED_KMPH = 95.0
SPIKE_SPEED_MPM = (SPIKE_SPEED_KMPH * 1000.0 / 60.0)
SPIKE_SPEED_MPS = (SPIKE_SPEED_MPM / 60.0)
SPIKE_SPEED_PPS = (SPIKE_SPEED_MPS * PIXEL_PER_METER)

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
    def update(self):
        if play_state.stage == 3:
            if server.rockman.y <= 375:
                server.spike[20].shot = 1

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def handle_collision(self, other, group):
        pass

    def ground_collision(self, type, other):
        if type == 1: #윗면
            if play_state.stage == 1:
                if self.num == 55:
                    self.show = 1
                    self.x = 10000
                elif self.num == 57:
                    server.spike[6].shot = 1
                elif self.num == 62:
                    server.spike[16].shot = 2
                elif self.num == 61:
                    server.spike[6].shot = 3
            if play_state.stage == 2:
                if self.num == 3:
                    server.spike[6].shot = 2
                elif self.num == 1:
                    for i in range(20, 37):
                        server.spike[i].shot = 1
                elif self.num == 5:
                    server.spike[38].shot = 3
        elif type == 2:# 아랫면
            if play_state.stage == 1:
                if self.num == 55:
                    self.show = 1
        elif type == 3:
            if play_state.stage == 1:
                if self.num == 55 and self.show == 1:
                    self.x = 875 - 150
            elif play_state.stage == 2:
                self.show = 1
        elif type == 4:
            if play_state.stage == 1:
                if self.num == 55 and self.show == 1:
                    self.x = 875 - 150


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

    def update(self):
        if play_state.stage == 1:
            if self.shot == 1:
                self.y += SPIKE_SPEED_PPS * game_framework.frame_time
                if self.y >= 950:
                    self.shot = 0
            elif self.shot == 2:
                self.x += SPIKE_SPEED_PPS * game_framework.frame_time / 5
                if self.x >= 875 - 450:
                    self.shot = 1
            elif self.shot == 3:
                self.y -= SPIKE_SPEED_PPS * game_framework.frame_time
                self.angle = 180
                if self.y < -50:
                    self.shot = 0
        elif play_state.stage == 2:
            if self.shot == 1:
                self.x += SPIKE_SPEED_PPS * game_framework.frame_time / 10
            elif self.shot == 2:
                self.y += SPIKE_SPEED_PPS * game_framework.frame_time
                if self.y >= 950:
                    self.shot = 0
            elif self.shot == 3:
                self.y -= SPIKE_SPEED_PPS * game_framework.frame_time
                self.angle = 180
                if self.y < -50:
                    self.shot = 0
        elif play_state.stage == 3:
            if self.shot == 1:
                self.x += SPIKE_SPEED_PPS * game_framework.frame_time / 2
                if self.x > 1100:
                    self.shot = 0



    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, other, group):
        pass

def reset_world():
    game_world.clear()
    game_world.add_object(server.rockman, 2)
    game_world.add_object(server.back_ground, 0)
    game_world.add_objects(server.ground, 1)
    game_world.add_objects(server.spike, 1)
    game_world.add_collision_pairs(server.rockman, server.ground, 'rockman:ground')
    game_world.add_collision_pairs(server.rockman, server.spike, 'rockman:spike')

    clear_map(server.ground, server.spike)
    if play_state.stage == 1:
        stage1(server.ground, server.spike)
    elif play_state.stage == 2 or play_state.stage == 3:
        play_state.stage = 2
        stage2(server.ground, server.spike)
    elif play_state.stage == 4:
        play_state.stage = 4
        game_world.add_object(server.boss, 3)
        game_world.add_collision_pairs(server.rockman, server.boss, 'rockman:boss')
        stage4(server.ground, server.spike)
        server.boss.reset()
    server.rockman.reset(play_state.save_x, play_state.save_y)
    server.rockman.death_count += 1
def stage_change():
    clear_map(server.ground, server.spike)
    if play_state.stage == 1:
        stage1(server.ground, server.spike)
    elif play_state.stage == 2:
        stage2(server.ground, server.spike)
    elif play_state.stage == 3:
        stage3(server.ground, server.spike)
    elif play_state.stage == 4:
        stage4(server.ground, server.spike)
        server.boss = Boss()
        game_world.add_object(server.boss, 3)
        game_world.add_collision_pairs(server.rockman, server.boss, 'rockman:boss')
def stage1(ground, spike):
    for i in range(9):
        ground[i].y = 25
        ground[i].x = 50 * i + 25
    for i in range(9, 18):
        ground[i].y = 25
        ground[i].x = 625 + i % 9 * 50
    for i in range(18, 33):
        ground[i].y = 75 + i % 18 * 50
        ground[i].x = 975
    for i in range(33, 53):
        ground[i].y = 175
        ground[i].x = 875 - i % 33 * 50

    ground[53].y = 175 + 150
    ground[53].x = 875
    ground[54].y = 175 + 150 + 50
    ground[54].x = 875 - 100
    ground[55].y = 175 + 350 # 갑툭튀
    ground[55].x = 875 - 150
    ground[55].show = 0
    ground[56].y = 175 + 200
    ground[56].x = 875 - 400
    ground[57].y = 175 + 250
    ground[57].x = 875 - 550
    ground[58].y = 175 + 350
    ground[58].x = 875 - 750
    ground[59].y = 175 + 450
    ground[59].x = 875 - 850
    ground[60].y = 175 + 500
    ground[60].x = 875 - 650
    ground[61].y = 175 + 500  # 가시 설치지점
    ground[61].x = 875 - 550
    ground[62].y = 175 + 500  # 가시 이동지점
    ground[62].x = 875 - 450
    ground[63].y = 175 + 500
    ground[63].x = 875 - 250
    ground[64].y = 175 + 550
    ground[64].x = 875 - 100

    for i in range(16):
        spike[i].y = 225
        spike[i].x = 50 * i + 25
        spike[i].angle = 0
        spike[i].shot = 0
    spike[16].y = 175 + 550
    spike[16].x = 875 - 550
    spike[17].y = 175 + 550
    spike[17].x = 875 - 225
    spike[16].shot = 0
    spike[17].shot = 0

def stage2(ground, spike):
    ground[0].x = 25
    ground[0].y = 25
    ground[1].x = 25 + 100
    ground[1].y = 25 + 150
    ground[2].x = 25 + 250
    ground[2].y = 25 + 200
    ground[3].x = 25 + 350
    ground[3].y = 25 + 350
    ground[4].x = 25 + 500
    ground[4].y = 25 + 400
    ground[5].x = 25 + 650
    ground[5].y = 25 + 450
    ground[6].x = 25 + 850
    ground[6].y = 25 + 550
    ground[7].x = 25 + 950
    ground[7].y = 25 + 650
    for i in range(8, 23):
        ground[i].y = 75 + i % 15 * 50
        ground[i].x = 975
        ground[i].show = 0

    for i in range(19):
        spike[i].y = 25
        spike[i].x = 50 * i + 75
        spike[i].shot = 0
    for i in range(20, 37):
        spike[i].y = 75 + i % 20 * 50
        spike[i].x = -100
        spike[i].angle = 270
        spike[i].shot = 0
    spike[37].x = 550
    spike[37].y = 25 + 450

    spike[38].x = 25 + 650
    spike[38].y = 875
    spike[38].angle = 180
    spike[38].shot = 0

def stage3(ground, spike):
    for i in range(0, 18):
        ground[i].y = 25 + i % 18 * 50
        ground[i].x = 250
    for i in range(18, 36):
        ground[i].y = 25 + i % 18 * 50
        ground[i].x = 750

    for i in range(0, 8):
        spike[i].x = 300 + i * 50
        spike[i].y = 700
    for i in range(8, 14):
        spike[i].x = 700 - i % 6 * 50
        spike[i].y = 600 - i % 6 * 50
        spike[i].angle = 90
    for i in range(14, 19):
        spike[i].x = 500 - i % 5 * 50
        spike[i].y = 650 - i % 5 * 50
        spike[i].angle = 270
    spike[19].x = 300
    spike[19].y = 400
    spike[19].angle = 270
    spike[20].x = 300
    spike[20].y = 350
    spike[20].angle = 270
    for i in range(21, 28):
        spike[i].x = 300 + i % 7 * 25
        spike[i].y = 300 - i % 7 * 50
    for i in range(28, 38):
        spike[i].x = 450 + i % 10 * 25
        spike[i].y = 300 - i % 10 * 50
def stage4(ground, spike):
    for i in range(20):
        ground[i].y = 25
        ground[i].x = 50 * i + 25
    for i in range(20, 22):
        ground[i].y = 875 - i % 2 * 50
        ground[i].x = 300


def clear_map(ground, spike):
    for g in ground:
        g.x, g.y = 2000, 1000
        g.show = 1
    for s in spike:
        s.x, s.y = 2000, 1000
        s.shot = 0
        s.angle = 0

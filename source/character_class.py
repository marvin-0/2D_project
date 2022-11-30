from pico2d import*
import game_world
import game_framework
import play_state
import map_class
from bullet_class import Bullet

PIXEL_PER_METER = (6.0 / 0.1)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

GRAVITY_SPEED_KMPH = 15.0
GRAVITY_SPEED_MPM = (GRAVITY_SPEED_KMPH * 1000.0 / 60.0)
GRAVITY_SPEED_MPS = (GRAVITY_SPEED_MPM / 60.0)
GRAVITY_SPEED_PPS = (GRAVITY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

RD, LD, RU, LU, ZD, ZU, CD, CU = range(8)
event_name = ['RD', 'LD', 'RU', 'LU', 'ZD', 'ZU', 'CD', 'CU']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_c): CD,
    (SDL_KEYUP, SDLK_c): CU,
    (SDL_KEYDOWN, SDLK_z): ZD,
    (SDL_KEYUP, SDLK_z): ZU,
}
class IDLE:
    @staticmethod
    def enter(self,event):
        self.dir = 0

    @staticmethod
    def exit(self, event):
        if event == ZD:
            self.shot_bullet()

    @staticmethod
    def do(self):
        if self.hp <= 0:
            if self.death < 3:
                self.death = (self.death + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        else:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        # self.frame = (self.frame + 1) % 30
    @staticmethod
    def draw(self):
        if self.hp <= 0:
            if self.face_dir == 1:
                self.image.clip_draw(int(self.death) * 32, 32 * 8, 32, 32, self.x, self.y, 50, 50)
            else:
                self.image.clip_draw(int(self.death) * 32, 32 * 3, 32, 32, self.x, self.y, 50, 50)
            if self.death >= 3:
                self.dead_image.draw(500, 450)
        else:
            if self.face_dir == 1:
                self.image.clip_draw(int(self.frame) * 32, 32 * 11, 32, 32, self.x, self.y, 50, 50)
            else:
                self.image.clip_draw(int(self.frame) * 32, 32 * 6, 32, 32, self.x, self.y, 50, 50)
class RUN:
    def enter(self, event):
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        self.face_dir = self.dir
        if event == ZD:
            self.shot_bullet()

    def do(self):
        if self.hp <= 0:
            if self.death < 3:
                self.death = (self.death + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        else:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        self.x = clamp(0, self.x, 1100)

    def draw(self):
        if self.hp <= 0:
            if self.face_dir == 1:
                self.image.clip_draw(int(self.death) * 32, 32 * 8, 32, 32, self.x, self.y, 50, 50)
            else:
                self.image.clip_draw(int(self.death) * 32, 32 * 3, 32, 32, self.x, self.y, 50, 50)
            if self.death >= 3:
                self.dead_image.draw(500, 450)
        else:
            if self.dir == 1:
                self.image.clip_draw(int(self.frame) * 32, 32 * 10, 32, 32, self.x, self.y, 50, 50)
            elif self.dir == -1:
                self.image.clip_draw(int(self.frame) * 32, 32 * 5, 32, 32, self.x, self.y, 50, 50)

class ATK_IDLE:
    def enter(self, event):
        self.dir = 0
        # 여기에 총발사 함수 발동

    def exit(self, event):
        pass

    def do(self):
        if self.hp <= 0:
            if self.death < 3:
                self.death = (self.death + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        pass
    def draw(self):
        if self.hp <= 0:
            if self.face_dir == 1:
                self.image.clip_draw(int(self.death) * 32, 32 * 8, 32, 32, self.x, self.y, 50, 50)
            else:
                self.image.clip_draw(int(self.death) * 32, 32 * 3, 32, 32, self.x, self.y, 50, 50)
            if self.death >= 3:
                self.dead_image.draw(500, 450)
        else:
            if self.face_dir == 1:
                self.image.clip_draw(int(self.frame % 1) * 32, 32 * 9, 32, 32, self.x, self.y, 50, 50)
            else:
                self.image.clip_draw(int(self.frame % 1) * 32, 32 * 4, 32, 32, self.x, self.y, 50, 50)
class ATK_RUN:
    def enter(self, event):
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        self.face_dir = self.dir

    def do(self):
        if self.hp <= 0:
            if self.death < 3:
                self.death = (self.death + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        else:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
            self.x = clamp(0, self.x, 1100)

    def draw(self):
        if self.hp <= 0:
            if self.face_dir == 1:
                self.image.clip_draw(int(self.death) * 32, 32 * 8, 32, 32, self.x, self.y, 50, 50)
            else:
                self.image.clip_draw(int(self.death) * 32, 32 * 3, 32, 32, self.x, self.y, 50, 50)
            if self.death >= 3:
                self.dead_image.draw(500, 450)
        else:
            if self.dir == 1:
                self.image.clip_draw(int(self.frame) * 32, 32 * 0, 32, 32, self.x, self.y, 50, 50)
            elif self.dir == -1:
                self.image.clip_draw(int(self.frame) * 32, 32 * 1, 32, 32, self.x, self.y, 50, 50)
class JUMP:
    def enter(self, event):
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        if self.jump == 0:
            self.jump_max = self.y + 170
            self.jump = 1
        if self.dir != 0:
            self.face_dir = self.dir

    def exit(self, event):
        if self.dir != 0:
            self.face_dir = self.dir
        if event == CU and self.jump_on == 0:
            self.jump_on = 1
            self.jump_dis = 0
        if event == ZD:
            self.shot_bullet()

    def do(self):
        if self.hp <= 0:
            if self.death < 3:
                self.death = (self.death + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if self.jump == 1:
            if self.jump_on == 0:
                self.y += round(GRAVITY_SPEED_PPS * game_framework.frame_time * 4.2)
                if self.y >= self.jump_max:
                    self.jump_on = 1
                    self.jump_dis = 0
            elif self.jump_on == 1:
                self.y += round(GRAVITY_SPEED_PPS * game_framework.frame_time / 3)
                if self.y <= self.jump_max - 40:
                    self.jump_on = 2
                    self.jump_dis = 0
        elif self.jump == 0:
            if self.dir == 0:
                self.cur_state = IDLE
            else:
                self.cur_state = RUN

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1100)

    def draw(self):
        if self.hp <= 0:
            if self.face_dir == 1:
                self.image.clip_draw(int(self.death) * 32, 32 * 8, 32, 32, self.x, self.y, 50, 50)
            else:
                self.image.clip_draw(int(self.death) * 32, 32 * 3, 32, 32, self.x, self.y, 50, 50)
            if self.death >= 3:
                self.dead_image.draw(500, 450)
        else:
            if self.face_dir == 1:
                self.image.clip_draw(int(self.frame % 1) * 32, 32 * 7, 32, 32, self.x, self.y, 50, 50)
            elif self.face_dir == -1:
                self.image.clip_draw(int(self.frame % 1) * 32, 32 * 2, 32, 32, self.x, self.y, 50, 50)
class ATK_JUMP:
    def enter(self, event):
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        if self.jump == 0:
            self.jump_max = self.y + 170
            self.jump = 1
        if self.dir != 0:
            self.face_dir = self.dir

    def exit(self, event):
        if self.dir != 0:
            self.face_dir = self.dir
        if event == CU and self.jump_on == 0:
            self.jump_on = 1
            self.jump_dis = 0

    def do(self):
        if self.hp <= 0:
            if self.death < 3:
                self.death = (self.death + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if self.jump == 1:
            if self.jump_on == 0:
                self.y += round(GRAVITY_SPEED_PPS * game_framework.frame_time * 4.2)
                if self.y >= self.jump_max:
                    self.jump_on = 1
                    self.jump_dis = 0
            elif self.jump_on == 1:
                self.y += round(GRAVITY_SPEED_PPS * game_framework.frame_time / 3)
                if self.y <= self.jump_max - 40:
                    self.jump_on = 2
                    self.jump_dis = 0
        elif self.jump == 0:
            if self.dir == 0:
                self.cur_state = ATK_IDLE
            else:
                self.cur_state = ATK_RUN

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1100)

    def draw(self):
        if self.hp <= 0:
            if self.face_dir == 1:
                self.image.clip_draw(int(self.death) * 32, 32 * 8, 32, 32, self.x, self.y, 50, 50)
            else:
                self.image.clip_draw(int(self.death) * 32, 32 * 3, 32, 32, self.x, self.y, 50, 50)
            if self.death >= 3:
                self.dead_image.draw(500, 450)
        else:
            if self.face_dir == 1:
                self.image.clip_draw(int(self.frame % 1 + 1) * 32, 32 * 7, 32, 32, self.x, self.y, 50, 50)
            elif self.face_dir == -1:
                self.image.clip_draw(int(self.frame % 1 + 1) * 32, 32 * 2, 32, 32, self.x, self.y, 50, 50)

next_state = {
    IDLE:   {RU: RUN, LU: RUN, RD: RUN, LD: RUN, ZD: ATK_IDLE, ZU: IDLE, CD: JUMP, CU: IDLE},
    RUN:    {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, ZD: ATK_RUN, ZU: RUN, CD: JUMP, CU: RUN},
    ATK_IDLE: {RU: ATK_RUN, LU: ATK_RUN, RD: ATK_RUN, LD: ATK_RUN, ZD: ATK_IDLE, ZU: IDLE, CD: ATK_JUMP, CU: ATK_IDLE},
    ATK_RUN: {RU: ATK_IDLE, LU: ATK_IDLE, RD: ATK_IDLE, LD: ATK_IDLE, ZD: ATK_RUN, ZU: RUN, CD: ATK_JUMP, CU: ATK_RUN},
    JUMP:   {RU: JUMP, LU: JUMP, RD: JUMP, LD: JUMP, ZD: ATK_JUMP, CD: JUMP, CU: JUMP},
    ATK_JUMP: {RU: ATK_JUMP, LU: ATK_JUMP, RD: ATK_JUMP, LD: ATK_JUMP, ZD: ATK_JUMP, ZU: JUMP, CD: ATK_JUMP, CU: ATK_JUMP}
}

class Main_char:
    def __init__(self, x = 100, y = 90):
        self.image = load_image('sprite/rockman_sprite.png')
        self.dead_image = load_image('sprite/game_over.png')
        self.x, self.y = x, y
        self.hp = 50
        self.dir = 0            # -1왼쪽 +1 오른쪽방향
        self.frame = 0          # 애니메이션 프레임
        self.attack = 0         # 공격하고 있는지 아닌지 z키가 공격
        self.face_dir = 1          # -1 왼쪽 +1 오른쪽 방향
        self.jump = 0           # 0 점프안함 1 점프상태
        self.jump_dis = 0
        self.jump_on = 0
        self.jump_max = self.y + 160
        self.death = 0

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(self.cur_state, event_name[event])

            self.cur_state.enter(self, event)
        self.gravity()
        self.stage_change()

    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.face_dir}, Dir: {self.dir}')
    def add_event(self, event):
        self.event_que.insert(0, event)
    def handle_event(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
    def shot_bullet(self):
        if self.hp > 0:
            bullet = Bullet(self.x, self.y, self.face_dir)
            game_world.add_object(bullet, 3)
            game_world.add_collision_pairs(bullet, play_state.ground, 'bullet:ground')
    def gravity(self):
        self.y -= GRAVITY_SPEED_PPS * game_framework.frame_time
        # self.y -= 4
        if self.y <= -10:
            self.hp = 0
    def get_bb(self):
        return self.x, self.y, self.x, self.y
    def get_bb_ground(self):
        return self.x - 10, self.y - 25, self.x + 10, self.y + 25
    def handle_collision(self, other, group):
        if group == 'char:spike':
            self.hp -= 50

    def ground_collision(self, type, other):
        if type == 1:
            self.y += GRAVITY_SPEED_PPS * game_framework.frame_time
            if self.jump_on != 0 and other.num != 55:
                self.jump_on = 0
                self.jump = 0
                self.jump_dis = 0
        elif type == 2:
            if self.jump == 1:
                self.jump_on = 2
        elif type == 3:
            if other.show == 0 and play_state.stage == 1:
                pass
            else:
                self.x -= RUN_SPEED_PPS * game_framework.frame_time
        elif type == 4:
            if other.show == 0 and play_state.stage == 1:
                pass
            else:
                self.x += RUN_SPEED_PPS * game_framework.frame_time

    def reset_char(self, x, y):
        self.x = x
        self.y = y
        self.death = 0
        self.hp = 50
        self.frame = 0

    def stage_change(self):
        if play_state.stage == 1:
            if self.x > 1000:
                play_state.stage = 2
                play_state.char_x, play_state.char_y = 25, 90
                self.reset_char(25, 90)
                map_class.stage_change()
        elif play_state.stage == 2 and self.hp > 0 and self.y <= 0:
            play_state.stage = 3
            self.reset_char(500, 900)
            map_class.stage_change()



from pico2d import*

class Main_char:
    def __init__(self):
        self.image = load_image('rockman_sprite.png')
        self.x, self.y = 100, 90
        self.hp = 50
        self.dir = 0            # -1왼쪽 +1 오른쪽방향
        self.frame = 0          # 애니메이션 프레임
        self.attack = 0         # 공격하고 있는지 아닌지 z키가 공격
        self.stand = 1          # -1 왼쪽 +1 오른쪽 방향
        self.jump = 0  # 0 점프안함 1 점프상태
        self.jump_dis = 0
        self.jump_on = 0
        self.jump_max = 20
        self.hit = 0
        self.death = 0

    def move(self):             # 실질적인 x,y좌표 바꾸는 함수
        if self.hit == 0:
            self.x += 5 * self.dir
        if self.jump == 1:
            if self.jump_on == 0:
                self.y += 12
                self.jump_dis += 1
                if self.jump_dis == self.jump_max:
                    self.jump_on = 1
                    self.jump_dis = 0
            elif self.jump_on == 1:
                self.y += 3
                self.jump_dis += 1
                if self.jump_dis == 6:
                    self.jump_on = 2
                    self.jump_dis = 0

    def idle(self):             # 서있는 애니메이션 출력하는 함수
        if self.stand == 1:
            if self.attack == 0:
                self.image.clip_draw(self.frame // 10 * 32, 32 * 11, 32, 32, self.x, self.y, 50, 50)
                self.frame = (self.frame + 1) % 30
            elif self.attack == 1:
                self.image.clip_draw(self.frame % 1 * 32, 32 * 9, 32, 32, self.x, self.y, 50, 50)
        elif self.stand == -1:
            if self.attack == 0:
                self.image.clip_draw(self.frame // 10 * 32, 32 * 6, 32, 32, self.x, self.y, 50, 50)
                self.frame = (self.frame + 1) % 30
            elif self.attack == 1:
                self.image.clip_draw(self.frame % 1 * 32, 32 * 4, 32, 32, self.x, self.y, 50, 50)
        delay(0.01)

    def run_ani(self):          # 달리는 애니메이션 출력하는 함수
        if self.dir == 1:
            if self.attack == 0:
                self.image.clip_draw(self.frame // 10 * 32, 32 * 10, 32, 32, self.x, self.y, 50, 50)
                self.frame = (self.frame + 1) % 40
            elif self.attack == 1:
                self.image.clip_draw(self.frame // 10 * 32, 32 * 0, 32, 32, self.x, self.y, 50, 50)
                self.frame = (self.frame + 1) % 40
            delay(0.01)
        elif self.dir == -1:
            if self.attack == 0:
                self.image.clip_draw(self.frame // 10 * 32, 32 * 5, 32, 32, self.x, self.y, 50, 50)
                self.frame = (self.frame + 1) % 40
            elif self.attack == 1:
                self.image.clip_draw(self.frame // 10 * 32, 32 * 1, 32, 32, self.x, self.y, 50, 50)
                self.frame = (self.frame + 1) % 40
            delay(0.01)

    def jump_ani(self):         # 점프하는 애니메이션 출력하는 함수
        if self.dir == 1 or self.stand == 1:
            if self.attack == 0:
                self.image.clip_draw(self.frame % 1 * 32, 32 * 7, 32, 32, self.x, self.y, 50, 50)
            elif self.attack == 1:
                self.image.clip_draw((self.frame % 1 + 1) * 32, 32 * 7, 32, 32, self.x, self.y, 50, 50)
        elif self.dir == -1 or self.stand == -1:
            if self.attack == 0:
                self.image.clip_draw(self.frame % 1 * 32, 32 * 2, 32, 32, self.x, self.y, 50, 50)
            elif self.attack == 1:
                self.image.clip_draw((self.frame % 1 + 1) * 32, 32 * 2, 32, 32, self.x, self.y, 50, 50)
        delay(0.01)

    def hit_ani(self):         # 점프하는 애니메이션 출력하는 함수
        if self.stand == 1:
            self.image.clip_draw(self.frame % 2 * 32, 32 * 8, 32, 32, self.x, self.y, 50, 50)
            self.frame += 1
        elif self.stand == -1:
            self.image.clip_draw(self.frame % 2 * 32, 32 * 3, 32, 32, self.x, self.y, 50, 50)
            self.frame += 1
        if self.frame == 50:
            self.frame = 0
            self.hit = 0
        delay(0.01)

    def dead(self):
        if self.hp == 0:
            self.dead_ani()

    def dead_ani(self):
        if self.dir == 1 or self.stand == 1:
            self.image.clip_draw(self.death // 10 * 32, 32 * 8, 32, 32, self.x, self.y, 50, 50)
            self.death = (self.death + 1) % 40
        elif self.dir == -1 or self.stand == -1:
            self.image.clip_draw(self.death // 10 * 32, 32 * 3, 32, 32, self.x, self.y, 50, 50)
            self.death = (self.death + 1) % 40
        delay(0.01)




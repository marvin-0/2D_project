from pico2d import*

class Main_char:
    def __init__(self):
        self.image = load_image('rockman_sprite.png')
        self.x, self.y = 100, 90
        self.hp = 100
        self.dir = 0            # -1왼쪽 +1 오른쪽방향
        self.frame = 0          # 애니메이션 프레임
        self.attack = 0         # 공격하고 있는지 아닌지 z키가 공격
        self.stand = 1          # -1 왼쪽 +1 오른쪽 방향
        self.jump = 0  # 0 점프안함 1 점프상태
        self.jump_dis = 0
        self.jump_on = 0
        self.jump_max = 100
        self.death = 0
        self.on = True          # esc키 누르면 false 되서 반복문 종료

    def move(self):             # 실질적인 x,y좌표 바꾸는 함수
        if self.dir == 1:
            self.x += 1
            if self.jump == 0:
                self.run_ani()
            elif self.jump == 1:
                if self.jump_on == 0:
                    self.y += 4
                    self.jump_dis += 4
                    if self.jump_dis == self.jump_max:
                        self.jump_on = 1
                else:
                    self.y -= 4
                    self.jump_dis -= 4
                    if self.jump_dis == 0:
                        self.jump_on = 0
                        self.jump = 0
                self.jump_ani()

        elif self.dir == -1:
            self.x -= 1
            if self.jump == 0:
                self.run_ani()
            elif self.jump == 1:
                if self.jump_on == 0:
                    self.y += 4
                    self.jump_dis += 4
                    if self.jump_dis == self.jump_max:
                        self.jump_on = 1
                else:
                    self.y -= 4
                    self.jump_dis -= 4
                    if self.jump_dis == 0:
                        self.jump_on = 0
                        self.jump = 0
                self.jump_ani()

        elif self.dir == 0:
            if self.jump == 0:
                self.idle()
            elif self.jump == 1:
                if self.jump_on == 0:
                    self.y += 4
                    self.jump_dis += 4
                    if self.jump_dis == self.jump_max:
                        self.jump_on = 1
                else:
                    self.y -= 4
                    self.jump_dis -= 4
                    if self.jump_dis == 0:
                        self.jump_on = 0
                        self.jump = 0
                self.jump_ani()

    def idle(self):             # 서있는 애니메이션 출력하는 함수
        if self.stand == 1:
            if self.attack == 0:
                self.image.clip_draw(self.frame // 10 * 32, 32 * 11, 32, 32, self.x, self.y, 100, 100)
                self.frame = (self.frame + 1) % 30
            elif self.attack == 1:
                self.image.clip_draw(self.frame % 1 * 32, 32 * 9, 32, 32, self.x, self.y, 100, 100)
        elif self.stand == -1:
            if self.attack == 0:
                self.image.clip_draw(self.frame // 10 * 32, 32 * 6, 32, 32, self.x, self.y, 100, 100)
                self.frame = (self.frame + 1) % 30
            elif self.attack == 1:
                self.image.clip_draw(self.frame % 1 * 32, 32 * 4, 32, 32, self.x, self.y, 100, 100)
        delay(0.01)

    def run_ani(self):          # 달리는 애니메이션 출력하는 함수
        if self.dir == 1:
            if self.attack == 0:
                self.image.clip_draw(self.frame // 10 * 32, 32 * 10, 32, 32, self.x, self.y, 100, 100)
                self.frame = (self.frame + 1) % 40
            elif self.attack == 1:
                self.image.clip_draw(self.frame // 10 * 32, 32 * 0, 32, 32, self.x, self.y, 100, 100)
                self.frame = (self.frame + 1) % 40
            delay(0.01)
        elif self.dir == -1:
            if self.attack == 0:
                self.image.clip_draw(self.frame // 10 * 32, 32 * 5, 32, 32, self.x, self.y, 100, 100)
                self.frame = (self.frame + 1) % 40
            elif self.attack == 1:
                self.image.clip_draw(self.frame // 10 * 32, 32 * 1, 32, 32, self.x, self.y, 100, 100)
                self.frame = (self.frame + 1) % 40
            delay(0.01)

    def jump_ani(self):         # 점프하는 애니메이션 출력하는 함수
        if self.dir == 1 or self.stand == 1:
            if self.attack == 0:
                self.image.clip_draw(self.frame % 1 * 32, 32 * 7, 32, 32, self.x, self.y, 100, 100)
            elif self.attack == 1:
                self.image.clip_draw((self.frame % 1 + 1) * 32, 32 * 7, 32, 32, self.x, self.y, 100, 100)
        elif self.dir == -1 or self.stand == -1:
            if self.attack == 0:
                self.image.clip_draw(self.frame % 1 * 32, 32 * 2, 32, 32, self.x, self.y, 100, 100)
            elif self.attack == 1:
                self.image.clip_draw((self.frame % 1 + 1) * 32, 32 * 2, 32, 32, self.x, self.y, 100, 100)
        delay(0.01)

    def move_dir(self):         # 메인함수에서 호출되어서 계속 반복하며 키 입력받는 함수
        for event in get_events():
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.dir = 1
                    self.stand = 1
                elif event.key == SDLK_LEFT:
                    self.dir = -1
                    self.stand = -1
                elif event.key == SDLK_ESCAPE:
                    # self.on = False
                    self.hp = 0
                if event.key == SDLK_z:
                    self.attack = 1
                if event.key == SDLK_c:
                    self.jump = 1
            if event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dir = 0
                if event.key == SDLK_LEFT:
                    self.dir = 0
                if event.key == SDLK_z:
                    self.attack = 0
        if(self.hp != 0):
            self.move()
        self.dead()

    def dead(self):
        if self.hp == 0:
            self.dead_ani()

    def dead_ani(self):
        if self.dir == 1 or self.stand == 1:
            self.image.clip_draw(self.death * 32, 32 * 8, 32, 32, self.x, self.y, 100, 100)
            self.death = (self.death + 1) % 5
        elif self.dir == -1 or self.stand == -1:
            self.image.clip_draw(self.death * 32, 32 * 3, 32, 32, self.x, self.y, 100, 100)
            self.death = (self.death + 1) % 5
        if self.death == 4:
            self.on = False
        delay(0.5)


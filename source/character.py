from pico2d import*

class Main_char:
    def __init__(self):
        self.image = load_image('rockman_sprite.png')
        self.x, self.y = 100, 90
        self.dir = 0
        self.jump = 0
        self.frame = 0
        self.attack = 0
        self.stand = 1
        self.on = True

    def move(self):
        if self.dir == 1:
            self.x += 1
            self.run_ani()

        elif self.dir == -1:
            self.x -= 1
            self.run_ani()

        elif self.dir == 0:
            self.idle()

    def idle(self):
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

    def run_ani(self):
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

    def move_dir(self):
        for event in get_events():
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.dir = 1
                    self.stand = 1
                elif event.key == SDLK_LEFT:
                    self.dir = -1
                    self.stand = -1
                elif event.key == SDLK_ESCAPE:
                    self.on = False
                if event.key == SDLK_z:
                    self.attack = 1
            if event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dir = 0
                if event.key == SDLK_LEFT:
                    self.dir = 0
                if event.key == SDLK_z:
                    self.attack = 0
        self.move()

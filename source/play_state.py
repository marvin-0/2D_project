from pico2d import*
import game_framework
import character_class
import monster1_class
import bullet_class

rockman = None
monster1 = []
running = True
bullet = None

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                rockman.dir = 1
                rockman.stand = 1
            elif event.key == SDLK_LEFT:
                rockman.dir = -1
                rockman.stand = -1
            elif event.key == SDLK_ESCAPE:
                # self.on = False
                rockman.hp = 0
            if event.key == SDLK_z:
                rockman.attack = 1
                bullet.append(bullet_class.Bullet())
            if event.key == SDLK_c:
                rockman.jump = 1
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                rockman.dir = 0
            if event.key == SDLK_LEFT:
                rockman.dir = 0
            if event.key == SDLK_z:
                rockman.attack = 0

def enter():
    global rockman, running, monster1, bullet
    rockman = character_class.Main_char()
    monster1.append(monster1_class.Monster_I())
    bullet = []
    running = True

def exit():
    global rockman
    del rockman

def update():
    rockman.move()
    for m in monster1:
        m.update()
    for b in bullet:
        b.update()
    bm_clash()

def bm_clash():
    for m in monster1[:]:
        for b in bullet[:]:
            if b.x < m.x + 50 and b.x > m.x - 50:
                if b.y < m.y + 50 and b.y > m.y - 50:
                    monster1.remove(m)
                    bullet.remove(b)

def draw():
    clear_canvas()
    draw_char()
    update_canvas()

def draw_char():
    if rockman.hp != 0:
        if rockman.jump == 0:
            if rockman.dir == 0:
                rockman.idle()
            else:
                rockman.run_ani()

        elif rockman.jump == 1:
            rockman.jump_ani()
    else:
        rockman.dead_ani()
        if rockman.death == 39:
            game_framework.quit()
    for m in monster1:
        m.draw()
    for b in bullet:
        b.draw()


def pause():
    pass

def resume():
    pass

from pico2d import*
import game_framework
import character_class
import monster1_class
import bullet_class
import stage_class

rockman = None
monster1 = []
running = True
bullet = None
stage = None
bullet_count = 0

def enter():
    global rockman, running, monster1, bullet, bullet_count, stage
    rockman = character_class.Main_char()
    monster1 = [monster1_class.Monster_I() for m in range(1)]
    bullet = []
    bullet_count = 0
    stage = stage_class.Stage()
    running = True

def handle_events():
    global running, bullet_count, monster1, bullet
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
                if rockman.hit == 0:
                    rockman.attack = 1
                    if bullet_count < 5:
                        bullet.append(bullet_class.Bullet())
                        bullet_count += 1
            if event.key == SDLK_c:
                rockman.jump = 1
            if event.key == SDLK_r:
                monster1 = [monster1_class.Monster_I() for m in range(11)]
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                rockman.dir = 0
            if event.key == SDLK_LEFT:
                rockman.dir = 0
            if event.key == SDLK_z:
                rockman.attack = 0

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
    cm_clash()
    bullet_out()

def draw():
    clear_canvas()
    draw_char()
    update_canvas()

def pause():
    pass

def resume():
    pass

def draw_char():
    stage.draw()
    if rockman.hp > 0:
        if rockman.hit == 0:
            if rockman.jump == 0:
                if rockman.dir == 0:
                    rockman.idle()
                else:
                    rockman.run_ani()

            elif rockman.jump == 1:
                rockman.jump_ani()
        else:
            rockman.hit_ani()
    else:
        rockman.dead_ani()
        if rockman.death == 39:
            game_framework.quit()

    for m in monster1:
        m.draw()
    for b in bullet:
        b.draw()

def bm_clash():
    global bullet_count
    for m in monster1[:]:
        for b in bullet[:]:
            if b.x < m.x + 50 and b.x > m.x - 50:
                if b.y < m.y + 50 and b.y > m.y - 50:
                    monster1.remove(m)
                    bullet.remove(b)
                    bullet_count -= 1

def cm_clash():
    for m in monster1[:]:
        if rockman.hit == 0:
            if rockman.x > m.x - 25 and rockman.x < m.x + 25:
                if rockman.y > m.y - 25 and rockman.y < m.y + 25:
                    rockman.hit = 1
                    rockman.hp = 0

def bullet_out():
    global bullet_count
    for b in bullet[:]:
        if b.x > 800:
            bullet.remove(b)
            bullet_count -= 1
        elif b.x < 0:
            bullet.remove(b)
            bullet_count -= 1
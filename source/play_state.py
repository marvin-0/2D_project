from pico2d import*
import game_framework
import character_class
import monster1_class
import bullet_class
import stage_class
import map_class

rockman = None
monster1 = []
running = True
bullet = None
stage = None
bullet_count = 0
ground = None
ground_amount = 0

def enter():
    global rockman, running, monster1, bullet, bullet_count, stage, ground, ground_amount
    rockman = character_class.Main_char()
    monster1 = [monster1_class.Monster_I() for m in range(1)]
    bullet = []
    bullet_count = 0
    stage = stage_class.Stage()
    ground_amount = 100
    ground = [map_class.Ground() for m in range(ground_amount)]
    set_ground()
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
            if event.key == SDLK_c and rockman.jump_on == 0:
                rockman.jump_on = 1
                rockman.jump_dis = 0

def exit():
    global rockman
    del rockman

def update():
    gravity()
    char_ground()
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
    for g in ground:
        g.draw()
    for m in monster1:
        m.draw()
    for b in bullet:
        b.draw()
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
                    rockman.hp -= 10

def bullet_out():
    global bullet_count
    for b in bullet[:]:
        if b.x > 1000:
            bullet.remove(b)
            bullet_count -= 1
        elif b.x < 0:
            bullet.remove(b)
            bullet_count -= 1
def char_ground():
    global rockman
    for i in range(ground_amount):
        if rockman.y - 25 <= ground[i].y + 25 and rockman.y - 25 >= ground[i].y - 25:
            if (rockman.x + 10 > ground[i].x - 25 and rockman.x + 10 < ground[i].x + 25) or (rockman.x - 10 > ground[i].x - 25 and rockman.x - 10 < ground[i].x + 25):
                rockman.y += 4
                if rockman.jump_on != 0:
                    rockman.jump_on = 0
                    rockman.jump = 0
                    rockman.jump_dis = 0
        if rockman.y + 25 >= ground[i].y - 25 and rockman.y + 25 <= ground[i].y + 25:
            if (rockman.x + 10 > ground[i].x - 25 and rockman.x + 10 < ground[i].x + 25) or (rockman.x - 10 > ground[i].x - 25 and rockman.x - 10 < ground[i].x + 25):
                if rockman.jump == 1:
                    rockman.jump_on = 2

        if rockman.x + 10 <= ground[i].x + 25 and rockman.x + 10 >= ground[i].x - 25:
            if (rockman.y + 20 >= ground[i].y - 25 and rockman.y + 20 <= ground[i].y + 25) or (rockman.y - 20 >= ground[i].y - 25 and rockman.y - 20 <= ground[i].y + 25):
                rockman.x -= 5
        if rockman.x - 10 <= ground[i].x + 25 and rockman.x - 10 >= ground[i].x - 25:
            if (rockman.y + 20 >= ground[i].y - 25 and rockman.y + 20 <= ground[i].y + 25) or (rockman.y - 20 >= ground[i].y - 25 and rockman.y - 20 <= ground[i].y + 25):
                rockman.x += 5
    if rockman.y - 25 <= 0:
        rockman.y = 90
        rockman.x = 100


def gravity():
    global rockman
    rockman.y -= 4

def set_ground():
    for i in range(9):
        ground[i].y = 25
        ground[i].x = 50 * i + 25
    for i in range(9, 18):
        ground[i].y = 25
        ground[i].x = 625 + i % 9 * 50
    for i in range(18, 30):
        ground[i].y = 75 + i % 18 * 50
        ground[i].x = 975
    for i in range(30, 50):
        ground[i].y = 175
        ground[i].x = 875 - i % 30 * 50
    # ground[30].y = 175
    # ground[30].x = 875

    # ground[15].y = 150
    # ground[15].x = 475
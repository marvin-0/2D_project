from pico2d import*
import game_framework
import character_class
import monster1_class
import bullet_class
import stage_class
import map_class
import pause_state

rockman = None

running = True
bullet = None
stage = None
bullet_count = 0
ground = None
ground_amount = 0
spike_up = None

def enter():
    global rockman, running, bullet, bullet_count, stage, ground, ground_amount, spike_up
    rockman = character_class.Main_char()
    bullet = []
    bullet_count = 0
    stage = stage_class.Stage()
    ground_amount = 100
    ground = [map_class.Ground() for m in range(ground_amount)]
    spike_up = [map_class.Spike() for s in range(20)]
    set_ground()
    running = True

def handle_events():
    global running, bullet_count, bullet
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(pause_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
            exit()
            enter()
        else:
            rockman.handle_event(event)
def exit():
    global rockman, running, bullet, bullet_count, stage, ground, ground_amount, spike_up
    del rockman, running, bullet, bullet_count, stage, ground, ground_amount, spike_up

def update():
    gravity()
    char_ground()
    char_spike()
    rockman.update()
    for b in bullet:
        b.update()
    for s in spike_up:
        s.update()
    bullet_out()
    delay(0.01)

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
    for b in bullet:
        b.draw()
    for s in spike_up:
        s.draw()
    rockman.draw()

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
                if i == 55:
                    ground[i].x = 10000
                if i == 57:
                    spike_up[6].shot = 1
                rockman.y += 4
                if rockman.jump_on != 0 and i != 55:
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
    if rockman.y + 25 <= 0:
        rockman.hp -= 50

def char_spike():
    for s in spike_up[:]:
        if rockman.x >= s.x - 25 and rockman.x <= s.x + 25:
            if rockman.y >= s.y - 25 and rockman.y <= s.y + 25:
                rockman.hp -= 50

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
    ground[55].y = 175 + 300
    ground[55].x = 875 - 200
    ground[56].y = 175 + 200
    ground[56].x = 875 - 450
    ground[57].y = 175 + 250
    ground[57].x = 875 - 550
    ground[58].y = 175 + 200
    ground[58].x = 875 - 850

    for i in range(16):
        spike_up[i].y = 225
        spike_up[i].x = 50 * i + 25

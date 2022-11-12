from pico2d import*
import game_framework
import pause_state
import game_world

import character_class
import bullet_class
import back_ground_class
import map_class


rockman = None

bullet = []
bullet_count = 0
back_ground = None
ground = None
ground_amount = 0
spike_up = None
stage = 1
char_x, char_y = 100, 90

def enter():
    global rockman, back_ground, ground, ground_amount, spike_up
    rockman = character_class.Main_char(char_x, char_y) # 875 - 850, 175 + 500
    back_ground = back_ground_class.Back_ground()
    ground_amount = 100
    ground = [map_class.Ground() for m in range(ground_amount)]
    if stage == 1:
        spike_up = [map_class.Spike() for s in range(20)]
    elif stage == 2:
        spike_up = [map_class.Spike() for s in range(50)]
    if stage == 1:
        stage1()
    elif stage == 2:
        stage2()
    game_world.add_object(rockman, 2)
    game_world.add_object(back_ground, 0)
    game_world.add_objects(ground, 1)
    game_world.add_objects(spike_up, 3)

    game_world.add_collision_pairs(rockman, ground, 'char:ground')
    game_world.add_collision_pairs(rockman, spike_up, 'char:spike')

def handle_events():
    global stage, char_x, char_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(pause_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
            exit()
            enter()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            exit()
            stage = 1
            char_x, char_y = 100, 90
            enter()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
            exit()
            stage = 2
            char_x, char_y = 25, 90
            enter()
        else:
            rockman.handle_event(event)
def exit():
    game_world.clear()
    global rockman, back_ground, ground, ground_amount, spike_up
    del rockman, back_ground, ground, ground_amount, spike_up

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b) and group != 'char:ground':
            a.handle_collision(b, group)
            b.handle_collision(a, group)
            break
        elif group == 'char:ground':
            collide_ground(a, b)

    delay(0.01)

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

# def gravity():
#     global rockman
#     rockman.y -= 4
def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True

def collide_ground(a, b):
    la, ba, ra, ta = a.get_bb_ground() # self.x - 10, self.y - 25, self.x + 10, self.y + 25
    lb, bb, rb, tb = b.get_bb() # self.x - 25, self.y - 25, self.x + 25, self.y + 25

    # 땅 윗면
    if ba <= tb and ba >= bb:
        if (la + 5 > lb and la + 5 < rb) or (ra - 5 > lb and ra - 5 < rb):
            a.ground_collision(1, b)
            b.ground_collision(1, a)
    # 땅 아랫면
    if ta >= bb and ta <= tb:
        if (la + 5 > lb and la + 5 < rb) or (ra - 5 > lb and ra - 5 < rb):
            a.ground_collision(2, b)
            b.ground_collision(2, a)
    # 땅 왼면
    if ra <= rb and ra >= lb:
        if (ta - 5 <= tb and ta - 5 >= bb) or (ba + 5 <= tb and ba + 5 >= bb):
            a.ground_collision(3, b)
            b.ground_collision(3, a)
    # 땅 오른면
    if la >= lb and la <= rb:
        if (ta - 5 <= tb and ta - 5 >= bb) or (ba + 5 <= tb and ba + 5 >= bb):
            a.ground_collision(4, b)
            b.ground_collision(4, a)

    return False
def stage1():
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
        spike_up[i].y = 225
        spike_up[i].x = 50 * i + 25
    spike_up[16].y = 175 + 550
    spike_up[16].x = 875 - 550
    spike_up[17].y = 175 + 550
    spike_up[17].x = 875 - 225

def stage2():
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



    for i in range(19):
        spike_up[i].y = 25
        spike_up[i].x = 50 * i + 75
    for i in range(20, 37):
        spike_up[i].y = 75 + i % 20 * 50
        spike_up[i].x = -75
        spike_up[i].angle = 270
        spike_up[i].shot = 1
    spike_up[37].x = 550
    spike_up[37].y = 25 + 450

from pico2d import*
import game_framework
import pause_state
import game_world

import character_class
import bullet_class
import back_ground_class
import map_class


rockman = None

back_ground = None
ground = None
ground_amount = 0
spike_up = None
stage = 1
save_x, save_y = 100, 90

def enter():
    global rockman, back_ground, ground, ground_amount, spike
    rockman = character_class.Main_char(save_x, save_y) # 875 - 850, 175 + 500
    back_ground = back_ground_class.Back_ground()
    ground_amount = 100
    ground = [map_class.Ground() for m in range(ground_amount)]
    spike = [map_class.Spike() for s in range(100)]
    if stage == 1:
        map_class.stage1(ground, spike)
    elif stage == 2:
        map_class.stage2(ground, spike)
    game_world.add_object(rockman, 2)
    game_world.add_object(back_ground, 0)
    game_world.add_objects(ground, 1)
    game_world.add_objects(spike, 1)

    game_world.add_collision_pairs(rockman, ground, 'char:ground')
    game_world.add_collision_pairs(rockman, spike, 'char:spike')

def handle_events():
    global stage, save_x, save_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(pause_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
            reset_world()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            stage = 1
            save_x, save_y = 100, 90
            reset_world()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
            stage = 2
            save_x, save_y = 25, 90
            reset_world()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_3):
            stage = 3
            save_x, save_y = 25, 90
            rockman.reset_char(500, 900)
            map_class.stage_change()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_4):
            stage = 4
            save_x, save_y = 50, 90
            rockman.reset_char(100, 900)
            map_class.stage_change()
        else:
            rockman.handle_event(event)
def exit():
    game_world.clear()

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

def reset_world():
    global stage
    map_class.clear_map(ground, spike)
    if stage == 1:
        map_class.stage1(ground, spike)
    elif stage == 2 or stage == 3:
        stage = 2
        map_class.stage2(ground, spike)
    elif stage == 4:
        stage = 4
        map_class.stage4(ground, spike)
    rockman.reset_char(save_x, save_y)


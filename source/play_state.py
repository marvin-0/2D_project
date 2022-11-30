from pico2d import *
import server
import game_framework
import pause_state
import game_world

import character_class
import back_ground_class
import map_class

stage = 1
save_x, save_y = 100, 90

def enter():
    server.rockman = character_class.Main_char(save_x, save_y) # 875 - 850, 175 + 500
    server.back_ground = back_ground_class.Back_ground()
    server.ground_amount = 100
    server.ground = [map_class.Ground() for m in range(server.ground_amount)]
    server.spike = [map_class.Spike() for s in range(100)]
    if stage == 1:
        map_class.stage1(server.ground, server.spike)
    elif stage == 2:
        map_class.stage2(server.ground, server.spike)
    game_world.add_object(server.rockman, 2)
    game_world.add_object(server.back_ground, 0)
    game_world.add_objects(server.ground, 1)
    game_world.add_objects(server.spike, 1)

    game_world.add_collision_pairs(server.rockman, server.ground, 'rockman:ground')
    game_world.add_collision_pairs(server.rockman, server.spike, 'rockman:spike')

def handle_events():
    global stage, save_x, save_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(pause_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
            map_class.reset_world()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            stage = 1
            save_x, save_y = 100, 90
            map_class.reset_world()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
            stage = 2
            save_x, save_y = 25, 90
            map_class.reset_world()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_3):
            stage = 3
            save_x, save_y = 25, 90
            server.rockman.reset(500, 900)
            map_class.stage_change()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_4):
            stage = 4
            save_x, save_y = 50, 90
            server.rockman.reset(100, 900)
            map_class.stage_change()
        else:
            server.rockman.handle_event(event)
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b) and group != 'rockman:ground':
            a.handle_collision(b, group)
            b.handle_collision(a, group)
            break
        elif group == 'rockman:ground':
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




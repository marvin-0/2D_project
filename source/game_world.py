world = [[], [], [], []]
collision_group = dict()

def add_object(o, depth):
    world[depth].append(o)

def add_objects(ol, depth):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o) # 리스트로부터 삭제
            remove_collision_object(o)
            del o # 실제로 메모리 삭제
            return
    raise ValueError('Trying destroy on existing object')

def all_objects():
    for layer in world:
        for o in layer:
            yield o

def clear():
    global collision_group
    for o in all_objects():
        del o
    for layer in world:
        layer.clear()
    for a, b, group in all_collision_pairs():
        del a, b, group
    collision_group = {}

def add_collision_pairs(a, b, group):
    if group not in collision_group:
        collision_group[group] = [ [], [] ] # list of list : list pair
    if a not in collision_group[group]:
        if type(a) is list:
            collision_group[group][0] += a
        else:
            collision_group[group][0].append(a)
    if b not in collision_group[group]:
        if type(b) is list:
            collision_group[group][1] += b
        else:
            collision_group[group][1].append(b)
def all_collision_pairs():
    for group, pairs in collision_group.items():
        for a in pairs[0]:
            for b in pairs[1]:
                yield a, b, group

def remove_collision_object(o):
    for pairs in collision_group.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

world = [[], [], [], []]

def add_object(o, depth):
    world[depth].append(o)

def add_objects(ol, depth):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o) # 리스트로부터 삭제
            del o # 실제로 메모리 삭제
            return
    raise ValueError('Trying destroy on existing object')

def all_objects():
    for layer in world:
        for o in layer:
            yield o

def clear():
    for o in all_objects():
        del o
    for layer in world:
        layer.clear()

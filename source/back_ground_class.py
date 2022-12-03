import server
import play_state
from pico2d import *

class Back_ground:
    def __init__(self):
        self.image = load_image('sprite/map.png')
        self.stage_bgm = load_music('music/stage_bgm.mp3')
        self.font = load_font('font/neodgm.ttf', 20)
        self.stage_bgm.set_volume(32)
        self.stage_bgm.repeat_play()
        self.start_time = get_time()

    def draw(self):
        self.image.draw(500, 450)
        self.font.draw(880, 870, 'Time  : %d' % (server.time), (0, 0, 0))
        self.font.draw(880, 850, 'Death : %d' % (server.rockman.death_count), (0, 0, 0))
        if play_state.stage == 1:
            self.font.draw(20, 870, 'z: attack, c: jump,  arrow key: move, 1: boss teleportation', (0, 0, 0))
        elif play_state.stage == 4:
            self.font.draw(20, 870, 'q : boss hp 10', (0, 0, 0))
    def update(self):
        server.time = int(get_time() - self.start_time)
        pass

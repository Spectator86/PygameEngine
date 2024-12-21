from settings import *

class Timer:
    def __init__(self, maxt):
        self.max_time = maxt*FPS
        self.t = 0
    
    def update(self):
        if self.t >= self.max_time:
            return True
            self.t = 0
        else:
            self.t += 1
            return False

from settings import *

class SpriteAnim:
	def __init__(self, sprites, sec):
		self.sprites = sprites
		self.id = 0
		self.t = 0
		self.interval = sec * FPS

	def update(self):
		if self.t >= self.interval:
			if self.id < len(self.sprites)-1:
				self.id += 1
			else:
				self.id = 0
			self.t = 0
		else:
			self.t += 1

	def get_sprite(self):
		return self.sprites[self.id]

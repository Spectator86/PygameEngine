from settings import *
from entity import Entity

class Widget(Entity):
	def __init__(self, type_, **kwargs):
		super().__init__(**kwargs)
		self.type_ = type_
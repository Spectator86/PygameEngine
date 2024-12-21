import pygame as pg
from settings import *
from entity import Entity

class Canvas:
    def __init__(self, widgets):
        self.widgets = widgets

    def draw(self, sc):
        for widget in self.widgets:
            sc.blit(widget.image, (widget.rect.x, widget.rect.y))

    def update(self):
        for widget in self.widgets:
            x, y = pg.mouse.get_pos()
            if widget.type_ == "button":
                if x > self.rect.x and x < self.rect.x + self.scale_x:
                    if y > self.rect.y and y < self.rect.y + self.scale_y:
                        pass

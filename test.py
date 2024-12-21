#Imports
import pygame as pg
from settings import *

#Import classes
from entity import Entity
from canvas import Canvas
from anim import SpriteAnim

#Pygame init
pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Test Engine")

clock = pg.time.Clock()

path_image = "assets/images/"

#Objects of classes
plane = Entity(100, 100, 100, 100, f"{path_image}nocode.png")
plane_anim = SpriteAnim([f"{path_image}nocode.png", f"{path_image}plane.png", f"{path_image}plane.png", f"{path_image}plane.png"], 3)

#Lists
ANIMS = plane_anim

#Other variables

while True:
    #Fill screen
    sc.fill(BLACK)

    #Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    #Main code
    plane.draw(sc)
    plane.new_image(plane_anim.get_sprite())

    plane_anim.update()

    #Update screen
    pg.display.update()
    clock.tick()

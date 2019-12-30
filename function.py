#Import
from data import *

def init_game():
    # creat player
    player = Player()

    # creat labyrinth
    labyrinth = Map()

    # creat Items
    items = []
    for x in range(0, ITEMS_NB):

def move(event):
    #move the hero's position
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            res = "Gauche"
        if event.key == K_RIGHT:
            res = "Droite"
        if event.key == K_UP:
            res = "Haut"
        if event.key == K_DOWN:
            res = "Bas"
    return res
#Import
import pygame
from pygame.locals import *
import Map

def init_game():

    # creat labyrinth
    labyrinth = Map.Map("map.txt")
    labyrinth.generate_map()

    # creat player
    #player = Player()



    # creat Items
    #items = []
    #for x in range(0, ITEMS_NB):
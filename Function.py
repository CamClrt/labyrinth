from Map import Map
from Player import Player
from Item import Item
from data import *

def init_game(player_name):
    """init game : player, map and items"""

    map_list = []  # contain the matrix of the map
    items_positions = []  # contain all the position of the items

    #init player
    player = Player(player_name,0,0)

    #init map
    labyrinth = Map(URL_MAP)
    map_list = labyrinth.generate_maplist()

    #init items
    for n in range(len(ITEMS_LIST)):
        items = Item(ITEMS_LIST[n])
        items.putItems(*map_list)
        if n > 0: #avoid duplicate entry
            while items_positions[n-1] == (items.position_x, items.position_y):
                items.putItems(*map_list)
        items_positions.append((items.position_x, items.position_y))

    return player, labyrinth, items_positions, map_list
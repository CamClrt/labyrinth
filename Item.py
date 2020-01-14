import random

from data import SPRITE_SIZE


class Item():
    """create the items"""

    def __init__(self,item_url):
        """init player"""
        self.url = ""
        self.position_x = ""
        self.position_y = ""

    def put_items(self,*maplist):
        """Put items randomly on the map and check if it's possible"""
        self.position_x = random.randint(0, (len(maplist) - 1))
        self.position_y = random.randint(1, (len(maplist[0]) - 2))

        while maplist[self.position_y][self.position_x] == "x":
            self.position_x = random.randint(0, (len(maplist) - 1))
            self.position_y = random.randint(1, (len(maplist[0]) - 2))

    def get_position(self):
            """return the current position of the item"""
            position = (self.position_x * SPRITE_SIZE, self.position_y * SPRITE_SIZE)
            return position
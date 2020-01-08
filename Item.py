import random

class Item():
    """A commenter"""

    #ATTRIBUTES
    def __init__(self,item_name):
        self.name = item_name
        self.position_x = ""
        self.position_y = ""

    #METHODES
    def putItems(self,*maplist):
        """Put items randomly on the map and check if it's possible"""
        self.position_x = random.randint(0, (len(maplist) - 1))
        self.position_y = random.randint(1, (len(maplist[0]) - 2))

        while maplist[self.position_y][self.position_x] == "x":
            self.position_x = random.randint(0, (len(maplist) - 1))
            self.position_y = random.randint(1, (len(maplist[0]) - 2))


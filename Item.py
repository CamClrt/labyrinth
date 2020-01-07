from data import *
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
        """Put items randomly on the map"""
        self.position_x = random.randint(0,(len(maplist)-1))
        self.position_y = random.randint(0,(len(maplist[0])-1))

    #TEST

    # init items
    #items = Item(**ITEMS)
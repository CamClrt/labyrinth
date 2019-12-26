#import
import random
from data import *

Index = 0
ItemList = []

class Items():
    """documenter"""

    def __init__(self,nom,image):
        #init Items
        self.nom = nom
        self.image = image

    def define_position_items(self):
        #Define_position randomly items
        for i in range(ITEMS):
            Index = randint(0,len(Map.PATH))
            ItemList = Map.PATH[Index]
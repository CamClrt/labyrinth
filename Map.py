class Map():
    """documenter"""

#import matrix
from data import *

START = []
FINISH = []
PATH = []

def __init__(self):
    #init map
    self._map = LABYRINTH #Protect the matrix

@classmethod
def rightPath(cls):
    #define the right paths, the start and the finish locations
    for l in range(len(LABYRINTH)): #matrix's line
        for c in  range(len(LABYRINTH)): #matrix's column
            if LABYRINTH[l][c] == 0: #path
                PATH.append((l,c))
            elif LABYRINTH[l][c] == "S": #start
                PATH.append((l,c))
            elif LABYRINTH[l][c] == "F": #finish
                PATH.append((l, c))

    # comment créer 3 objets, comment les stocker, comment les placer sur la map
    def define_position_items(self):
        #Define_position randomly items
        for i in range(ITEMS):
            Index = randint(0,len(Map.PATH))
            ItemList = Map.PATH[Index]

labyrinth = Map()

print(START)
print(FINISH)
print(PATH)
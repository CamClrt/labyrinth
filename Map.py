class Map():
    """documenter"""

#import matrix
from data import *

START = []
FINISH = []
PATH = []

def __init__(self,LABYRINTH):
    #init map
    self._map = LABYRINTH #Protect the matrix

@classmethod
def rightPath(cls):
    #define the right paths, the start and the finish locations
    for l in range(len(LABYRINTH)): #matrix's line
        for c in  range(len(LABYRINTH)): #matrix's column
            if LABYRINTH[l][c] == "O": #path
                PATH.append((l,c))
            elif LABYRINTH[l][c] == "S": #start
                PATH.append((l,c))
            elif LABYRINTH[l][c] == "F": #finish
                PATH.append((l, c))
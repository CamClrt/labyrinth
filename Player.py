#import
from Map import *

class Player():
    """documenter"""

ITEMS_COLLECTION = []

    def __init__(self,x,y,position):
        #init player
        self.name = "MacGyver"
        self.image = "player_url"
        self.x = x
        self.y = y
        self.position = position #A revoir ou : (x,y) ?

#METHODE DE CLASSE CF DOC OC
#Une méthode de classe est une fonction dont le champ d'action s'étend à l'ensemble de la classe.
#Elles sont souvent utilisées pour créer de nouvelles instances à travers des boucles ou pour modifier des attributs de classe.
#Ici x & y ?

    def goRight(self):
        #move to right
        self.y = self.y + 1

    def goLeft(self):
        #move to left
        self.y = self.y - 1

    def goUp(self):
        #move to up
        self.x = self.x - 1

    def goDown(self):
        #move to down
        self.x = self.x + 1
class Player():
    """documenter >>> son rôle écouter ce qu'il y a sur le clavier >>> listener il va modifier la position du joueur dans la matrice"""

    #ATTRIBUTES
    def __init__(self):
        #init player
        self.name = "MacGyver"
        self.x = 0
        self.y = 0

    #METHODES
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

    def move(self,direction):
        #update position
        return direction[x][y]

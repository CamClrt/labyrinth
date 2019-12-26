class Position():
    """documenter"""

    def __init__(self,x,y):
        #init position
        self.x = x
        self.y = y

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

    def rightPath(self):
        #check if the move is possible

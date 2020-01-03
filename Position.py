class Position():
    """documenter"""

    #ATTRIBUTES
    def __init__(self,x,y):
        #init position
        self.x = x
        self.y = y

    # METHODES
    def goRight(self):
        # move to right
        self.x = self.x + 1

    def goLeft(self):
        # move to left
        self.x = self.x - 1

    def goUp(self):
        # move to up
        self.y = self.y - 1

    def goDown(self):
        # move to down
        self.y = self.y + 1
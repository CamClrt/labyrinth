class Position():
    """Move the player into the labyrinth"""

    #ATTRIBUTES
    def __init__(self,x,y):
        #init position
        self.x = x #abscissa
        self.y = y #ordinate

    # METHODES
    def goRight(self,*list):
        """move to right"""
        res = ""
        self.x += 1
        res = "Path"
        try:
            list[self.y][self.x]
        except IndexError:
            self.x -= 1 #cancel the move
            res = "Wall"
        if list[self.y][self.x] == "x":
            self.x -= 1 #cancel the move
            res = "Wall"
        return res

    def goLeft(self,*list):
        """move to left"""
        res = ""
        self.x -= 1
        res = "Path"
        if self.x < 0:
            self.x += 1 #cancel the move
            res = "Wall"
        if list[self.y][self.x] == "x":
            self.x += 1 #cancel the move
            res = "Wall"
        return res

    def goUp(self,*list):
        """move to up"""
        res = ""
        self.y -= 1
        res = "Path"
        if self.y < 0:
            self.y += 1 #cancel the move
            res = "Wall"
        if list[self.y][self.x] == "x":
            self.y += 1 #cancel the move
            res = "Wall"
        return res

    def goDown(self,*list):
        """move to down"""
        res = ""
        self.y += 1
        res = "Path"
        try:
            list[self.y][self.x]
        except IndexError:
            self.y -= 1 #cancel the move
            res = "Wall"
        if list[self.y][self.x] == "x":
            self.y -= 1 #cancel the move
            res = "Wall"
        return res
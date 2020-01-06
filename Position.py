class Position():
    """documenter"""

    #ATTRIBUTES
    def __init__(self,x,y):
        #init position
        self.x = x #abscissa
        self.y = y #ordinate

    # METHODES
    def goRight(self,*list):
        # move to right
        res = ""
        self.x = self.x + 1
        if self.x > len(list)-1:
            res = "Invalid movement on right, you will be out the zone"
            self.x = self.x - 1  # cancel the movement
        elif list[self.y][self.x] is "o":
            res = "Path"
        elif list[self.y][self.x] is "x":
            res = "Wall"
            self.x = self.x - 1 #cancel the movement
        elif list[self.y][self.x] is "F":
            res = "You win !"
        return res

    def goLeft(self,*list):
        # move to left
        res = ""
        self.x = self.x - 1
        if self.x < 0:
            res = "Invalid movement on left, you will be out the zone"
            self.x = self.x + 1  # cancel the movement
        elif list[self.y][self.x] is "o":
            res = "Path"
        elif list[self.y][self.x] is "x":
            res = "Wall"
            self.x = self.x + 1  # cancel the movement
        elif list[self.y][self.x] is "F":
            res = "You win !"
        return res


    def goUp(self,*list):
        # move to up
        res = ""
        self.y = self.y - 1
        if self.y < 0:
            res = "Invalid movement on up, you will be out the zone"
            self.y = self.y + 1  # cancel the movement
        elif list[self.y][self.x] is "o":
            res = "Path"
        elif list[self.y][self.x] is "x":
            res = "Wall"
            self.y = self.y + 1  # cancel the movement
        elif list[self.y][self.x] is "F":
            res = "You win !"
        return res

    def goDown(self,*list):
        # move to down
        res = ""
        self.y = self.y + 1
        if self.y > len(list)-1:
            res = "Invalid movement on down, you will be out the zone"
            self.y = self.y - 1  # cancel the movement
        elif list[self.y][self.x] is "o":
            res = "Path"
        elif list[self.y][self.x] is "x":
            res = "Wall"
            self.y = self.y - 1 #cancel the movement
        elif list[self.y][self.x] is "F":
            res = "You win !"
        return res
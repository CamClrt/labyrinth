from data import SPRITE_SIZE

class Player():
    """to create the player"""

    #ATTRIBUTES
    def __init__(self,name,x,y):
        """init player"""
        self.name = name
        self.x = x #abscissa
        self.y = y #ordinate

    #METHODES
    def go_right(self,*list):
        """try to move to right"""
        self.x += 1
        try:
            list[self.y][self.x]
        except IndexError:
            self.x -= 1 #cancel the move
        if list[self.y][self.x] == "x":
            self.x -= 1 #cancel the move

    def go_left(self,*list):
        """try to move to left"""
        self.x -= 1
        if self.x < 0:
            self.x += 1 #cancel the move
        if list[self.y][self.x] == "x":
            self.x += 1 #cancel the move

    def go_up(self,*list):
        """try to move to up"""
        self.y -= 1
        if self.y < 0:
            self.y += 1 #cancel the move
        if list[self.y][self.x] == "x":
            self.y += 1 #cancel the move

    def go_down(self,*list):
        """try to move to down"""
        self.y += 1
        try:
            list[self.y][self.x]
        except IndexError:
            self.y -= 1 #cancel the move
        if list[self.y][self.x] == "x":
            self.y -= 1 #cancel the move

    def get_position(self):
        """return the current position of player"""
        position = (self.x * SPRITE_SIZE,self.y * SPRITE_SIZE)
        return position
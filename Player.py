import Position

class Player():
    """documenter"""

    #ATTRIBUTES
    def __init__(self,name):
        #init player
        self.name = name
        #self.position = Position()

    #METHODES
    #Créer une méthode qui retourne le nom


    #Approfondir cette partie
    def get_position(self):
        return self.position

    def move_right(self):
        self.position.goRight()
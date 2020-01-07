import Position

class Player():
    """documenter"""

    #ATTRIBUTES
    def __init__(self):
        #init player
        self.name = "MacGyver"
        self.position = Position()

    #METHODES
    #Créer une méthode qui retourne le nom


    #Approfondir cette partie
    def get_position(self):
        return self.position

    def move_right(self):
        self.position.goRight()
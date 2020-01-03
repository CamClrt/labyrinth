from Map import Map
from Player import Player
from Position import Position

#init player
only_player = Player()
print("\nWelcome to the labyrinth {} !".format(only_player.name))

#init map
labyrinth = Map()
print("\nWill you find the exit ?\n")
print(labyrinth.display_map())

position_labyrinth = labyrinth.map_structure
print(position_labyrinth)

#Print("Vous êtes actuellement positionné en {}".format(???))
#direction = input("\nWhich position do you want to take? U = Up, D = Down, L = Left and R = Right : ")
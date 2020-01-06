from Map import Map
from Player import Player
from Position import Position

maplist = [] #contain the matrix of the map
conditions = False #while the player is not at the end of the labyrinth
command = ""
direction = ""

#init player
only_player = Player()
print("\nWelcome to the labyrinth {} !".format(only_player.name))

#init map
labyrinth = Map()
print("\nWill you find the exit ?\n")
print(labyrinth.display_map())
maplist = labyrinth.generate_maplist()

#init position
position = Position(0,0)

print("\nYour actual position is (x: {} ,y: {})".format(position.x,position.y))

while conditions == False :
    command = input("\nWhich position do you want to take ? U = Up, D = Down, L = Left and R = Right : ")
    if command == "D" or command == "d":
        direction = position.goDown(*maplist)
    elif command == "U" or command == "u":
        direction = position.goUp(*maplist)
    elif command == "L" or command == "l":
        direction = position.goLeft(*maplist)
    elif command == "R" or command == "r":
        direction = position.goRight(*maplist)
    else:
        direction = "Command not found"
    x = position.x
    y = position.y
    print("\n{} : Your current position is (x: {} ,y: {})".format(direction,position.x,position.y))

    if x == 13 and y == 14:
        conditions = True
        print("Congrats ! You reach the goal !!!")
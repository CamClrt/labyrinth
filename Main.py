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

#Init position
position = Position(0,0)

print("\nYour actual position is ({},{})".format(position.x,position.y))

x = position.x
y = position.y

while x != 1 and y != 1:
    direction = input("\nWhich position do you want to take ? U = Up, D = Down, L = Left and R = Right : ")
    if direction == "D" or direction == "d":
        position.goDown()
    elif direction == "U" or direction == "u":
        position.goUp()
    elif direction == "L" or direction == "l":
        position.goLeft()
    elif direction == "R" or direction == "r":
        position.goRight()
    else:
        print("Command not found")
    x = position.x
    y = position.y
    print("\nYour new position is : ({},{})".format(position.x,position.y))

print("You win !!!")
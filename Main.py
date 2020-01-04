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

#init position
position = Position(0,0)

print("\nYour actual position is ({},{})".format(position.x,position.y))

conditions = False
x = position.x
y = position.y
if x == 0 and y == 0:
    conditions = True

while conditions == False :
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
    if x == 0 and y == 0:
        conditions = True

print("Congrats ! You reach the goal !!!")
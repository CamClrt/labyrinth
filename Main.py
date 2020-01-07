from data import *
from Map import Map
from Item import Item
from Player import Player
from Position import Position

maplist = [] #contain the matrix of the map
game_conditions = False #while the player is not at the end of the labyrinth
player_command = "" #the command of the player
player_direction = "" #where the player want to go

#init player
player = Player()
print("\nWelcome to the labyrinth {} !".format(player.name))

#init map
labyrinth = Map()
print("\nWill you find the exit ?\n")
print(labyrinth.display_map())
maplist = labyrinth.generate_maplist()

# init items
print("\nWill you find the 3 items before the exit ?")
for n in range(len(ITEMS_LIST)):
    items = Item(ITEMS_LIST[n])
    res = items.putItems(*maplist)
    print("\n >>> {} (x: {}, y: {}) res: {}".format(items.name,items.position_x,items.position_y,res))

#init position
player_position = Position(0, 0)

print("\nYour actual position is (x: {} ,y: {})".format(player_position.x, player_position.y))

while game_conditions == False :
    player_command = input("\nWhich position do you want to take ? U = Up, D = Down, L = Left and R = Right : ")
    if player_command == "D" or player_command == "d":
        player_direction = player_position.goDown(*maplist)
    elif player_command == "U" or player_command == "u":
        player_direction = player_position.goUp(*maplist)
    elif player_command == "L" or player_command == "l":
        player_direction = player_position.goLeft(*maplist)
    elif player_command == "R" or player_command == "r":
        player_direction = player_position.goRight(*maplist)
    else:
        player_direction = "Command not found"
    x = player_position.x
    y = player_position.y
    print("\n{} : Your current position is (x: {} ,y: {})".format(player_direction, player_position.x, player_position.y))

    if x == 13 and y == 14:
        game_conditions = True
        print("Congrats ! You reach the goal !!!")
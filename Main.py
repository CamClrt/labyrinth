from data import *
from Map import Map
from Item import Item
from Player import Player
from Position import Position

map_list = [] #contain the matrix of the map
game_condition = False #while the player is not at the end of the labyrinth
player_name = ''
player_command = "" #the command of the player
player_direction = "" #where the player want to go
items_positions_list = [] #contain all the position of the items
items_counter_set = set() #determine the number of items collected

#init player
player_name = str(input("What's your name ? : "))
player = Player(player_name)
print("\nWelcome to the labyrinth {} !".format(player.name))

#init map
labyrinth = Map(URL_MAP)
print("\nWill you find the exit ?\n")
print(labyrinth.display_map())
map_list = labyrinth.generate_maplist()

#init items
print("\nWill you find the 3 items before the exit ?")
for n in range(len(ITEMS_LIST)):
    items = Item(ITEMS_LIST[n])
    items.putItems(*map_list)
    items_positions_list.append((items.position_x,items.position_y))
    print("\n >>> {} (x: {}, y: {})".format(items.name,items.position_x,items.position_y))
    #voir comment faire pour positionner les objets directement lors de la création de la map
    #voir comment = aller mettre/positionner les 3 objets directement dans la liste de liste ?

#init position
player_position = Position(0, 0)

print("\nYour actual position is (x: {} ,y: {})".format(player_position.x, player_position.y))

while game_condition == False :
    player_command = input("\nWhich position do you want to take ? U = Up, D = Down, L = Left and R = Right : ")
    if player_command == "D" or player_command == "d":
        player_direction = player_position.goDown(*map_list) #à gérer avec Player
    elif player_command == "U" or player_command == "u":
        player_direction = player_position.goUp(*map_list) #à gérer avec Player
    elif player_command == "L" or player_command == "l":
        player_direction = player_position.goLeft(*map_list) #à gérer avec Player
    elif player_command == "R" or player_command == "r":
        player_direction = player_position.goRight(*map_list) #player.move_right()
    else:
        player_direction = "Command not found"
    x = player_position.x #à gérer avec Player
    y = player_position.y #à gérer avec Player
    player_position_tuple = (player_position.x,player_position.y) #à gérer avec Player
    print("\n{} : Your current position is {}".format(player_direction, player_position_tuple))

    for n in range(len(items_positions_list)):
        item_position_tuple = items_positions_list[n]
        if item_position_tuple == player_position_tuple:
            items_counter_set.add(item_position_tuple)
    print("You have collected",len(items_counter_set),"items")

    if player_position_tuple == (13, 14):
        if len(items_counter_set) == len(items_positions_list):
            game_condition = True
            print("You win !!!")
        else:
            print("You lose")
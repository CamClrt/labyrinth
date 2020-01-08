from Function import *

map_list = [] #contain the matrix of the map DOUBLON AVEC FONCTION ?
game_condition = False #while the player is not at the end of the labyrinth
player_name = "" #determine the name of the player
player_command = "" #the command of the player
items_counter = "" #determine the number of items collected

#Main code

player_name = str(input("Welcome into labyrinth, what's your name ? : "))

player, labyrinth, items_positions, map_list = init_game(player_name)

print("\n {} : will you find the exit ?\n".format(player.name))
print(labyrinth.display_map(),"\n")
print("Before finding the exit, you have to collect 3 items located at :",items_positions,"\n")
print("Your actual position is {})".format(player.get_position(),"\n"))

while game_condition == False :
    player_command = input("\nWhich position do you want to take ? U = Up, D = Down, L = Left and R = Right : ")
    if player_command == "D" or player_command == "d":
        player.goDown(*map_list)
    elif player_command == "U" or player_command == "u":
        player.goUp(*map_list)
    elif player_command == "L" or player_command == "l":
        player.goLeft(*map_list)
    elif player_command == "R" or player_command == "r":
        player.goRight(*map_list)
    else:
        print("Command not found")

    print("\nYour current position is {}".format(player.get_position()))

    items_counter = items_collected(*items_positions)
    print("You have collected",len(items_counter),"items")

    if player.get_position() == (13, 14):
        if len(items_counter_set) == len(items_positions):
            game_condition = True
            print("You win !!!")
        else:
            print("You lose")
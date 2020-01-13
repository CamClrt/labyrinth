from Function import *
import pygame
from pygame.locals import *

map_list = [] #contain the matrix of the map
player_name = "" #determine the name of the player
#items_collected_position = "" #store the items' position collected
#items_counter = set() #determine the number of items collected
close_window = False
game_condition = False
x_wall = 0 #collect the abscissa of the wall
y_wall = 0 #collect the ordinate of the wall
x_item = 0 #collect the abscissa of the item
y_item = 0 #collect the ordinate of the wall


#MAIN CODE

#init game
player, labyrinth, items_positions, map_list = init_game(PLAYER_NAME)

#init pygame
pygame.init()

#set the empty window and its title
pygame.display.set_caption(WINDOW_TITLE) #determine the title
window = pygame.display.set_mode((WINDOW_SIZE,WINDOW_SIZE)) #determine the size of the window
background = pygame.image.load(BACKGROUND).convert() #load the background
window.blit(background, (0,0)) #stick the background

#refresh the screen
pygame.display.flip()

#limit the FPS
pygame.time.Clock().tick(1) #FPS > notion à revoir frame per second

#move the player with the down, up, left and right buttons and quit the game
while close_window == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #quit the programe
            close_window = True
        elif event.type == KEYDOWN and event.key == K_DOWN:
            player.go_down(*map_list)
        elif event.type == KEYDOWN and event.key == K_UP:
            player.goUp(*map_list)
        elif event.type == KEYDOWN and event.key == K_LEFT:
            player.goLeft(*map_list)
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            player.goRight(*map_list)

        #stick the background on the map
        window.blit(background,(0,0))

        #set a part of the wall on the map
        wall = pygame.image.load(WALL_PICTURE_URL)

        #stick the wall on the map
        for line in range(len(map_list)):
            for element in range(len(map_list)):
                if map_list[line][element] == "x":
                    x_wall = element * SPRITE_SIZE
                    y_wall = line * SPRITE_SIZE
                    window.blit(wall, (x_wall, y_wall), (160, 160, 40, 20)) #40*20
                    window.blit(wall, (x_wall, y_wall + 20), (160, 160, 40, 20)) #40*20

        #set and stick the items on the map
        for element in range(len(ITEMS_LIST)):
            item = pygame.image.load(ITEMS_LIST[element]).convert_alpha()
            x_item, y_item = items_positions[element]
            window.blit(pygame.transform.scale(item, (40, 40)), (x_item * SPRITE_SIZE, y_item * SPRITE_SIZE))

        #set and stick the player on the map
        player_picture = pygame.image.load(PLAYER_PICTURE_URL).convert_alpha()  #load the player image
        window.blit(player_picture, player.get_position())  #stick the player

        #set and stick the guard on the map
        guard_picture = pygame.image.load(GUARD_PICTURE_URL).convert()
        window.blit(guard_picture, FINISH_PX)

        #refresh the window
        pygame.display.flip()

        #collect the items



        #win and close if the player reach the guard
        if player.get_position() == FINISH_PX: #si position player == position garde > A CORRIGER
            close_window = True



        """for n in range(len(items_positions)):
            items_collected_position = items_positions[n]
            if items_collected_position == player_position:
                items_counter.add(items_collected_position)
        print("You have collected", len(items_counter), "items")

        if player.get_position() == FINISH:
            if len(items_counter) == len(items_positions):
                game_condition = True
                print("You win !!!")
            else:
                print("You lose")"""
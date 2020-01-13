from Function import *
import pygame
from pygame.locals import *

close_window = False
game_condition = False
map_list = [] #contain the matrix of the map
item_collected = "" #contain the name of the item collected
item_tuple = "" #contain the positions of the items
x_wall = 0 #collect the abscissa of the wall
y_wall = 0 #collect the ordinate of the wall
x_item = 0 #collect the abscissa of the item
y_item = 0 #collect the ordinate of the wall


#MAIN CODE

#init game
player, labyrinth, items_dictionary, map_list = init_game(PLAYER_NAME)

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
            player.go_up(*map_list)
        elif event.type == KEYDOWN and event.key == K_LEFT:
            player.go_left(*map_list)
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            player.go_right(*map_list)

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
        for key, value in items_dictionary.items():
            item = pygame.image.load(key).convert_alpha()
            item_tuple = value
            window.blit(pygame.transform.scale(item, (40, 40)), (item_tuple[0], item_tuple[1]))

        #set and stick the player on the map
        player_picture = pygame.image.load(PLAYER_PICTURE_URL).convert_alpha()  #load the player image
        window.blit(player_picture, player.get_position())  #stick the player

        #set and stick the guard on the map
        guard_picture = pygame.image.load(GUARD_PICTURE_URL).convert()
        window.blit(guard_picture, FINISH_PX)

        #refresh the window
        pygame.display.flip()

        #collect item
        for key, value in items_dictionary.items():
            if player.get_position() == value:
                item_collected = key
        if item_collected != "":
            items_dictionary.pop(item_collected,"")

        #win and close if the player reach the guard
        if player.get_position() == FINISH_PX: #si position player == position garde > A CORRIGER
            close_window = True
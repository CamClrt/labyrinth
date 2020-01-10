from Function import *
import pygame
from pygame.locals import *

map_list = [] #contain the matrix of the map DOUBLON AVEC FONCTION ?
player_name = "" #determine the name of the player
player_command = "" #the command of the player
items_collected_position = "" #store the items' position collected
items_counter = set() #determine the number of items collected
player_position = "" #pygame object : rect
close_window = False
game_condition = False

#MAIN CODE

#init game
player, labyrinth, items_positions, map_list = init_game(PLAYER_NAME)

#init pygame
pygame.init()

#set the window and its title
pygame.display.set_caption(WINDOW_TITLE) #determine the title
window = pygame.display.set_mode((WINDOW_SIZE,WINDOW_SIZE)) #determine the size of the window
background = pygame.image.load(BACKGROUND).convert() #load the background
window.blit(background, (0,0)) #stick the background

#set the player on the map
player_picture = pygame.image.load(PLAYER_PICTURE_URL).convert_alpha() #load the player image
player_position = player_picture.get_rect() #init rect (or move)
window.blit(player_picture, player_position) #stick the player

#set the guard on the map
guard_picture = pygame.image.load(GUARD_PICTURE_URL).convert()

#set a part of the wall on the map
wall = pygame.image.load(WALL_PICTURE_URL)

#refresh the screen
pygame.display.flip()

#move the player with the down, up, left and right buttons and quit the game
while close_window == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #quit the programe
            close_window = True
        elif event.type == KEYDOWN and event.key == K_DOWN:
            res = player.goDown(*map_list)
            if res == "Path":
                player_position = player_position.move(0, SPRITE_SIZE)
        elif event.type == KEYDOWN and event.key == K_UP:
            res = player.goUp(*map_list)
            if res == "Path":
                player_position = player_position.move(0, -SPRITE_SIZE)
        elif event.type == KEYDOWN and event.key == K_LEFT:
            res = player.goLeft(*map_list)
            if res == "Path":
                player_position = player_position.move(-SPRITE_SIZE,0)
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            res = player.goRight(*map_list)
            if res == "Path":
                player_position = player_position.move(SPRITE_SIZE, 0)


        #stick the background, the player and the guard on the map
        window.blit(background,(0,0))
        window.blit(player_picture, player_position)
        window.blit(guard_picture, FINISH_PX)

        #stick the wall on the map
        for line in range(len(map_list)):
            for element in range(len(map_list)):
                if map_list[line][element] == "x":
                    x = element * SPRITE_SIZE
                    y = line * SPRITE_SIZE
                    window.blit(wall, (x, y), (160, 160, 40, 20))
                    window.blit(wall, (x, y + 20), (160, 160, 40, 20))

        #Refresh the window
        pygame.display.flip()
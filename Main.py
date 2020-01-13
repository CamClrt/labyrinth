from Function import *
from data import *

close_window = False
game_condition = False
map_list = [] #contain the matrix of the map
item_collected = "" #contain the name of the item collected
item_tuple = "" #contain the positions of the items
x_wall = 0 #collect the abscissa of the wall
y_wall = 0 #collect the ordinate of the wall
x_item = 0 #collect the abscissa of the item
y_item = 0 #collect the ordinate of the item

home_page = True
game_page = True
end_page_win = False
end_page_lose = False


# MAIN CODE

# init pygame
pygame.init()

# init home page
while home_page == True:
    home_button = init_home_page()

    # limit the FPS
    pygame.time.Clock().tick(10)  # FPS > notion à revoir frame per second

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if home_button.collidepoint(event.pos) == True:
                home_page = False

# init game
player, labyrinth, items_dictionary, map_list = init_game(PLAYER_NAME)

# init window for the game
window, background = init_window_game()

# move the player with the down, up, left and right buttons and quit the game
while game_page == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit the programe
            close_window = True
        elif event.type == KEYDOWN and event.key == K_DOWN:
            player.go_down(*map_list)
        elif event.type == KEYDOWN and event.key == K_UP:
            player.go_up(*map_list)
        elif event.type == KEYDOWN and event.key == K_LEFT:
            player.go_left(*map_list)
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            player.go_right(*map_list)

        # stick the background on the map
        window.blit(background,(0,0))

        # set a part of the wall on the map
        wall = pygame.image.load(WALL_PICTURE_URL)

        # stick the wall on the map
        for line in range(len(map_list)):
            for element in range(len(map_list)):
                if map_list[line][element] == "x":
                    x_wall = element * SPRITE_SIZE
                    y_wall = line * SPRITE_SIZE
                    window.blit(wall, (x_wall, y_wall), (160, 160, 40, 20)) #40*20
                    window.blit(wall, (x_wall, y_wall + 20), (160, 160, 40, 20)) #40*20

        # set and stick the items on the map
        for key, value in items_dictionary.items():
            item = pygame.image.load(key).convert_alpha()
            item_tuple = value
            window.blit(pygame.transform.scale(item, (40, 40)), (item_tuple[0], item_tuple[1]))

        # set and stick the player on the map
        player_picture = pygame.image.load(PLAYER_PICTURE_URL).convert_alpha()  #load the player image
        window.blit(player_picture, player.get_position())  #stick the player

        # set and stick the guard on the map
        guard_picture = pygame.image.load(GUARD_PICTURE_URL).convert()
        window.blit(guard_picture, FINISH_PX)

        # refresh the window
        pygame.display.flip()

        # collect item
        for key, value in items_dictionary.items():
            if player.get_position() == value:
                item_collected = key
        if item_collected != "":
            items_dictionary.pop(item_collected,"")

        # win and close if the player reach the guard
        if player.get_position() == FINISH_PX:
            game_page = False
            if len(items_dictionary) == 0:
                end_page_win = True
            else:
                end_page_lose = True

        # refresh the screen
        pygame.display.flip()

while end_page_win == True:
    # set the empty window and its title
    pygame.display.set_caption(WINDOW_TITLE)  # determine the title
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))  # determine the size of the window
    end_page = pygame.image.load(WIN_URL).convert()  # load the background
    window.blit(pygame.transform.scale(end_page, (WINDOW_SIZE, WINDOW_SIZE)), (0, 0))

    # refresh the screen
    pygame.display.flip()

while end_page_lose == True:
    # set the empty window and its title
    pygame.display.set_caption(WINDOW_TITLE)  # determine the title
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))  # determine the size of the window
    end_page = pygame.image.load(LOSE_URL).convert()  # load the background
    window.blit(pygame.transform.scale(end_page, (WINDOW_SIZE, WINDOW_SIZE)), (0, 0))


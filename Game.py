from Map import Map
from Player import Player
from Item import Item

import pygame
from pygame.locals import *

from data import *


class Game:
    """launch the game"""
    def __init__(self):
        self.map_list = []  # contain the matrix of the map
        self.item_collected = ""  # contain the name of the item collected
        self.item_tuple = ""  # contain the positions of the items
        self.x_wall = 0  # collect the abscissa of the wall
        self.y_wall = 0  # collect the ordinate of the wall
        self.x_item = 0  # collect the abscissa of the item
        self.y_item = 0  # collect the ordinate of the item
        self.home_page = True # launch home page
        self.game_page = False # launch game page
        self.end_page_win = False # launch win page
        self.end_page_lose = False # launch lose page

    def start_game(self):
        """start the game"""
        # init pygame
        pygame.init()

        # init home page
        while self.home_page is True:

            self.home_button = self.init_home_page()

            # limit the FPS
            pygame.time.Clock().tick(30)  # FPS

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if self.home_button.collidepoint(event.pos) == True:
                        self.home_page = False
                        self.game_page = True
                if event.type == pygame.QUIT:
                    self.home_page = False

        # init game
        player, labyrinth, self.items_dictionary, self.map_list = self.init_game()

        # init window for the game
        window, background = self.init_game_page()

        # move the player with the down, up, left and right buttons or quit the game
        while self.game_page is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quit the program
                    self.game_page = False
                elif event.type == KEYDOWN and event.key == K_DOWN:
                    player.go_down(*self.map_list)
                elif event.type == KEYDOWN and event.key == K_UP:
                    player.go_up(*self.map_list)
                elif event.type == KEYDOWN and event.key == K_LEFT:
                    player.go_left(*self.map_list)
                elif event.type == KEYDOWN and event.key == K_RIGHT:
                    player.go_right(*self.map_list)

                # stick the background on the map
                window.blit(background, (0, 0))

                # set a part of the wall on the map
                wall = pygame.image.load(WALL_PICTURE_URL)

                # stick the wall on the map
                for line in range(len(self.map_list)):
                    for element in range(len(self.map_list)):
                        if self.map_list[line][element] == "x":
                            self.x_wall = element * SPRITE_SIZE
                            self.y_wall = line * SPRITE_SIZE
                            window.blit(wall, (self.x_wall, self.y_wall), (160, 160, 40, 20))  # 40*20
                            window.blit(wall, (self.x_wall, self.y_wall + 20), (160, 160, 40, 20))  # 40*20

                # set and stick the items on the map
                for key, value in self.items_dictionary.items():
                    item = pygame.image.load(key).convert_alpha()
                    item_tuple = value
                    window.blit(pygame.transform.scale(item, (40, 40)), (item_tuple[0], item_tuple[1]))

                # set and stick the player on the map
                player_picture = pygame.image.load(PLAYER_PICTURE_URL).convert_alpha()  # load the player image
                window.blit(player_picture, player.get_position())  # stick the player

                # set and stick the guard on the map
                guard_picture = pygame.image.load(GUARD_PICTURE_URL).convert()
                window.blit(guard_picture, FINISH_PX)

                # refresh the window
                pygame.display.flip()

                # collect item
                for key, value in self.items_dictionary.items():
                    if player.get_position() == value:
                        self.item_collected = key
                if self.item_collected != "":
                    self.items_dictionary.pop(self.item_collected, "")

                # refresh the screen
                pygame.display.flip()

                # win, if the player reach the guard with all the items collected
                if player.get_position() == FINISH_PX:
                    self.game_page = False
                    if len(self.items_dictionary) == 0:
                        self.end_page_win = True
                    else:
                        self.end_page_lose = True

        while self.end_page_win is True:

            self.init_win_page()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end_page_win = False

        while self.end_page_lose is True:

            self.init_lose_page()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end_page_lose = False

    def init_game(self):
        """init player, map and items"""
        map_list = []  # contain the matrix of the map
        items_positions = []  # contain all the position of the items

        # init player
        player = Player(0, 0)

        # init map
        labyrinth = Map(URL_MAP)
        map_list = labyrinth.generate_maplist()

        # init items
        items_dictionary = {}
        items_positions = []
        for n in range(len(ITEMS_LIST)):
            items = Item(ITEMS_LIST[n])  # generate the items object
            items.url = ITEMS_LIST[n]
            items.put_items(*map_list)
            if n > 0:  # avoid duplicate entry
                while items_positions[n - 1] == (items.position_x, items.position_y):
                    items.put_items(*map_list)
            items_positions.append((items.position_x, items.position_y))
            items_dictionary[items.url] = items.get_position()

        return player, labyrinth, items_dictionary, map_list

    def init_home_page(self):
        """set the empty window and its title"""
        pygame.display.set_caption(WINDOW_TITLE)  # determine the title
        window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))  # determine the size of the window
        home = pygame.image.load(HOME_URL).convert()  # load the background
        window.blit(pygame.transform.scale(home, (WINDOW_SIZE, WINDOW_SIZE)), (0, 0))

        # refresh the screen
        pygame.display.flip()

        # create button
        home_button = pygame.Rect(WELCOME_BUTTON)

        return home_button

    def init_game_page(self):
        """init window and title of the game page"""

        # set the empty window and its title
        pygame.display.set_caption(WINDOW_TITLE)  # determine the title
        window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))  # determine the size of the window
        background = pygame.image.load(BACKGROUND).convert()  # load the background
        window.blit(background, (0, 0))  # stick the background

        # refresh the screen
        pygame.display.flip()

        return window, background

    def init_win_page(self):
        """init window and title of the win page"""
        pygame.display.set_caption(WINDOW_TITLE)  # determine the title
        window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))  # determine the size of the window
        end_page = pygame.image.load(WIN_URL).convert()  # load the background
        window.blit(pygame.transform.scale(end_page, (WINDOW_SIZE, WINDOW_SIZE)), (0, 0))

        # refresh the screen
        pygame.display.flip()

    def init_lose_page(self):
        """init window and title of the lose page"""
        pygame.display.set_caption(WINDOW_TITLE)  # determine the title
        window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))  # determine the size of the window
        end_page = pygame.image.load(LOSE_URL).convert()  # load the background
        window.blit(pygame.transform.scale(end_page, (WINDOW_SIZE, WINDOW_SIZE)), (0, 0))

        # refresh the screen
        pygame.display.flip()

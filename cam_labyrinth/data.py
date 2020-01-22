from os import path

directory = path.dirname(__file__)

PLAYER_NAME = "MacGyver"

FINISH_PX = (520, 560)

URL_MAP = path.join(directory, "map.txt")

ITEMS_LIST = [
    path.join(directory, "resources/tube.png"),
    path.join(directory, "resources/needle.png"),
    path.join(directory, "resources/ether.png")
]

#graphic mode
WINDOW_TITLE = "The labyrinth"
BACKGROUND = path.join(directory, "resources/background.jpg")
PLAYER_PICTURE_URL = path.join(directory, "resources/player.png")
GUARD_PICTURE_URL = path.join(directory, "resources/guard.png")
WALL_PICTURE_URL = path.join(directory, "resources/wall20x20.png")
SPRITE_SIZE = 40
NB_SPRITE = 15
WINDOW_SIZE = SPRITE_SIZE * NB_SPRITE

HOME_URL = path.join(directory, "resources/home.png")
WIN_URL = path.join(directory, "resources/win.png")
LOSE_URL = path.join(directory, "resources/lose.png")
WELCOME_BUTTON = (125,330,250,75) #left, top, width, height

print(HOME_URL)

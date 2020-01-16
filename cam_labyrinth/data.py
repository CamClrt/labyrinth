import os

path = os.path.dirname(__file__)

PLAYER_NAME = "MacGyver"

FINISH_PX = (520, 560)

URL_MAP = os.path.join(path, "map.txt")

ITEMS_LIST = [
    os.path.join(path, "resources/burger.png"),
    os.path.join(path, "resources/needle.png"),
    os.path.join(path, "resources/lamp.png")
]

#graphic mode
WINDOW_TITLE = "The labyrinth"
BACKGROUND = os.path.join(path, "resources/background.jpg")
PLAYER_PICTURE_URL = os.path.join(path, "resources/player.png")
GUARD_PICTURE_URL = os.path.join(path, "resources/guard.png")
WALL_PICTURE_URL = os.path.join(path, "resources/wall20x20.png")
SPRITE_SIZE = 40
NB_SPRITE = 15
WINDOW_SIZE = SPRITE_SIZE * NB_SPRITE

HOME_URL = os.path.join(path, "resources/home.png")
WIN_URL = os.path.join(path, "resources/win.png")
LOSE_URL = os.path.join(path, "resources/lose.png")
WELCOME_BUTTON = (125,330,250,75) #left, top, width, height

print(HOME_URL)

import os

path = os.getcwd()
print(path)

PLAYER_NAME = "MacGyver"

FINISH_PX = (520, 560)

URL_MAP = os.path.join(path, "cam_labyrinth/map.txt")

ITEMS_LIST = [
    os.path.join(path, "cam_labyrinth/resources/burger.png"),
    os.path.join(path, "cam_labyrinth/resources/needle.png"),
    os.path.join(path, "cam_labyrinth/resources/lamp.png")]

#graphic mode
WINDOW_TITLE = "The labyrinth"
BACKGROUND = os.path.join(path, "cam_labyrinth/resources/background.jpg")
PLAYER_PICTURE_URL = os.path.join(path, "cam_labyrinth/resources/player.png")
GUARD_PICTURE_URL = os.path.join(path, "cam_labyrinth/resources/guard.png")
WALL_PICTURE_URL = os.path.join(path, "cam_labyrinth/resources/wall20x20.png")
SPRITE_SIZE = 40
NB_SPRITE = 15
WINDOW_SIZE = SPRITE_SIZE * NB_SPRITE

HOME_URL = os.path.join(path, "cam_labyrinth/resources/home.png")
WIN_URL = os.path.join(path, "cam_labyrinth/resources/win.png")
LOSE_URL = os.path.join(path, "cam_labyrinth/resources/lose.png")
WELCOME_BUTTON = (125,330,250,75) #left, top, width, height


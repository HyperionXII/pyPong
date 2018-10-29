from src.game.Paddle import *
from src.core.GameObject import GameObject
from src.game.Background import *

# Manager for the whole game
#
class GameManager(GameObject):

    # Ctor.
    #
    def __init__(self, screen):
        self.__screen = screen
        self.__paddle1 = Paddle(screen)
        self.__background = Background(screen)
        DebugLog("New GameManager Created")

    # Render
    #
    def Render(self, _screen):
        self.__background.Render()
        self.__paddle1.Render()

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

    # Handle events passed from pyGame
    #
    def process_event(self, event):
        if event.type == QUIT:
            DebugLog("Esc pressed")
            return
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                self.__paddle1.move_up()
            if event.key == K_DOWN:
                self.__paddle1.move_down()
        elif event.type == KEYUP:
            pass
            # if event.key == K_UP or event.key == K_DOWN:
            #     player.movepos = [0, 0]
            #     player.state = "still"

    # Called once per frame
    #
    def update(self):
        self.__paddle1.update()

    # Render
    #
    def Render(self, _screen):
        self.__background.Render()  # Always render the background first
        self.__paddle1.render()

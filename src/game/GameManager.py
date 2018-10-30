from src.core.GameObject import GameObject
from src.game.Background import *
from src.game.Ball import *
from src.game.Paddle import *


# Manager for the whole game
#
class GameManager(GameObject):

    # Ctor.
    #
    def __init__(self, screen):
        self._screen = screen
        self._paddle1 = Paddle(screen, 10)
        self._ball = Ball(screen)
        self._background = Background(screen)
        DebugLog("New GameManager Created")

    # Handle events passed from pyGame
    #
    def process_event(self, event):
        if event.type == QUIT:
            DebugLog("Esc pressed")
            return
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                self._paddle1.move_up()
            if event.key == K_DOWN:
                self._paddle1.move_down()
        elif event.type == KEYUP:
            pass
            # if event.key == K_UP or event.key == K_DOWN:
            #     player.movepos = [0, 0]
            #     player.state = "still"

    # Called once per frame
    #
    def update(self):
        self._ball.update()
        self._paddle1.update()

    # Render
    #
    def Render(self,):
        self._background.render()  # Always render the background first
        self._paddle1.render()
        self._ball.render()

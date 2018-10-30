from Debugging import *
from src.utils.ResourceUtils import *


# Container for the Ball functionality
#
class Ball(pygame.sprite.Sprite):

    # Ctor
    #
    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)
        self._surface = surface
        self._image, self._rect = load_image("ball.png")
        self._direction = "left"
        self._speed = 5
        surfaceRect = self._surface.get_rect()
        self._pos = [surfaceRect.width * 0.5, surfaceRect.height * 0.5]
        DebugLog("New Ball Created")

    # Called once per frame
    #
    def update(self):
        if self._direction == "left":
            self._pos[0] = self._pos[0] - self._speed
        elif self._direction == "right":
            self._pos[0] = self._pos[0] + self._speed
        self.check_boundaries()

    # Render the ball
    #
    def render(self):
        self._surface.blit(self._image, self._pos)

    # Keep the ball within the screen bounds
    #
    def check_boundaries(self):
        if self._direction == "left":
            if self._pos[0] < 0:
                self._pos[0] = 0
                self._direction = "right"
        elif self._direction == "right":
            rightPixel = self._pos[0] + self._rect.width
            if rightPixel > self._surface.get_rect().width:
                self._pos[0] = self._surface.get_rect().width - self._rect.width
                self._direction = "left"


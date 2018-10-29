import pygame

from Debugging import *
from src.core.GameObject import GameObject
from src.core.Vectors import *
from src.utils.ResourceUtils import *


# Paddle class
# 
class Paddle(pygame.sprite.Sprite):
    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self._image, self._rect = load_image('paddle.png')
        self._score = 0
        self._surface = surface
        DebugLog("New Paddle Created")

    # Get Paddle Score
    #
    def GetScore(self):
        return self._score

    # Render the paddle
    #
    def Render(self):
        self._surface.blit(self._image, self._rect)

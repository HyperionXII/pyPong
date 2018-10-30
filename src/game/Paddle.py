import pygame

from Debugging import *
from src.core.GameObject import GameObject
from src.core.Vectors import *
from src.utils.ResourceUtils import *


# Paddle class
# 
class Paddle(pygame.sprite.Sprite):
    def __init__(self, surface, xPos):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self._image, self._rect = load_image('paddle.png')
        self._score = 0
        self._surface = surface
        self._speed = 5
        self._pos = [xPos, surface.get_rect().height * 0.5]
        DebugLog("New Paddle Created")

    # Render the paddle
    #
    def render(self):
        self._surface.blit(self._image, self._pos)

    # Move the paddle up
    #
    def move_up(self):
        self._pos[1] = self._pos[1] - self._speed

    def move_down(self):
        self._pos[1] = self._pos[1] + self._speed

    # Get Paddle Score
    #
    def get_score(self):
        return self._score

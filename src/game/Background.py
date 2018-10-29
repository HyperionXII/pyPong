import pygame
from src.core.Vectors import Vector2

# Background rendering class
#
class Background(pygame.Surface):

    # Ctor.
    #
    def __init__(self, screen):
        self._screen = screen
        self._position = Vector2(0, 0)
        self._background = pygame.Surface(screen.get_size()).convert()
        self._background.fill((0, 0, 128))

    # Render the background
    #
    def Render(self):
        self._screen.blit(self._background, (0, 0))

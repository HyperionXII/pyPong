# 
# Collection of static functions for loading resources 
# 
import os
import pygame
from pygame.locals import *
from pygame.compat import geterror

dirName = os.path.dirname
__main_dir = os.path.join(dirName(dirName(dirName(__file__))))
__resourcePath = os.path.join(__main_dir, 'resources')
__imagesResourcePath = os.path.join(__resourcePath, 'images')
__soundResourcePath = os.path.join(__resourcePath, 'sounds')

#  Load an Image
# 
def load_image(name, colorkey=None):
    print(__main_dir)
    fullname = os.path.join(__imagesResourcePath, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

# Load a SFX
# 
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join(__soundResourcePath, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound:', name)
        raise SystemExit(message)
    return sound
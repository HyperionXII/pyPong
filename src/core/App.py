import pygame
from pygame.locals import *

from Debugging import *
from src.game.GameManager import *

# App Class
# 
class App:
    # Ctor
    # 
    def __init__(self):
        DebugLog("Creating new App...")
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.gameManager = GameManager()
        DebugLog("App init success")
    # Initialise the App
    # 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('pyPong')
        pygame.mouse.set_visible(0)
        self.gameManager = GameManager(self._display_surf)
        self._running = True
    # Handle Events passed from pyGame
    # 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    # App Update 
    # 
    def on_loop(self):
        self.gameManager.Update()
    # App Render 
    # 
    def on_render(self):
        self.gameManager.Render()
        pygame.display.flip()
    # Clean-up when the app is closing 
    # 
    def on_cleanup(self):
        DebugLog("Quitting...")
        pygame.quit()
    # Master App execution loop
    # 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
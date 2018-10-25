
import pygame

from Debugging import *
from src.game.Paddle import *
from src.core.GameObject import GameObject
from src.core.Vectors import Vector2

# Manager for the whole game 
# 
class GameManager(GameObject):
	# Ctor.
	# 
	def __init__(self, _screen):
		DebugLog("New GameManager Created")
		self.screen = _screen
		self.background = pygame.Surface(_screen.get_size())
   		# self.background = self.background.convert()
  		# self.background.fill((250, 250, 250))
    	# self.background.position = Vector2(0,0)
		self.paddle1 = Paddle()
	# 
	# 
	def Render(self, _screen):
		pass
		# self.screen.blit(self.background, self.background.position)

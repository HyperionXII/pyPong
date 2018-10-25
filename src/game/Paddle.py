import pygame

from Debugging import *
from src.core.GameObject import GameObject
from src.core.Vectors import *
from src.utils.ResourceUtils import *

# Paddle class
# 
class Paddle(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.image, self.rect = load_image('paddle.png')
		self.score = 0
		self.position = Vector2(1, 1)
		DebugLog("New Paddle Created")
	# Get Paddle Score 
	# 
	def GetScore(self):
		return self.score
	# Render the paddel
	# 
	def Render(self):
		pass
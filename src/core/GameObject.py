# Base class for all game objects
#
class GameObject:

	__renderLayer = 0

	def __init__(self):
		pass
	def Update(self):
		# update loop 
		pass
	def SetRenderLayer(self, layer):
		self.__renderLayer = layer
	def GetRenderLayer(self):
		return self.__renderLayer
	def Render(self):
		# render here
		pass
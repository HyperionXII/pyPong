# Vector 2 object
# 
class Vector2:
	def __init__(self):
		self.Set(0, 0)
	def __init__(self, _x, _y):
		self.Set(_x, _y)
	def Set(self, _x, _y):
		self.x = _x
		self.y = _y
# Vector with 3 elements
# 
class Vector3(Vector2):
	def __init__(self):
		Set(0, 0, 0)
	def __init__(self, _x, _y, _z):
		self.Set(_x, _y, _z)
	def Set(self, _x, _y, _z):
		self.Set(_x, _y)
		self.z = _z
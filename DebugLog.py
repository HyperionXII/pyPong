# 
# Debug Logger Class
# 

class DebugLog:

	# Ctor.
	# 
	def __init__(self):
		self.Log("Creating New DebugLog")

	# Log
	#
	def Log(self, msg):
		log = "DebugLog: " + msg
		print(log)

	# Log Warning 
	# 
	def LogWarning(self, msg):
		log = "WARNING - " + msg
		Log(log)

	# Log Error 
	# 
	def LogError(self, msg):
		log = "ERROR - " + msg
		Log(log)
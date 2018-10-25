# 
# Debugging Class
# 

# Log message
# 
def DebugLog(msg):
	log = "DebugLog: " + msg
	print(log)
# Log Warning 
# 
def DebugLogWarning(msg):
	log = "WARNING - " + msg
	DebugLog(log)
# Log Error 
# 
def DebugLogError(msg):
	log = "ERROR - " + msg
	DebugLog(log)
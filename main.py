#!flask/bin/python

from Debugging import *
from src.core.App import *
 
# Entry
# 
if __name__ == "__main__" :
	DebugLog("Hello, World!")

	theApp = App()
	theApp.on_execute()
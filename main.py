#!flask/bin/python

from src.core.App import *

VERSION = "0.1"
 
# Program entry
# 
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()

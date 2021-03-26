#!/usr/bin/python
import sys
import os

hsvRunDir = os.path.dirname(sys.argv[1])
print("Working Directory: " + hsvRunDir)
os.chdir(hsvRunDir)
print(os.listdir())




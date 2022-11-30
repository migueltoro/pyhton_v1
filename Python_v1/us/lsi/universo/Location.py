'''
Created on 30 nov 2022

@author: migueltoro
'''

from enum import Enum, auto

class Location(Enum):
    INSIDE=auto()
    LEFT=auto()
    RIGHT=auto()
    UP=auto()
    DOWN=auto()
    OUTSIDE=auto()
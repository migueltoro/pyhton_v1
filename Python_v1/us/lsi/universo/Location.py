# -*- coding: utf-8 -*-
'''
Created on 12 ago 2022

@author: mateosg
'''

from enum import Enum, auto

class Location(Enum):
    INSIDE=auto()
    LEFT=auto()
    RIGHT=auto()
    UP=auto()
    DOWN=auto()
    OUTSIDE=auto()
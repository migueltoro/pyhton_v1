'''
Created on 24 nov 2021

@author: migueltoro
'''

from us.lsi.tools.Iterable import str_iterable
import sys

if __name__ == '__main__':
    print(str_iterable(sys.path,sep='\n'))
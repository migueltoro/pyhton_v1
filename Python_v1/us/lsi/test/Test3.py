'''
Created on 24 nov 2021

@author: migueltoro
'''

from us.lsi.tools.Iterable import str_iterable
import sys
import calendar

d = {0:'a',1:'b',2:'c'}
print(list(d.values()))

if __name__ == '__main__':
    print(str_iterable(sys.path,sep='\n'))
    print(list(calendar.day_name))
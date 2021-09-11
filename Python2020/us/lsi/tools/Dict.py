'''
Created on 27 August. 2021

@author: migueltoro
'''

from typing import Dict, TypeVar


K = TypeVar('K')
V = TypeVar('V')
E = TypeVar('E')
R = TypeVar('R')

def str_dictionary(dictionary:Dict[K,V],sep:str='\n',prefix:str='',suffix:str='') ->str:
    ts = lambda x:'({}:{})'.format(str(x[0]),str(x[1]))
    return "{0}{1}{2}".format(prefix,sep.join(ts(x) for x in sorted(dictionary.items(),key=lambda x:x[0])),suffix)
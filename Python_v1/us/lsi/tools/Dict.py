'''
Created on 27 August. 2021

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Iterable
from us.lsi.tools.Iterable import flat,grouping_list, grouping_set


K = TypeVar('K')
V = TypeVar('V')
E = TypeVar('E')
R = TypeVar('R')


def invert_dict_list(d:dict[K,V | Iterable[V]]) -> dict[V,list[K]]:
    fl = ((k,nv)  for k,v in d.items()  for nv in flat(v))
    return grouping_list(fl,fkey=lambda e:e[1],fvalue=lambda e:e[0])

def invert_dict_set(d:dict[K,V | Iterable[V]]) -> dict[V,set[K]]:
    fl = ((k,nv)  for k,v in d.items()  for nv in flat(v))
    return grouping_set(fl,fkey=lambda e:e[1],fvalue=lambda e:e[0])

def str_dictionary(dictionary:dict[K,V],sep:str='\n',prefix:str='',suffix:str='')->str:
    ts = lambda x:'({}:{})'.format(str(x[0]),str(x[1]))
    return "{0}{1}{2}".format(prefix,sep.join(ts(x) for x in sorted(dictionary.items(),key=lambda x:x[0])),suffix)
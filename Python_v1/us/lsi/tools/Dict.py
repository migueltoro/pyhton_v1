'''
Created on 27 August. 2021

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Iterable, Callable
from us.lsi.tools.Iterable import flat,grouping_list, grouping_set


K = TypeVar('K')
V = TypeVar('V')
E = TypeVar('E')
R = TypeVar('R')


def invert_dict_list(d:dict[K,V | Iterable[V]]) -> dict[V,list[K]]:
    fl:Iterable[tuple[K,V]] = ((k,nv)  for k,v in d.items() for nv in flat(v))
    return grouping_list(fl,key=lambda e:e[1],value=lambda e:e[0])

def invert_dict_set(d:dict[K,V | Iterable[V]]) -> dict[V,set[K]]:
    fl = ((k,nv)  for k,v in d.items()  for nv in flat(v))
    return grouping_set(fl,key=lambda e:e[1],value=lambda e:e[0])

def strfdict(dictionary:dict[K,V],sep:str='\n',prefix:str='',suffix:str='',
                   key:Callable[[K],str]=str,value:Callable[[K],str]=str)->str:
    ts = lambda x:f'({key(x[0])}:{value(x[1])})'
    r:str = sep.join(ts(x) for x in dictionary.items())
    return f"{prefix}{r}{suffix}"


if __name__ == '__main__':
    pass
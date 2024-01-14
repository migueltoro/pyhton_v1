'''
Created on 27 August. 2021

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Iterable, Callable, overload
from us.lsi.tools.Iterable import flat,grouping_list, grouping_set


K = TypeVar('K')
V = TypeVar('V')
E = TypeVar('E')
R = TypeVar('R')
I = TypeVar('I',bound=Iterable)

@overload
def dict_map(d:dict[K,V],key:Callable[[K],E]) -> dict[E,V]: ... 

@overload  
def dict_map(d:dict[K,V],value:Callable[[V],R]) -> dict[K,R]: ...

@overload
def dict_map(d:dict[K,V],key:Callable[[K],E],value:Callable[[V],R]) -> dict[E,R]: ...

def dict_map(d,key=None,value=None) :
    if key is None:
        key = lambda x: x
    if value is None:
        value = lambda x: x
    return {key(k) : value(v) for k,v in d.items()}  

@overload
def dict_filter(d:dict[K,V],key:Callable[[K],bool]) -> dict[K,V]: ... 

@overload  
def dict_filter(d:dict[K,V],value:Callable[[V],bool]) -> dict[K,V]: ...

@overload
def dict_filter(d:dict[K,V],key:Callable[[K],bool],value:Callable[[V],bool]) -> dict[K,V]: ...

def dict_filter(d,key=None,value=None) :
    if key is None:
        key = lambda x: True
    if value is None:
        value = lambda x: True
    return {k:v for k,v in d.items() if key(k) and value(v)}  

def dict_invert_list(d:dict[K,V | Iterable[V]]) -> dict[V,list[K]]:
    fl:Iterable[tuple[K,V]] = ((k,nv)  for k,v in d.items() for nv in flat(v))
    return grouping_list(fl,key=lambda e:e[1],value=lambda e:e[0])

def dict_invert_set(d:dict[K,V | Iterable[V]]) -> dict[V,set[K]]:
    fl = ((k,nv)  for k,v in d.items()  for nv in flat(v))
    return grouping_set(fl,key=lambda e:e[1],value=lambda e:e[0])

def str_dict(dictionary:dict[K,V],sep:str='\n',prefix:str='',suffix:str='',
                   key:Callable[[K],str]=str,value:Callable[[V],str]=str)->str:
    ts = lambda x:f'({key(x[0])}:{value(x[1])})'
    r:str = sep.join(ts(x) for x in dictionary.items())
    return f"{prefix}{r}{suffix}"


if __name__ == '__main__':
    pass
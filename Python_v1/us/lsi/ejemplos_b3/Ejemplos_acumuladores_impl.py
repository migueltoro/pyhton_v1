'''
Created on 10 nov 2022

@author: migueltoro
'''

from typing import Iterable, Iterator,TypeVar, Callable, Optional, cast
from functools import reduce
from us.lsi.tools.Preconditions import check_state
from us.lsi.generic_types.Comparable import Comparable
import random
from statistics import mean

E = TypeVar('E')
R = TypeVar('R', bound=Comparable)
U = TypeVar('U',int,float)
S = TypeVar('S')

def sum2(iterable:Iterable[U],start:U=0)->U:
    s:U = start
    for x in iterable:
        s = s + x 
    return s

def media(iterable:Iterable[U])->float:
    s:U = 0
    n:int = 0
    for x in iterable:
        s = s + x 
        n = n+1
    return s/n

def reduce2(op:Callable[[R,E],R],iterable:Iterable[E],initial:Optional[R]=None)->Optional[R]:
    it:Iterator[E] = iter(iterable)
    r: R 
    if initial is None:
        try:
            e = next(it)
            r = cast(R,e)
        except StopIteration:
            check_state(False,'El iterable está vacío y no hay valor inicial')
    else:
        r = initial
    for e in it:
        r = op(r,e)
    return r


def min2(iterable:Iterable[E],key:Callable[[E],R])->E:
    it:Iterator[E] = iter(iterable)
    r:E
    try:
        r = next(it)
    except StopIteration:
        check_state(False,'El iterable está vacío')
    for e in it:
        if key(e) < key(r) :
            r = e  
    return r



if __name__ == '__main__':
    
    print(sum(range(2,30,5)))
    print(sum2(range(2,30,5)))
    print(mean(range(2,30,5)))
    print(media(range(2,30,5)))
    print(reduce(lambda x,y: x*y,range(2,30,5)))
    vl: Callable[[int],int]
    print(reduce2(lambda x,y: x*y,range(2,30,5)))
    ls:list[int] = []
    print(reduce(lambda x,y: x+[y],range(2,30,5),ls))
    print(reduce2(lambda x,y: x+[y],range(2,30,5),ls))
    ls = list(random.randint(100,1000) for _ in range(30))
    print(min(ls,key=lambda e:e))
    print(min2(ls,key=lambda e:e))
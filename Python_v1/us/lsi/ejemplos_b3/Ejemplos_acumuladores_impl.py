'''
Created on 10 nov 2022

@author: migueltoro
'''

from typing import Iterable, Iterator,TypeVar, Callable, Optional, Union, overload, Any
from functools import reduce
from us.lsi.tools.Types import Comparable
import random
from statistics import mean
from us.lsi.tools.File import lineas_de_csv
from us.lsi.tools.Iterable import flat_map
from fractions import Fraction

E = TypeVar('E')
R = TypeVar('R', bound=Comparable)
U = TypeVar('U',int,float)
S = TypeVar('S')
N = Union[int,float,Fraction,complex]

identity = lambda x:x

def sum2(iterable:Iterable[N],start:N=0)->N:
    s:N = start
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

def count_if(iterable:Iterable[E],predicate:Callable[[E],bool]=lambda _:True)->int:
    n = 0
    for e in iterable:
        if predicate(e):
            n = n+1
    return n

def sum_file(file:str)->int:  
    it0:Iterable[list[str]] =  lineas_de_csv(file) 
    it1:Iterable[str] = flat_map(it0,lambda x:x)
    it2:Iterable[int] = (int(e) for e in it1)
    return sum(it2)

@overload
def reduce2(op:Callable[[E,E],E],it:Iterable[E])->E: ...
 
@overload
def reduce2(op:Callable[[R,E],R],it:Iterable[E], ini:R)->R: ...

def reduce2(op:Callable[[Any,Any],Any], it:Iterable[Any], ini:Optional[Any]=None)->Any:
    r = ini
    for e in it:
        if r is None:
            r = e
        else:
            r = op(r,e)
    return r

def min2(iterable:Iterable[E],key:Callable[[E],R] = identity)->Optional[E]:
    it:Iterator[E] = iter(iterable)
    r:Optional[E] = None
    for e in it:
        if r is None:
            r = e
        elif key(e) < key(r):
            r = e  
    return r

def all2(iterable:Iterable[bool])->bool:
    r:bool = True
    for e in iterable:
        if not e:
            r = False
            break
    return r

def any2(iterable:Iterable[bool])->bool:
    r:bool = False
    for e in iterable:
        if e:
            r = True
            break
    return r

def sorted2(iterable:Iterable[E], key:Callable[[E],R]=identity,reverse:bool=False)->list[E]:
    ls = list(iterable)
    n = len(ls)
    for i in range(n):
        for j in range(n):
            if not reverse:
                if key(ls[i]) < key(ls[j]):
                    ls[i], ls[j] = ls[j], ls[i]
            else: 
                if key(ls[i]) > key(ls[j]):
                    ls[i], ls[j] = ls[j], ls[i]          
    return ls



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
    print(all((e%2==0 for e in range(2,341,5))))
    print(all2((e%2==0 for e in range(2,341,5))))
    print(any((e%13==0 for e in range(2,341,5))))
    print(any2((e%13==0 for e in range(2,341,5))))
    
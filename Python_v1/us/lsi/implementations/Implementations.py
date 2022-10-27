'''
Created on 23 oct 2022

@author: migueltoro
'''

from typing import Iterable, Iterator,TypeVar, Callable, Any, Optional

identity = lambda x:x

def arithmetic(a:int,b:int,c:int) -> Iterable[int]:
    n = a
    while n < b:
        yield n
        n = n+c

def zip2(*iterables:Iterable[Any])->Iterable[Any]:
    r = [iter(it) for it in iterables]
    n = len(r)
    try:
        while True:
            ls = []
            for i in range(n):
                e = next(r[i])
                ls.append(e)          
            yield tuple(ls)               
    except StopIteration:
        return

E = TypeVar('E')
R = TypeVar('R')   
U = TypeVar('U',int,float)
    
def average(iterable:Iterable[U])->float:
    s:U = 0
    n:int = 0
    for x in iterable:
        s = s + x 
        n = n+1
    return s/n

def reduce1(function:Callable[[E,E],E], iterable:Iterable[E],initializer:Optional[E]=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

def reduce2(iterable:Iterable[E],op:Callable[[R,R],R],value:Callable[[E],R]=identity, initial:Optional[R]=None)->R|None:
    it:Iterator[E] = iter(iterable)
    r: R
    if not initial:
        r = value(next(it))
    else:
        r = initial
    for e in it:
        r = op(r,value(e))
    return r
    


if __name__ == '__main__':
    pass
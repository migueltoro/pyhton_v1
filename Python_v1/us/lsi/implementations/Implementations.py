'''
Created on 23 oct 2022

@author: migueltoro
'''

from typing import Iterable, Any

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
    

    
if __name__ == '__main__':
    pass
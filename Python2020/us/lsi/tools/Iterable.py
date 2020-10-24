'''
Created on 15 jul. 2020

@author: migueltoro
'''
from typing import Iterator, Iterable, TypeVar, Dict, Callable, List, Set, Union, Optional
from us.lsi.tools.Functions import identity
# from optional import Optional

K = TypeVar('K')
V = TypeVar('V')
E = TypeVar('E')
R = TypeVar('R')


def str_iterable(iterable:Iterator[str],sep:str=',',prefix:str='{',suffix:str='}') -> str:
    return '{0}{1}{2}'.format(prefix,sep.join(x for x in iterable),suffix)

def size(iterable:Iterator[E]) -> int:
    n = 0
    for _ in iterable:
        n = n+1
    return n

def iterate(initial:E, predicate:Callable[[E],bool],operator:Callable[[E,E],E]) -> Iterator[E]:
    e = initial
    while predicate(e):
        yield e
        e = operator(e)

def average(iterable:Iterator[Union[int, float]]) -> float:
    s = 0
    n = 0
    for x in iterable:
        s = s + x 
        n = n+1
    return s/n

def find_first(iterable:Iterator[E], predicate:Callable[[E],bool]) -> Optional[E]:
    return next((x for x in iterable if predicate(x)), None)

def distinct(iterable:Iterator[E])->Iterator[E]:
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item 
            
def limit(iterable:Iterator[E],n:int) -> Iterator[E]:
    s = zip(iterable,range(n))
    return (x for x,_ in s)

def index(iterable:Iterator[bool],default:int=None):
    for i,e in enumerate(iterable):
        if e:
            return i
    return default
    
def flat_map(iterable:Iterator[E],fm:Callable[[E],Iterable[R]]=identity) -> Iterator[R]:
    return (y for x in iterable for y in fm(x))
    
def flat(e:Union[E,Iterable[E]]) -> Iterator[E]:
    if isinstance(e,Iterable):
        for x in e:
            yield x 
    else:
        yield e
    
def joining(iterable:Iterator[E],tostring:Callable[[E],str]=str,separator:str='\n',prefix:str='',suffix:str='') -> str:
        return '{0}{1}{2}'.format(prefix,separator.join(tostring(x) for x in  iterable),suffix)
  

def grouping(iterable:Iterator[E],fkey:Callable[[E],K],op:Callable[[V],E],a0:E=None) -> Dict[K, V]:
    a = {}
    for e in iterable:
        k = fkey(e)
        if not (a0 is None):
            a[k] = op(a.get(k,a0),e)
        elif k in a:
            a[k] = op(a[k],e)
        else:
            a[k] = e
    return a

def grouping_list(iterable:Iterator[E],fkey:Callable[[E],K],fvalue:Callable[[E],V]=identity) -> Dict[K,List[V]]:
    return grouping(iterable,fkey,lambda x,y:x+[fvalue(y)],a0=[])

def grouping_set(iterable:Iterator[E],fkey:Callable[[E],K],fvalue:Callable[[E],V]=identity) -> Dict[K,Set[V]]:
    return grouping(iterable,fkey,lambda x,y:x|{fvalue(y)},a0=set())

def counting(iterable:Iterator[E],fkey:Callable[[E],R]) -> Dict[K,int]:
    return grouping(iterable,fkey,lambda x,y:x+1,a0=0)    

if __name__ == '__main__':
    print(str_iterable(str(x) for x in range(0,100)))
    print(average(range(0,100)))
    print(str_iterable(str(x) for x in flat_map([[0,1],[2,3,4],[5,6],[9]])))
    
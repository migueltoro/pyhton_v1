'''
Created on 15 jul. 2020

@author: migueltoro
'''
from typing import Iterator, TypeVar, Dict, Callable, List, Set, Union
from us.lsi.tools.Functions import identity

K = TypeVar('K')
V = TypeVar('V')
E = TypeVar('E')
R = TypeVar('R')


def str_iterable(iterable:Iterator[E],ft:Callable[[E],str]=str,sep:str=',',pf:str='{',sf:str='}') -> str:
    return '{}{}{}'.format(pf,sep.join(ft(x) for x in iterable),sf)

def average(iterable:Iterator[Union[int, float]]) -> float:
        s = 0
        n = 0
        for x in iterable:
            s = s + x 
            n = n+1
        return s/n

def unique_values(iterable:Iterator[E])->Iterator[E]:
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item 
            
def limit(iterable:Iterator[E],n:int) -> Iterator[E]:
        s = zip(iterable,range(n))
        return (x for x,_ in s)
    
def flat_map(iterable:Iterator[E],ft:Callable[[E],R]=identity) -> Iterator[R]:
        return (y for x in iterable for y in ft(x))
    
def joining(iterable:Iterator[E],tostring:Callable[[E],str]=str,separator:str='\n',prefix:str='',suffix:str='') -> str:
        return '{0}{1}{2}'.format(prefix,separator.join(tostring(x) for x in  iterable),suffix)
  

def grouping(iterable:Iterator[E],f_key:Callable[[E],K],op:Callable[[V],E],a0:E=None) -> Dict[K, V]:
    a = {}
    for e in iterable:
        k = f_key(e)
        if not (a0 is None):
            a[k] = op(a.get(k,a0),e)
        elif k in a:
            a[k] = op(a[k],e)
        else:
            a[k] = e
    return a

def grouping_list(iterable:Iterator[E],fk:Callable[[E],K]) -> Dict[K,List[E]]:
    return grouping(iterable,fk,lambda x,y:x+[y],a0=[])

def grouping_set(iterable:Iterator[E],fk:Callable[[E],K]) -> Dict[K,Set[E]]:
    return grouping(iterable,fk,lambda x,y:x|{y},a0=set())

def counting(iterable:Iterator[E],fk:Callable[[E],R]) -> Dict[K,int]:
    return grouping(iterable,fk,lambda x,y:x+1,a0=0)    

if __name__ == '__main__':
    print(str_iterable(range(0,100)))
    print(average(range(0,100)))
    print(str_iterable(flat_map([[0,1],[2,3,4],[5,6],[9]])))
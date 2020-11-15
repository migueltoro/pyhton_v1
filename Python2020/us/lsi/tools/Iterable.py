'''
Created on 15 jul. 2020

@author: migueltoro
'''
from typing import Iterator, Iterable, TypeVar, Dict, Callable, List, Set, Union, Optional
from us.lsi.tools.Functions import identity
import random
from us.lsi.tools.File import lineas_de_fichero
# from optional import Optional

K = TypeVar('K')
V = TypeVar('V')
E = TypeVar('E')
R = TypeVar('R')


def arithmetic(a:int,b:int,c:int) -> Iterable[int]:
    n = a
    while n < b:
        yield n
        n = n+c
        
def geometric(a:int,b:int,c:int) -> Iterable[int]:
    n = a
    while n < b:
        yield n
        n = n*c

def aleatorios(a:int,b:int,n:int) -> Iterable[int]:
    for _ in range(n):
        yield random.randint(a,b)
                
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

def index_bool(iterable:Iterator[bool],default:int=-1)->int:
    for i,e in enumerate(iterable):
        if e:
            return i
    return default

def index(iterable:Iterator[E],predicate:Callable[[E],bool],default:int=-1)->int:
    for i,e in enumerate(iterable):
        if predicate(e):
            return i
    return default

def index_elem(iterable:Iterator[E],elem:E,default:int=-1)->int:
    for i,e in enumerate(iterable):
        if e == elem:
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
  
def str_iterable(iterable:Iterator[str],sep:str=',',prefix:str='{',suffix:str='}',ts:Callable[[E],str]=str) ->str:
    return "{0}{1}{2}".format(prefix,sep.join(ts(x) for x in iterable),suffix)

def str_dictionary(dictionary:Dict[K,V],sep:str='\n',prefix:str='',suffix:str='') ->str:
    ts = lambda x:'({}:{})'.format(str(x[0]),str(x[1]))
    return "{0}{1}{2}".format(prefix,sep.join(ts(x) for x in sorted(dictionary.items(),key=lambda x:x[0])),suffix)

def reduce(iterable:Iterator[E],op:Callable[[E,E],E])->E:
    it = (x for x in iterable)
    a = next(it)
    for e in it:
        a = op(a,e)
    return a

def accumulate(iterable:Iterator[E],op:Callable[[V,E],E],a0:V)->V:
    a = a0
    for e in iterable:
        a = op(a,e)
    return a

def grouping_reduce(iterable:Iterator[E],fkey:Callable[[E],K],op:Callable[[E,E],E]) -> Dict[K, E]:
    a = {}
    for e in iterable:
        k = fkey(e)
        if k in a:
            a[k] = op(a[k],e)
        else:
            a[k] = e
    return a

def grouping_acum(iterable:Iterator[E],fkey:Callable[[E],K],op:Callable[[V],E],a0:E=None) -> Dict[K, V]:
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
    return grouping_acum(iterable,fkey,lambda x,y:x+[fvalue(y)],a0=[])

def grouping_set(iterable:Iterator[E],fkey:Callable[[E],K],fvalue:Callable[[E],V]=identity) -> Dict[K,Set[V]]:
    return grouping_acum(iterable,fkey,lambda x,y:x|{fvalue(y)},a0=set())    

def counting(iterable:Iterator[E],fkey:Callable[[E],K],fsum:Callable[[E],int]=lambda e:1) -> Dict[K,int]:
    return grouping_acum(iterable,fkey,lambda x,y:x+fsum(y),a0=0) 

if __name__ == '__main__':
    print(str_iterable(range(0,100)))
    print(average(range(0,100)))
    print(str_iterable(flat_map([[0,1],[2,3,4],[5,6],[9]])))
    print(str_iterable(geometric(2,100,5)))
    print(index_bool((x%29==0 for x in aleatorios(10,1000,50))))
    print(str_iterable(lineas_de_fichero('../../../resources/datos.txt')))
    print(index((int(e) for e in lineas_de_fichero('../../../resources/datos.txt')),lambda x: x==7))
    
    
    
    
          
    
    
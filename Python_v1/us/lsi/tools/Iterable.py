'''
Created on 15 jul. 2020

@author: migueltoro
'''
from typing import Iterable, TypeVar, Callable, Any
import random
from us.lsi.tools.File import lineas_de_fichero
from us.lsi.tipos.IntPar import IntPar
from collections import Counter

identity = lambda x:x

num = int | float

K = TypeVar('K')
V = TypeVar('V')
E = TypeVar('E')
R = TypeVar('R')


def zip2(*iterables:Iterable[Iterable[Any]])->Iterable[Any]:
    iterables = [iter(it) for it in iterables]
    n = len(iterables)
    try:
        while True:
            ls = []
            for i in range(n):
                e = next(iterables[i])
                ls.append(e)          
            yield tuple(ls)               
    except StopIteration:
        return

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

def iterate(initial:E, operator:Callable[[E],E], predicate:Callable[[E],bool]=lambda x:True) -> Iterable[E]:
    e = initial
    while predicate(e):
        yield e
        e = operator(e)
        
def all_pairs(n:int,m:int,n0:int = 0, m0:int= 0)-> Iterable[IntPar]:
    for i in range(n0,n):
        for j in range(m0,m):
            yield IntPar.of(i,j)

def average(iterable:Iterable[num]):
    s = 0
    n = 0
    for x in iterable:
        s = s + x 
        n = n+1
    return s/n

def first(iterable:Iterable[E], p:Callable[[E],bool]=lambda x:True) -> E | None:
    for e in iterable:
        if p(e):
            return e
    return None
    
def first_and_last(iterable:Iterable[E],defaultvalue=None)->tuple[E,E]:
    first = last = next(iterable, defaultvalue)
    for last in iterable:
        pass
    return (first,last)
    

def distinct(iterable:Iterable[E])->Iterable[E]:
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item 
            
def limit(iterable:Iterable[E],limit:int) -> Iterable[E]:
    i = 0
    for e in iterable:
        if i < limit:
            yield e
            i = i +1
        else:
            break
        
def count(iterable:Iterable[E],predicate:Callable[[E],bool]=lambda _:True)->int:
    n = 0
    for e in iterable:
        if predicate(e):
            n = n+1
    return n

def reduce2(f:Callable[[R,E],R], iterable:Iterable[E], initial:R=None)->R|None:
    r = initial
    if initial is None:
        iterable = iter(iterable)
        r = next(iterable)
    for e in iterable:
        r = f(r,e)
    return r
    

def index_bool(iterable:Iterable[bool],default:int=-1)->int:
    for i,e in enumerate(iterable):
        if e:
            return i
    return default

def index_predicate(iterable:Iterable[E],predicate:Callable[[E],bool],default:int=-1)->int:
    for i,e in enumerate(iterable):
        if predicate(e):
            return i
    return default

def index_elem(iterable:Iterable[E],elem:E,default:int=-1)->int:
    for i,e in enumerate(iterable):
        if e == elem:
            return i
    return default
    
def flat_map(iterable:Iterable[E],fm:Callable[[E],Iterable[R]]=identity) -> Iterable[R]:
    for e in iterable:
        for pe in fm(e):
            yield pe
            
def enumerate_flat_map(iterable:Iterable[enumerate[E]],fm:Callable[[E],Iterable[R]]=identity) -> Iterable[enumerate[R]]:
    for e in iterable:
        for pe in fm(e.item):
            yield enumerate(e.count,pe)
    
def flat(e: E | Iterable[E]) -> Iterable[E]:
    if isinstance(e,Iterable):
        for x in e:
            yield x 
    else:
        yield e
        
    
def joining(iterable:Iterable[E],tostring:Callable[[E],str]=str,separator:str='\n',prefix:str='',suffix:str='') -> str:
        return '{0}{1}{2}'.format(prefix,separator.join(tostring(x) for x in  iterable),suffix)
  
def str_iterable(iterable:Iterable[str],sep:str=',',prefix:str='{',suffix:str='}',ts:Callable[[E],str]=str) ->str:
    return "{0}{1}{2}".format(prefix,sep.join(ts(x) for x in iterable),suffix)


def grouping_reduce(iterable:Iterable[E],fkey:Callable[[E],K], \
                    op:Callable[[V,V],V],fvalue:Callable[[E],V]= identity) -> dict[K, E]:
    a = {}
    for e in iterable:
        k = fkey(e)
        if k in a:
            a[k] = op(a[k],fvalue(e))
        else:
            a[k] = fvalue(e)
    return a


def grouping_list(iterable:Iterable[E],fkey:Callable[[E],K],fvalue:Callable[[E],V]=identity) -> dict[K,list[V]]:
    return grouping_reduce(iterable,fkey,lambda x,y:x+y,lambda x: [fvalue(x)])

def grouping_set(iterable:Iterable[E],fkey:Callable[[E],K],fvalue:Callable[[E],V]=identity) -> dict[K,set[V]]:
    return grouping_reduce(iterable,fkey,lambda x,y:x|y,lambda x: {fvalue(x)}) 

# similar a Counter
def groups_size(iterable:Iterable[E],fkey:Callable[[E],K]=identity,fsum:Callable[[E],int]=lambda e:1) -> dict[K,int]:
    return grouping_reduce(iterable,fkey,op=lambda x,y:x+y,fvalue= fsum)

if __name__ == '__main__':
    print(str_iterable(range(0,100)))
    print(average(range(0,100)))
    print(str_iterable(flat_map([[0,1],[2,3,4],[5,6],[9]])))
    print(str_iterable(geometric(2,100,5)))
    print(index_bool((x%29==0 for x in aleatorios(10,1000,50))))
    print(str_iterable(lineas_de_fichero('../../../resources/datos.txt')))
    print(index_predicate((int(e) for e in lineas_de_fichero('../../../resources/datos.txt')),lambda x: x==7))
    print(first_and_last(arithmetic(3,500,29)))
    print(list(zip2([1,2,3,5],[6,7,8,9,10],[11,12,13,14,15]))) 
    g = grouping_reduce(range(0,10,2),fkey = lambda x: x%3,op=lambda x,y:x+y)
    print(g[0])   
    cp = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
    print(cp.most_common(1)[0][1])
    r = ((1, 2, 3, 4)*2)[-2:-1]
    print(r)   
    print(','.join(str(p) for p in all_pairs(3,4)))
    
    
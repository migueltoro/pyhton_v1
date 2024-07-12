'''
Created on 15 jul. 2020

@author: migueltoro
'''
from typing import Iterable, Iterator, TypeVar, Callable, Optional, overload
import random
from us.lsi.tools.File import lineas_de_fichero
from collections import Counter
from us.lsi.tools.Optional import optional_get
from itertools import product

K = TypeVar('K')
V = TypeVar('V')
E = TypeVar('E')
R = TypeVar('R')

identity = lambda x:x

def aleatorios(n:int,a:int,b:int) -> Iterable[int]:
    assert a < b, f"en aleatorios: {a} debe ser menor que {b}"
    for _ in range(n):
        yield random.randint(a,b)

def iterate(initial:E, operator:Callable[[E],E], predicate:Callable[[E],bool]=lambda _:True) -> Iterable[E]:
    e = initial
    while predicate(e):
        yield e
        e = operator(e)
        
def all_pairs(n:int,m:int,n0:int = 0, m0:int= 0)-> Iterable[tuple[int,int]]:
    for i in range(n0,n):
        for j in range(m0,m):
            yield (i,j)   

def distinct(iterable:Iterable[E])->Iterable[E]:
    seen:set[E] = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item 
            
def all_different(iterable:Iterable[E])->bool:
    st:set[E] = set()
    n:int = 0
    for item in iterable:
        n = n+1
        st.add(item)
    return len(st) == n
            
def limit(iterable:Iterable[E],limit:int) -> Iterable[E]:
    i = 0
    for e in iterable:
        if i < limit:
            yield e
            i = i +1
        else:
            break
        
def count_if(iterable:Iterable[E],predicate:Callable[[E],bool]=lambda _:True)->int:
    n = 0
    for e in iterable:
        if predicate(e):
            n = n+1
    return n

def first(iterable:Iterable[E], p:Callable[[E],bool]=lambda _:True) -> Optional[E]:
    r:Optional[E] = None
    for e in iterable:
        if p(e):
            r = e
            break
    return r

def first_and_rest(iterable:Iterable[E]) -> Optional[tuple[E,Iterable[E]]]:
    it:Iterator[E] = iter(iterable)
    e:Optional[E] = next(it,None)
    if e is None:
        return None
    else:
        return (e,it)
    
def first_and_last(iterable:Iterable[E])->Optional[tuple[E,E]]:
    it = iter(iterable)
    first =  next(it, None)
    if first is None:
        return None
    else:
        last = first
        for last in it:
            pass
    return (first,last)

def first_index_true(iterable:Iterable[bool],default:int=-1)->int:
    for i,e in enumerate(iterable):
        if e:
            return i
    return default

def first_index_if(iterable:Iterable[E],predicate:Callable[[E],bool],default:int=-1)->int:
    for i,e in enumerate(iterable):
        if predicate(e):
            return i
    return default

def first_index_with_elem(iterable:Iterable[E],elem:E,default:int=-1)->int:
    for i,e in enumerate(iterable):
        if e == elem:
            return i
    return default

@overload
def flat_map(iterable:Iterable[Iterable[E]]) -> Iterable[E]: ...

@overload   
def flat_map(iterable:Iterable[E],key:Callable[[E],Iterable[R]]) -> Iterable[R]: ...
    
def flat_map(iterable:Iterable[E],key:Optional[Callable[[E],Iterable[R]]]=None) -> Iterable[R]:
    if key is None:
            key = identity
    for e in iterable:
        for pe in key(e):
            yield pe
            
@overload
def flat_map_enumerate(iterable:enumerate[Iterable[E]]) -> Iterable[tuple[int,E]]: ...

@overload   
def flat_map_enumerate(iterable:enumerate[E],key:Callable[[E],Iterable[R]]) -> Iterable[tuple[int,R]]: ...
            
def flat_map_enumerate(iterable:enumerate[E],key:Optional[Callable[[E],Iterable[R]]]=None) -> Iterable[tuple[int,R]]:
    if key is None:
        key = identity
    for ln,lv in iterable:    
        for r in key(lv):
            yield (ln,r)
    
def flat(e: E | Iterable[E]) -> Iterable[E]:
    if isinstance(e,Iterable):
        for x in e:
            yield x 
    else:
        yield e
  
def str_iter(iterable:Iterable[E],sep:str=',',prefix:str='{',suffix:str='}',
             key:Callable[[E],str]=str)->str:
    r:str = sep.join(key(x) for x in iterable)
    return f"{prefix}{r}{suffix}"

@overload
def grouping_reduce(iterable:Iterable[E],key:Callable[[E],K],op:Callable[[V,V],V],value:Callable[[E],V]=identity) -> dict[K,V]: ...
@overload
def grouping_reduce(iterable:Iterable[E],key:Callable[[E],K],op:Callable[[V,V],V],value:Callable[[E],V]=identity,andThen:Optional[Callable[[V],R]]=None) -> dict[K,R]: ...

def grouping_reduce(iterable:Iterable[E],key:Callable[[E],K], 
                    op:Callable[[V,V],V],
                    value:Callable[[E],V]=identity,
                    andThen:Optional[Callable[[V],R]]=None):
    r0:dict[K,V] = {}
    for e in iterable:
        k = key(e)
        if k in r0:
            r0[k] = op(r0[k],value(e))
        else:
            r0[k] = value(e)
    if andThen is None:
        return r0
    else:
        r1:dict[K,R] = {k:andThen(r0[k]) for k in r0.keys()}
        return r1
    
@overload
def grouping_list(iterable:Iterable[E],key:Callable[[E],K],value:Callable[[E],V]=identity) -> dict[K,list[V]]: ...

@overload
def grouping_list(iterable:Iterable[E],key:Callable[[E],K],value:Callable[[E],V]=identity,andThen:Optional[Callable[[list[V]],R]]=None) -> dict[K,R]: ...
    
def grouping_list(iterable:Iterable[E], key:Callable[[E],K], value:Callable[[E],V]=identity, andThen:Optional[Callable[[list[V]],R]]=None)  :
    return grouping_reduce(iterable,key,op=lambda x,y:x+y,value=lambda x:[value(x)],andThen=andThen)

@overload
def grouping_set(iterable:Iterable[E],key:Callable[[E],K],value:Callable[[E],V]=identity) -> dict[K,set[V]]: ...

@overload
def grouping_set(iterable:Iterable[E],key:Callable[[E],K],value:Callable[[E],V]=identity,andThen:Optional[Callable[[set[V]],R]]=None) -> dict[K,R]: ...

def grouping_set(iterable:Iterable[E],key:Callable[[E],K],value:Callable[[E],V]=identity,andThen:Optional[Callable[[set[V]],R]]=None) :
    r0:dict[K,set[V]]= grouping_reduce(iterable,key,lambda x,y:x|y,lambda x:{value(x)})
    return {k:andThen(r0[k]) for k in r0.keys()} if andThen else r0

# similar a Counter
def groups_size(iterable:Iterable[E],key:Callable[[E],K]=identity,value:Callable[[E],int]=lambda _:1) -> dict[K,int]:
    return grouping_reduce(iterable,key,op=lambda x,y:x+y,value=value)

def join(s1:Iterable[E],s2:Iterable[R],key1:Callable[[E],K],key2:Callable[[R],K])->Iterable[tuple[E,R]]:
    m1:dict[K,list[E]] = grouping_list(s1,key1)
    m2:dict[K,list[R]] = grouping_list(s2,key2)
    common_keys:set[K] = m1.keys() & m2.keys()
    return flat_map(common_keys,lambda k:product(m1[k],m2[k])) 

def test1():
    print(str_iter(range(0,100)))
    r: Iterable[int] = flat_map([[0,1],[2,3,4],[5,6],[9]],lambda x:x)
    print(str_iter(r))
    print(str_iter(range(2,100,5)))
    
def test2():
    print(str_iter(lineas_de_fichero('../../../datos/datos.txt')))
    print(first_index_if((int(e) for e in lineas_de_fichero('../../../datos/datos.txt')),lambda x: x==7))
    print(first_and_last(range(3,500,29)))
    print(list(zip([1,2,3,5],[6,7,8,9,10],[11,12,13,14,15]))) 
    print(list(aleatorios(10,50,1000)))
    print(first_index_true((x%29==0 for x in aleatorios(10,50,1000))))
    
def test3():
    sm:Callable[[int,int],int] = lambda x,y:x+y
    g = grouping_reduce(range(0,10,2),key = lambda x: x%3,op=sm, value= lambda x:x)
    print(g[0])
    
def test4(): 
    cp = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
    print(cp.most_common(1)[0][1])
    r = ((1, 2, 3, 4)*2)[-2:-1]
    print(r)   
    
def test5():
    print(','.join(str(p) for p in all_pairs(3,4)))
    print(len(range(10,3000,7)))
    
def test6():
    e,it = optional_get(first_and_rest(range(10,3000,7)))
    print(e)
    print(list(it))
    
def test7():
    it2:Iterable[int] = (x for x in range(10,3000,7))
    e = optional_get(first(it2))
    print(f"first = {e}, iterable = {list(it2)}")
    
def test8():
    it4:Iterable[int] = (x for x in range(10,3000,7))
    e2:tuple[int,Iterable[int]] = optional_get(first_and_rest(it4))
    print(f"first = {e2[0]}, rest = {list(e2[1])}")
    print(first_and_last((x for x in range(10,3000,7))))
    
def test9():
    it5:list[int] = [x for x in range(10,50,7)]
    print(it5)
    print(list(join(it5,it5,lambda x:x%2,lambda x:x%3)))
    
def test10():
    it5:list[int] = [x for x in range(10,30,7)]
    print(grouping_list(it5,lambda x:x%2))

if __name__ == '__main__':
    test2() 
    
    
    
    
    
    
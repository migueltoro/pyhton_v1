'''
Created on 23 dic 2023

@author: migueltoro
'''

from typing import Iterable, TypeVar, Callable, Optional, Any, overload, Union, TypeVarTuple, Unpack
from functools import reduce
from us.lsi.tools.Types import Comparable, FieldElement, Sum
from statistics import mean, StatisticsError
from fractions import Fraction

identity = lambda x:x

E = TypeVar('E')
R = TypeVar('R')
S = TypeVar('S')
T = TypeVar('T')
T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')
T4 = TypeVar('T4')
Ts1 = TypeVarTuple('Ts1')
Ts2 = TypeVarTuple('Ts2')
C = TypeVar('C', bound=Comparable)
F = TypeVar('F', bound=FieldElement)
A = TypeVar('A',bound=Sum)
N = Union[int,float,Fraction,complex]

@overload
def sum2(it:Iterable[N])->N:...

@overload
def sum2(it:Iterable[A],start:A)->A: ...

def sum2(it:Iterable[A],start=0)->A:
    return sum(it,start)

def any2(it:Iterable[bool])->bool:
    return any(it)

def all2(it:Iterable[bool])->bool:
    return any(it)

@overload
def min2(iterable:Iterable[C])->Optional[C]: ...

@overload    
def min2(iterable:Iterable[E],key:Optional[Callable[[E],C]])->Optional[E]: ...

def min2(iterable:Iterable[Any],key:Optional[Callable[[Any],C]]=None): 
    try:
        return min(iterable,key=key) 
    except Exception:
        return None

@overload
def max2(iterable:Iterable[C])->Optional[C]: ...

@overload    
def max2(iterable:Iterable[E],key:Optional[Callable[[E],C]])->Optional[E]: ...

def max2(iterable:Iterable[Any],key:Optional[Callable[[Any],C]]=None):
    try:
        return max(iterable,key=key) 
    except Exception:
        return None

@overload   
def sorted2(it:Iterable[C],r:bool=False)->list[C]: ...

@overload
def sorted2(it:Iterable[E],r:bool=False,k:Optional[Callable[[E],C]]=None,)->list[E]: ...
    
def sorted2(it:Iterable[Any],r:bool=False,k:Optional[Callable[[Any],Any]]=None,)->list[Any]:
    if k is None:
        return sorted(it,reverse=r)
    else:
        return sorted(it,key=k,reverse=r)
        
def map2(f:Callable[[E],R],it:Iterable[E])->Iterable[R]:
    return map(f,it)


def filter2(p:Callable[[E],bool],it:Iterable[E])->Iterable[E]:
    return filter(p,it)

def enumerate2(it:Iterable[E],start:int=0)->Iterable[tuple[int,E]]:
    return enumerate(it,start=start)

@overload
def zip2(it1:Iterable[T1],it2:Iterable[T2])->Iterable[tuple[T1,T2]]: ...

@overload
def zip2(it1:Iterable[T1],it2:Iterable[T2],it3:Iterable[T3])->Iterable[tuple[T1,T2,T3]]: ...

@overload
def zip2(it1:Iterable[T1],it2:Iterable[T2],it3:Iterable[T3],it4:Iterable[T4])->Iterable[tuple[T1,T2,T3,T4]]: ...

@overload
def zip2(it1:Iterable[T1],it2:Iterable[T2],it3:Iterable[T3],it4:Iterable[T4],*it5:tuple[Unpack[Ts1]])->Iterable[tuple[T1,T2,T3,T4,Unpack[Ts2]]]: ...

def zip2(*it):
    return zip(it)

@overload
def unzip(it:Iterable[tuple[E,R]])->tuple[Iterable[E],Iterable[R]]: ...

@overload
def unzip(it:Iterable[tuple[E,R,S]])->tuple[Iterable[E],Iterable[R],Iterable[S]]: ...

@overload
def unzip(it:Iterable[tuple[E,R,S,T,Unpack[Ts1]]])->tuple[Iterable[E],Iterable[R],Iterable[S],Iterable[T],Unpack[Ts2]]: ...

def unzip(it:Iterable[tuple[Unpack[Ts1]]])->tuple:
    return tuple(x for x in zip(*it))

@overload
def mean2(it:Iterable[int])->Optional[float]: ...

@overload
def mean2(it:Iterable[float])->Optional[float]: ...

@overload
def mean2(it:Iterable[Fraction])->Optional[Fraction]: ...

def mean2(it:Iterable[Any])->Optional[Any]: 
    try:
        return mean(it)
    except StatisticsError:
        return None

#Versión de mean que incluye los números complejos
   
def mean3(it:Iterable[F])->Optional[F]:
    n:int=0
    s:Optional[F]=None
    for e in it:
        if s is None:
            s = e            
        else:
            s = s+e
        n=n+1
    if s is None:
        return None
    else:
        return s/n
    
@overload
def reduce2(f:Callable[[E,E],E],it:Iterable[E])->Optional[E]: ...
 
@overload
def reduce2(f:Callable[[R,E],R],it:Iterable[E],ini:R)->R: ...
     
def reduce2(f:Callable[[Any,Any],Any], it:Iterable[Any],ini:Optional[Any]=None)->Any:
    if ini is None:
        try:
            return reduce(f,it)
        except Exception:
            return None  
    else:
        return reduce(f,it,ini)
    

if __name__ == '__main__':
    from fractions import Fraction as FF
    print(sum2((FF(3, 7), FF(1, 21), FF(5, 3), FF(1, 3))))
    ls:list[Fraction] = []
    print(sum2(([FF(3, 7), FF(1, 21)], [FF(5, 3), FF(1, 3)], [FF(5, 3), FF(1, 3)]),ls))
    print(mean2((FF(3, 7), FF(1, 21), FF(5, 3), FF(1, 3))))
    print(mean2((1,2,3,4)))
    print(mean2((1.,2.,3.,4.)))
    print(mean3((complex(3, 7), complex(1, 21), complex(5, 3), complex(1, 3))))
    emt:list[int] = []
    print(reduce2(f=lambda x,y:x+[y],it=(1,2,3,4),ini=emt))
    print(min2((FF(3, 7), FF(1, 21), FF(5, 3), FF(1, 3))))
    print(min2(()))
    print(reduce2(lambda x,y:x+y,(FF(3, 7), FF(1, 21), FF(5, 3), FF(1, 3))))
    print(reduce2(lambda x,y:x+y,emt))
    pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    numbers, letters = zip(*pairs)
    print(numbers)
    print(letters)
    
    name=['Manjeet','Nikhil','Shambhavi','Astha']
    roll_no = [ 4, 1, 3, 2 ]
    marks = [ 40, 50, 60, 70 ]

    # using zip() to map values
    mapped = list(zip(name, roll_no, marks))

    # converting values to print as list
#    mapped2 = 

    # printing resultant values
    print ('The zipped result is : ',end='')
    print (mapped)

    print('\n')

    # unzipping values
    namz, roll_noz, marksz = zip(*mapped)

    print ('The unzipped result: \n',end='')

    # printing initial lists
    print ('The name list is : ',end='')
    print (namz)

    print ('The roll_no list is : ',end='')
    print (roll_noz)

    print ('The marks list is : ',end='')
    print (marksz)
    
    full_name_list = [('Joe', 'Schmoe', 23),
                  ('Earnst', 'Ehlmann', 65),
                  ('Thomas', 'Fischer', 11),
                  ('Martin', 'Walter', 36),
                  ('Charles', 'Rogan', 83)]
    
    full_name_list_2 = [('Joe', 'Schmoe'),
                  ('Earnst', 'Ehlmann'),
                  ('Thomas', 'Fischer'),
                  ('Martin', 'Walter'),
                  ('Charles', 'Rogan')]
    
    full_name_list_3 = [('Joe', 'Schmoe', 23, 56),
                  ('Earnst', 'Ehlmann', 65, 67),
                  ('Thomas', 'Fischer', 11, -1),
                  ('Martin', 'Walter', 36, 10),
                  ('Charles', 'Rogan', 83, 45)]

    first_name, last_name, age = list(zip(*full_name_list))
    print(f"first name: {first_name}\nlast name: {last_name} \nage: {age}")
    
    for x in zip(*full_name_list):
        print(x)
        
    print(unzip(full_name_list))
    print(unzip(full_name_list_2))
    print(unzip(full_name_list_3))
    print(type(unzip(full_name_list)[0][0]))
    print(FF(3, 7)+0)
    print(complex(3, 7)*1)
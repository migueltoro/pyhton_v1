'''
Created on 22 sept 2022

@author: migueltoro
'''
from functools import reduce
from typing import Iterable, TypeVar
from us.lsi.tools.Iterable import count_if, first_index_if, distinct, first
from fractions import Fraction
from statistics import mean

E = TypeVar('E')

dias = ["lunes", "martes", "miercoles", "jueves","viernes", "sabado", "domingo"]

texto = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"

square = {2: 4, -3: 9, -1: 1, -2: 4}

key2 = max(square, key = lambda k: square[k])

def tolist(iterable:Iterable[E])->list[E]:
    ls= []
    for e in iterable:
        ls.append(e)
    return ls

def toset(iterable:Iterable[E])->set[E]:
    st : set[E]= set()
    for e in iterable:
        st.add(e)
    return st

def test1():
    print(sum((Fraction(51, 5), Fraction(25, 2), Fraction(59, 5))))
    print(mean((2, 3, 4, 2, 3, 6, 4, 2)))
    print(sorted(dias, key=len))
    print(reduce(lambda x,y: x*y,range(2,30,5)))
    
def test2():
    es:set[str] = set()
    print(reduce(lambda s,e: s | {e}, texto, es))
    print(max(dias,key=lambda x:len(x)))
    print(any((e%13==0 for e in range(2,341,5))))
    print(all((e%2==0 for e in range(2,341,5))))
    print(first(e for e in range(2,341,5) if e%13==0))
    
def test3():
    print("Apariciones de la letra a:", count_if(texto,lambda e:e=="a"))
    print("Primera aparicion de la letra a:",first_index_if(texto,lambda e:e=="a"))
    print(count_if(distinct(texto)))
    

if __name__ == '__main__':
    test3()
    

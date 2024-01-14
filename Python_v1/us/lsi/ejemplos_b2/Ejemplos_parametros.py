'''
Created on 18 sept 2022

@author: migueltoro
'''

from typing import Callable, TypeVar, Any, TypeVarTuple, Unpack
import math
from pip._vendor.typing_extensions import Unpack

E = TypeVar('E')
R = TypeVar('R')
Ts = TypeVarTuple('Ts')

def imprime_linea(rp:int=40, cadena:str="-=")->None:
    linea = cadena * rp
    print(linea)

multiplica_por_dos: Callable[[int],int] = lambda n: 2 * n

def transforma(ls:list[E],t: Callable[[E],R])->list[R]:
    lt = []
    for elemento in ls:
        lt.append(t(elemento))
    return lt

def filtra(ls:list[E],f:Callable[[E],bool] = lambda x: True)->list[E]:
    lf = []
    for elemento in ls:
        if f(elemento):
            lf.append(elemento)
    return lf

def f(fn:Callable[[Unpack[Ts]],R],*p:Unpack[Ts])->R:
    return fn(*p)

def test1():
    imprime_linea()
    imprime_linea(20) 
    imprime_linea(20, ":)")
    imprime_linea(20, cadena= ")")
    
def test2():
    print(multiplica_por_dos(45))
    
def test3():
    ls:list[int] = [1, 2, 3, 4, 5]
    print(transforma(ls, t = math.sqrt))
    print(transforma(ls, t = math.sin))
    print(transforma(ls, lambda y: y*y))
    print(filtra(ls,lambda x:x%2==0))
    print(filtra(ls))
    print(filtra(ls,f=lambda x:x%2==0)) 
    
def test4():
    ls:list[int] = [1, 2, 3, 4, 5]
    print(f(filtra,ls,lambda x:x%2==0))
    print(*ls,sep=';') 
    

if __name__ == '__main__':
    test4()

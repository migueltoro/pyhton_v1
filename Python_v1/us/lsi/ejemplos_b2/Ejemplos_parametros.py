'''
Created on 18 sept 2022

@author: migueltoro
'''

from typing import Callable, TypeVar
import math

E = TypeVar('E')
R = TypeVar('R')


def imprime_linea(rp:int, cadena:str="-=")->None:
    linea = cadena * rp
    print(linea)
    


multiplica_por_dos: Callable[[int],int] = lambda n: 2 * n

def transforma(ls:list[E],t: Callable[[E],R])->list[R]:
    lt:list[R] = []
    for elemento in ls:
        lt.append(t(elemento))
    return lt

def filtra(ls:list[E],f:Callable[[E],bool] = lambda x: True)->list[E]:
    lf:list[E] = []
    for elemento in ls:
        if f(elemento):
            lf.append(elemento)
    return lf

def test1():
    imprime_linea(30)
    imprime_linea(20) 
    imprime_linea(20, ":)")
    imprime_linea(20, cadena= ")")
    
def test2():
    print(multiplica_por_dos(45))
    
def test3():
    ls:list[int] = [1, 2, 3, 4, 5]
    ls2:list[float] = transforma(ls, t = math.sqrt)
    print(ls2)
    print(transforma(ls, t = math.sin))
    ls3:list[int] = transforma(ls, t = lambda n:n*n)
    print(ls3)
    print(transforma(ls, lambda y: y*y))
    print(filtra(ls,lambda x:x > 3))
    print(filtra(ls))
    print(filtra(ls,f=lambda x:x%2==0)) 
    
    

if __name__ == '__main__':
    test3()

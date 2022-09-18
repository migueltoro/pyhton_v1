'''
Created on 18 sept 2022

@author: migueltoro
'''

from typing import Callable, TypeVar
import math

E = TypeVar('E')
R = TypeVar('R')

multiplica_por_dos: Callable[[int],int] = lambda n: 2 * n

def transforma(ls:list[E],t: Callable[[E],R])->list[R]:
    lt = []
    for elemento in ls:
        lt.append(t(elemento))
    return lt

def filtra(ls:list[E],f:Callable[[E],bool])->list[E]:
    lf = []
    for elemento in ls:
        if f(elemento):
            lf.append(elemento)
    return lf



if __name__ == '__main__':
    print(multiplica_por_dos(45))
    ls:list[int] = [1, 2, 3, 4, 5]
    print(transforma(ls, math.sqrt))
    print(transforma(ls, math.sin))
    print(transforma(ls, lambda y: y*y))
    print(filtra(ls,lambda x:x%2==0))

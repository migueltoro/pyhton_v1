'''
Created on 26 oct 2022

@author: belen
'''
from __future__ import annotations

from fractions import Fraction
from us.lsi.matriz.Matriz import Matriz
from typing import Callable, Iterable
from us.lsi.tools.Iterable import all_pairs
from us.lsi.tools import Preconditions
from us.lsi.tools.File import absolute_path


class Matriz_of_fraction(Matriz[Fraction]):
    #===========================================================================
    # MÉTODOS DE FACTORÍA
    #===========================================================================
        
    @staticmethod
    def of(datos:list[list[Fraction]])->Matriz_of_fraction:
        return Matriz_of_fraction(datos)
    
    @staticmethod
    def of_file_fraction(file:str)->Matriz_of_fraction:
        return Matriz_of_fraction.of(Matriz.of_file(file, lambda x: Fraction(x)).datos)

    #===========================================================================
    # PROPIEDADES DERIVADAS
    #===========================================================================
    @property
    def es_antisimetrica(self)->bool:
        indices:Iterable[tuple[int,int]] = (p for p in all_pairs(self.nf,self.nc) if p[0] >= p[1])
        return all(self.get(par[0],par[1]) == -self.get(par[0],par[1]) for par in indices)
    
    #===========================================================================
    # OTROS MÉTODOS
    #===========================================================================
    def __add__(self,other:Matriz_of_fraction)->Matriz_of_fraction:
        datos:list[list[Fraction]] = [[self.get(f,c) + other.get(f,c) for c in range(self.nc)] for f in range(self.nf)]
        return Matriz_of_fraction.of(datos)
    
    def __sub__(self,other:Matriz_of_fraction)->Matriz_of_fraction:
        datos:list[list[Fraction]] = [[self.get(f,c) - other.get(f,c) for c in range(self.nc)] for f in range(self.nf)]
        return Matriz_of_fraction.of(datos)
    
    def __mul__(self,other:Matriz_of_fraction)->Matriz_of_fraction:
        Preconditions.check_argument(self.nc == other.nf, f'No se pueden multiplicar')
        ss:Callable[[int,int],Fraction] = lambda f,c:sum((self.get(f,k)*other.get(k,c) for k in range(self.nc)),Fraction(0))
        datos:list[list[Fraction]] = [[ss(f,c) for c in range(other.nc)] for f in range(self.nf)]
        return Matriz_of_fraction.of(datos)
    
if __name__ == '__main__':
    m3:Matriz_of_fraction = Matriz_of_fraction.of_file_fraction(absolute_path('/ficheros/matriz4.txt'))
    print(m3)
    print('----------------')
    m5:Matriz_of_fraction = Matriz_of_fraction.of_file_fraction(absolute_path('/ficheros/matriz7.txt'))
    print(m5)
    print('----------------')
    print(m3+m5)
    print('----------------')
    print(m3-m5)
    print('----------------')
    print(m3*m5)
    print('----------------')
    
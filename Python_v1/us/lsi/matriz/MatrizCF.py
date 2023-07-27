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


class MatrizF(Matriz[Fraction]):
    #===========================================================================
    # MÉTODOS DE FACTORÍA
    #===========================================================================
        
    @staticmethod
    def of(datos:list[list[Fraction]])->MatrizF:
        return MatrizF(datos)
    
    @staticmethod
    def of_file_fraction(file:str)->MatrizF:
        return MatrizF.of(Matriz.parse(file, lambda x: Fraction(x)).datos)

    #===========================================================================
    # PROPIEDADES DERIVADAS
    #===========================================================================
    @property
    def es_antisimetrica(self)->bool:
        indices:Iterable[tuple[int,int]] = ((f,c) for f,c in all_pairs(self.nf,self.nc) if f > c)
        return all(self.get(f,c) == -self.get(c,f) for f,c in indices)
    
    #===========================================================================
    # OTROS MÉTODOS
    #===========================================================================
    def __add__(self,other:MatrizF)->MatrizF:
        datos:list[list[Fraction]] = [[self.get(f,c) + other.get(f,c) for c in range(self.nc)] for f in range(self.nf)]
        return MatrizF.of(datos)
    
    def __sub__(self,other:MatrizF)->MatrizF:
        datos:list[list[Fraction]] = [[self.get(f,c) - other.get(f,c) for c in range(self.nc)] for f in range(self.nf)]
        return MatrizF.of(datos)
    
    def __mul__(self,other:MatrizF)->MatrizF:
        Preconditions.check_argument(self.nc == other.nf, f'No se pueden multiplicar')
        ss:Callable[[int,int],Fraction] = lambda f,c:sum((self.get(f,k)*other.get(k,c) for k in range(self.nc)),Fraction(0))
        datos:list[list[Fraction]] = [[ss(f,c) for c in range(other.nc)] for f in range(self.nf)]
        return MatrizF.of(datos)
    
if __name__ == '__main__':
    m2:MatrizF = MatrizF.of_file_fraction(absolute_path('/datos/matriz2.txt'))
    print(m2)
    print(m2.es_antisimetrica)
    m3:MatrizF = MatrizF.of_file_fraction(absolute_path('/datos/matriz4.txt'))
    print(m3)
    print(m3.es_antisimetrica)
    print('----------------')
    m5:MatrizF = MatrizF.of_file_fraction(absolute_path('/datos/matriz7.txt'))
    print(m5)
    print('----------------')
    print(m3+m5)
    print('----------------')
    print(m3-m5)
    print('----------------')
    print(m3*m5)
    print('----------------')
    
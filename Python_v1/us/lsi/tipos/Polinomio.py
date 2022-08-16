'''
Created on 16 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from numbers import Number
from us.lsi.tools.Preconditions import checkPositionIndex
from typing import TypeVar, Generic
from fractions import Fraction

E = TypeVar('E', bound=Number)

@dataclass(frozen=True)
class Polinomio(Generic[E]):
    coeficientes: list[E] 
      
    @staticmethod
    def of_list(coeficientes: list[E]) -> Polinomio[E]:
        return Polinomio(coeficientes)
    
    @staticmethod
    def of(*n:E) -> Polinomio[E]:
        coeficientes = list(n)
        return Polinomio(coeficientes)
    
    @property
    def grado(self) -> int:
        return len(self.coeficientes) -1
    
    def coeficiente(self,i:int)->E:
        checkPositionIndex(i,self.grado)
        return self.coeficientes[i]
    
    def value(self,v:E,unidad:E)->E:
        p: E = unidad
        s: E = p * self.coeficiente(0)
        for i in range(1,self.grado+1):
            p = p * v
            s = s + p*self.coeficiente(i) 
        return s
    
    def __str__(self) -> str:
        coefstr = list(f'{self.coeficiente(i)}x^{i}' if i > 0 else f'{self.coeficiente(i)}' for i in range(self.grado+1))
        return '+'.join(coefstr)

if __name__ == '__main__':
    p: Polinomio[int] = Polinomio.of(3,-4,5,7)
    print(p)
    print(p.grado)
    print(isinstance(p.coeficiente(0), Number))
    print(p.value(3,1))
    p2 : Polinomio[Fraction] = Polinomio.of(Fraction(3,5),Fraction(-4,5),Fraction(7))
    print(p2)
    print(p2.grado)
    print(isinstance(p2.coeficiente(0), Number))
    p3 : Polinomio[complex] = Polinomio.of(complex(3,5),complex(-4,5),complex(7))
    print(p3)
    print(p3.grado)
    print(p3.value(3+4j,complex(1,0)))
    print(isinstance(p3.coeficiente(0), Number))
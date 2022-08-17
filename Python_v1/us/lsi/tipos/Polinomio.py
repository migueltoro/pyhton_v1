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

E = TypeVar('E', float, complex, Fraction)

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
    
    @staticmethod
    def constante(z:E) -> Polinomio[E]:
        return Polinomio([z])
    
    @property
    def grado(self) -> int:
        return len(self.coeficientes) - 1
    
    def coeficiente(self,i:int)->E:
        checkPositionIndex(i,self.grado)
        return self.coeficientes[i]
    
    def factor(self,i:int)->Polinomio[E]:
        checkPositionIndex(i,self.grado)
        coef = list(self.coeficiente(j)-self.coeficiente(j) if j != i else  self.coeficiente(j) 
                    for j in range(self.grado+1))
        return Polinomio.of_list(coef)
    
    def value(self,v:E)->E:
        p: E = self.coeficiente(0) ** 0
        s: E = p * self.coeficiente(0)
        for i in range(1,self.grado+1):
            p = p * v
            s = s + p*self.coeficiente(i) 
        return s
    
    def __add__(self,other:Polinomio[E])-> Polinomio[E]:
        zero = self.coeficiente(0)-self.coeficiente(0)
        n = max(self.grado,other.grado)
        p1 = self.coeficientes + list(zero for i in range(n-self.grado))
        p2 = other.coeficientes + list(zero for i in range(n-other.grado))
        p = list(p1[i]+p2[i] for i in range(n+1))
        return Polinomio.of_list(p)
    
    def __sub__(self,other:Polinomio[E])-> Polinomio[E]:
        zero = self.coeficiente(0)-self.coeficiente(0)
        n = max(self.grado,other.grado)
        p1 = self.coeficientes + list(zero for i in range(n-self.grado))
        p2 = other.coeficientes + list(zero for i in range(n-other.grado))
        p = list(p1[i]-p2[i] for i in range(n+1))
        return Polinomio.of_list(p)
    
    def __mul__(self,other:Polinomio[E] | E)-> Polinomio[E]:
        if isinstance(other, Polinomio):
            n = self.grado+other.grado
            p = list(None for i in range(n+1))
            for i in range(0,self.grado+1):
                for j in range(0,other.grado+1):
                    p[i+j] = p[i+j] + self.coeficiente(i)*other.coeficiente(j) if p[i+j] else self.coeficiente(i)*other.coeficiente(j)
            return Polinomio.of_list(p)
        else:
            coef = list(other*self.coeficiente(i) for i in range(self.grado+1))
            return Polinomio.of_list(coef)
    
    @property
    def derivada(self):
        coeficientes = [self.coeficiente(i)*i for i in range(1,self.grado+1)]
        return Polinomio.of_list(coeficientes)
    
    def integral(self,v:E):
        coeficientes = [v]+[self.coeficiente(i)/(i+1) for i in range(self.grado+1)]
        return Polinomio.of_list(coeficientes)
    
    def __str__(self) -> str:
        coefstr = list(f'{self.coeficiente(i)}x^{i}' if i > 0 else f'{self.coeficiente(i)}' for i in range(self.grado,-1,-1))
        return '+'.join(coefstr)

if __name__ == '__main__':
    p0: Polinomio[Fraction] = Polinomio.of(Fraction(1),Fraction(1))
    p1: Polinomio[Fraction] = Polinomio.of(Fraction(3),Fraction(-4),Fraction(5),Fraction(7))
    p = p0 - p1
    print(p0)
    print(p1)
    print(p)
    
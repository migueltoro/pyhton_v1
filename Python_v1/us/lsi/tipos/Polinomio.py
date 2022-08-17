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
        return len(self.coeficientes) -1
    
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
        cf = lambda p,i: p.coeficiente(i) if i <= p.grado else 0
        n = max(self.grado,other.grado)
        coef = list(cf(self,i)+cf(other,i) for i in range(n+1))
        return Polinomio.of_list(coef)
    
    def __sub__(self,other:Polinomio[E])-> Polinomio[E]:
        cf = lambda p,i: p.coeficiente(i) if i <= p.grado else 0
        n = max(self.grado,other.grado)
        coef = list(cf(self,i)-cf(other,i) for i in range(n+1))
        return Polinomio.of_list(coef)
    
    def __mul__(self,other:Polinomio[E] | E)-> Polinomio[E]:
        if isinstance(other, Polinomio):
            p = self*other.coeficiente(0)
            print(p)
            for i in range(1,other.grado+1):
                p = p + self*other.c(i)
                print(p)
            return p
            print('_______________')
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
    print(p0*p0)
    p: Polinomio[Fraction] = Polinomio.of(Fraction(3),Fraction(-4),Fraction(5),Fraction(7))
    print(p)
    print(p.grado)
    print(isinstance(p.coeficiente(0), Number))
    print(p.value(1))
    print(p+p)
    print(p*Fraction(2))
    print('__________________')
    print(p.derivada)
    print(p.integral(0))
    print('__________________')
    p2 : Polinomio[Fraction] = Polinomio.of(Fraction(3,5),Fraction(-4,5),Fraction(7))
    print(p2)
    print(p2.grado)
    print(isinstance(p2.coeficiente(0), Number))
    print('__________________')
    print(p2.derivada)
    print(p2.integral(Fraction(0)))
    print('__________________')
    p3 : Polinomio[complex] = Polinomio.of(complex(3,5),complex(-4,5),complex(7))
    print(p3)
    print(p3.grado)
    print(p3.value(complex(1,0)))
    print('__________________')
    print(p3.derivada)
    print('__________________')
    print(isinstance(p3.coeficiente(0), Number))
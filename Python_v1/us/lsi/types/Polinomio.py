'''
Created on 16 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass, astuple, asdict
from us.lsi.tools.Preconditions import check_position_index, check_argument
from fractions import Fraction

@dataclass(frozen=True)
class Polinomio():
    coeficientes: list[Fraction] 
      
    @staticmethod
    def of_list(coeficientes: list[Fraction]) -> Polinomio:
        return Polinomio(coeficientes)
    
    @staticmethod
    def of(*n:Fraction) -> Polinomio:
        coeficientes = list(n)
        return Polinomio(coeficientes)
    
    @staticmethod
    def zero() -> Polinomio:
        return Polinomio([Fraction(0,1)])
    
    @staticmethod
    def one() -> Polinomio:
        return Polinomio([Fraction(1,1)])
    
    @property
    def grado(self) -> int:
        return len(self.coeficientes) - 1
    
    def coeficiente(self,i:int)->Fraction:
        check_position_index(i,self.grado)
        return self.coeficientes[i]
    
    @property
    def constains_coeficiente_zero(self)->bool:
        return Fraction(0,1) in self.coeficientes
    
    def value(self,v:Fraction)->Fraction:
        p: Fraction = Fraction(1,1)
        s: Fraction = self.coeficiente(0)
        for i in range(1,self.grado+1):
            p = p * v
            s = s + p*self.coeficiente(i) 
        return s
    
    def __add__(self,other:Polinomio)-> Polinomio:
        n = max(self.grado,other.grado)
        p1 = self.coeficientes + [Fraction(0,1) for _ in range(n-self.grado)]
        p2 = other.coeficientes + [Fraction(0,1) for _ in range(n-other.grado)]
        p = list(p1[i]+p2[i] for i in range(n+1))
        return Polinomio.of_list(p)
        
    def __sub__(self,other:Polinomio)-> Polinomio:
        n = max(self.grado,other.grado)
        p1 = self.coeficientes + [Fraction(0,1) for _ in range(n-self.grado)]
        p2 = other.coeficientes + [Fraction(0,1) for _ in range(n-other.grado)]
        p = list(p1[i]-p2[i] for i in range(n+1))
        return Polinomio.of_list(p)
    
    def __mul__(self,other:Polinomio | Fraction)-> Polinomio:
        if isinstance(other, Polinomio):
            n = self.grado+other.grado
            p = [Fraction(0,1) for i in range(n+1)]
            for i in range(0,self.grado+1):
                for j in range(0,other.grado+1):
                    p[i+j] = p[i+j] + self.coeficiente(i)*other.coeficiente(j)
            return Polinomio.of_list(p)
        else:
            coef = list(other*self.coeficiente(i) for i in range(self.grado+1))
            return Polinomio.of_list(coef)
        
    def __pow__(self,n:int)-> Polinomio:
        check_argument(n >=0,f'elexponente no puede ser negativo y es {n}')
        r: Polinomio = Polinomio.one()
        for _ in range(n):
            r = r*self
        return r 
    
    @property
    def derivada(self)->Polinomio:
        coeficientes = [self.coeficiente(i)*i for i in range(1,self.grado+1)]
        return Polinomio.of_list(coeficientes)
    
    def integral(self,v:Fraction = Fraction(0,1))->Polinomio:
        coeficientes:list[Fraction] = [v]+[self.coeficiente(i)/(i+1) for i in range(self.grado+1)]
        return Polinomio.of_list(coeficientes)
    
    def __str__(self) -> str:
        coefstr = [f'{self.coeficiente(i)}x^{i}' if i > 0 else f'{self.coeficiente(i)}' 
                            for i in range(self.grado,-1,-1)]
        return '+'.join(coefstr)

if __name__ == '__main__':
    p0: Polinomio = Polinomio.of(Fraction(1,1),Fraction(1,1))
    p1: Polinomio = Polinomio.of(Fraction(3,1),Fraction(-4,1),Fraction(0,1),Fraction(7))
    print(f'p0 = {p0}')
    print(f'p1 = {p1}')
    print(f'Derivada de p1 = {p1.derivada}')
    print(f'Integral de p1 = {p1.integral()}')
    print(f'Valor de p0 en 1 = {p0.value(Fraction(1,1))}')
    print(f'p1 = {p1}')
    print(f'p0*p1 = {p0 * p1}')
    print(f'p0+p1 = {p0 + p1}')
    print(f'p0**2 = {p0 ** 2}')
    print(p1.constains_coeficiente_zero)
    print(astuple(p1))
    print(asdict(p1))
    
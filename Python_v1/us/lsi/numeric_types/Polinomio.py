'''
Created on 16 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from us.lsi.tools.Preconditions import check_position_index, check_argument
from fractions import Fraction
from typing import TypeVar, Generic
from us.lsi.numeric_types.Field import FieldElement,Field,FractionField,ComplexField,FloatField

S = TypeVar('S',bound=FieldElement)

@dataclass(frozen=True)
class Polinomio(Generic[S]):
    coeficientes: list[S]
    field:Field[S]
      
    @staticmethod
    def of_list(coeficientes: list[S],field: Field[S]) -> Polinomio[S]:
        return Polinomio(coeficientes,field)
    
    @staticmethod
    def of_value(v: S,field: Field[S]) -> Polinomio[S]:
        return Polinomio([v],field)
    
    @staticmethod
    def of(field: Field[S],*n:S) -> Polinomio[S]:
        coeficientes = list(n)
        return Polinomio(coeficientes,field)
    
    @staticmethod
    def zero(field: Field[S]) -> Polinomio[S]:
        return Polinomio([field.zero],field)
    
    @staticmethod
    def one(field: Field[S]) -> Polinomio[S]:
        return Polinomio([field.one],field)
    
    @property
    def grado(self) -> int:
        return len(self.coeficientes) - 1
    
    def coeficiente(self,i:int)->S:
        check_position_index(i,self.grado)
        return self.coeficientes[i]
    
    @property
    def constains_coeficiente_zero(self)->bool:
        return self.field.zero in self.coeficientes
    
    def value(self,v:S)->S:
        p: S = self.field.one
        s: S = self.coeficiente(0)
        for i in range(1,self.grado+1):
            p = p * v
            s = s + p*self.coeficiente(i) 
        return s
    
    def __add__(self,other:Polinomio[S])-> Polinomio[S]:
        n = max(self.grado,other.grado)
        p1 = self.coeficientes + [self.field.zero for _ in range(n-self.grado)]
        p2 = other.coeficientes + [self.field.zero for _ in range(n-other.grado)]
        p = list(p1[i]+p2[i] for i in range(n+1))
        return Polinomio.of_list(p,self.field)
        
    def __sub__(self,other:Polinomio[S])-> Polinomio[S]:
        n = max(self.grado,other.grado)
        p1 = self.coeficientes + [self.field.zero for _ in range(n-self.grado)]
        p2 = other.coeficientes + [self.field.zero for _ in range(n-other.grado)]
        p = list(p1[i]-p2[i] for i in range(n+1))
        return Polinomio.of_list(p,self.field)
    
    def __mul__(self,other:Polinomio[S] | S)-> Polinomio[S]:
        if isinstance(other, Polinomio):
            n = self.grado+other.grado
            p = [self.field.zero for i in range(n+1)]
            for i in range(0,self.grado+1):
                for j in range(0,other.grado+1):
                    p[i+j] = p[i+j] + self.coeficiente(i)*other.coeficiente(j)
            return Polinomio.of_list(p,self.field)
        else:
            coef = list(other*self.coeficiente(i) for i in range(self.grado+1))
            return Polinomio.of_list(coef,self.field)
        
    def __pow__(self,n:int)-> Polinomio:
        check_argument(n >=0,f'elexponente no puede ser negativo y es {n}')
        r: Polinomio[S] = Polinomio.one(self.field)
        for _ in range(n):
            r = r*self
        return r 
    
    @property
    def derivada(self)->Polinomio:
        coeficientes = [self.coeficiente(i)*i for i in range(1,self.grado+1)]
        return Polinomio.of_list(coeficientes,self.field)
    
    def integral(self,v:S)->Polinomio:
        coeficientes:list[S] = [v]+[self.coeficiente(i)/(i+1) for i in range(self.grado+1)]
        return Polinomio.of_list(coeficientes,self.field)
    
    def __str__(self) -> str:
        coefstr = [f'{self.coeficiente(i)}x^{i}' if i > 0 else f'{self.coeficiente(i)}' 
                            for i in range(self.grado,-1,-1)]
        return '+'.join(coefstr)

if __name__ == '__main__':
    p0: Polinomio[Fraction] = Polinomio.of(FractionField(),Fraction(1,1),Fraction(1,1))
    p1: Polinomio[Fraction] = Polinomio.of(FractionField(),Fraction(3,1),Fraction(-4,1),Fraction(0,1),Fraction(7))
    print(f'p0 = {p0}')
    print(f'p1 = {p1}')
    print(f'Derivada de p1 = {p1.derivada}')
    print(f'Integral de p1 = {p1.integral(Fraction(0))}')
    print(f'Valor de p0 en 1 = {p0.value(Fraction(1,1))}')
    print(f'p1 = {p1}')
    print(f'p0*p1 = {p0 * p1}')
    print(f'p0+p1 = {p0 + p1}')
    print(f'p0**2 = {p0 ** 2}')
    print(p1.constains_coeficiente_zero)
    print('_____________________')
    p2: Polinomio[complex] = Polinomio.of(ComplexField(),complex(1,1),complex(1,1))
    p3: Polinomio[complex] = Polinomio.of(ComplexField(),complex(3,1),complex(-4,1),complex(0),complex(7))
    print(f'p2 = {p2}')
    print(f'p3 = {p3}')
    print(f'Derivada de p3 = {p3.derivada}')
    print(f'Integral de p3 = {p3.integral(complex(0))}')
    print(f'Valor de p2 en 1 = {p2.value(complex(1,1))}')
    print(f'p1 = {p2}')
    print(f'p2*p3 = {p2 * p3}')
    print(f'p2+p3 = {p2 + p3}')
    print(f'p2**2 = {p2 ** 2}')
    print(p3.constains_coeficiente_zero)
    print('_____________________')
    p4: Polinomio[float] = Polinomio.of(FloatField(),1,1)
    p5: Polinomio[float] = Polinomio.of(FloatField(),3,-4,0,7)
    print(f'p4 = {p4}')
    print(f'p5 = {p5}')
    print(f'Derivada de p5 = {p5.derivada}')
    print(f'Integral de p5 = {p5.integral(0.)}')
    print(f'Valor de p4 en 1 = {p4.value(1)}')
    print(f'p5 = {p5}')
    print(f'p4*p5 = {p4 * p5}')
    print(f'p4+p5 = {p4 + p5}')
    print(f'p4**2 = {p4 ** 2}')
    print(p5.constains_coeficiente_zero)
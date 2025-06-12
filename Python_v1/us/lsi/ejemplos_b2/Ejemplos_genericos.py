'''
Created on 10 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import Generic, TypeVar
from fractions import Fraction
from abc import ABC,abstractmethod


A = TypeVar('A')
B = TypeVar('B')
E = TypeVar('E')
 

class Par(Generic[A,B]):
    
    def __init__(self,first: A,second: B)->None:
        self.__first=first
        self.__second= second
      
    @staticmethod
    def of(first:A,second:B) -> Par[A,B]:
        return Par(first,second)
    
    @property
    def first(self)->A:
        return self.__first
    
    @property
    def second(self)->B:
        return self.__second
      
    def __eq__(self,other)->bool:
        r:bool=False
        if isinstance(other, Par):
            r = self.__first == other.__first and self.__second == other.__second
        return r
    
    def __str__(self) -> str:
        return f'({self.__first},{self.__second})'
    

class Polinomio(ABC,Generic[E]): 
    
    def __init__(self,coeficientes: list[E])->None:
        self.__coeficientes: list[E] = coeficientes 
        
    @staticmethod
    @abstractmethod
    def of_list(coeficientes: list[E]) -> Polinomio[E]:
        ...
    
    @staticmethod
    @abstractmethod
    def of(*n:Fraction) -> Polinomio[E]:
        ...
    
    @staticmethod
    @abstractmethod
    def zero() -> Polinomio[E]:
        ...
    
    @staticmethod
    @abstractmethod
    def one() -> Polinomio[E]:
        ...
    
    @property
    @abstractmethod
    def grado(self) -> int:
        ...
    
    def coeficiente(self,i:int)->E:
        assert 0 <= i <= self.grado, f'Índice {i} fuera de rango [0,{self.grado}]'
        return self.__coeficientes[i]
        
    def coeficientes(self)->list[E]:
        return self.__coeficientes
    
    @property
    @abstractmethod
    def constains_coeficiente_zero(self)->bool:
        ...
    
    @abstractmethod
    def value(self,v:E)->E:
        ...
    
    @abstractmethod
    def __add__(self,other:Polinomio[E])-> Polinomio[E]:
        ...
    
    @abstractmethod    
    def __sub__(self,other:Polinomio[E])-> Polinomio[E]:
        ...
    
    @abstractmethod
    def __mul__(self,other:Polinomio[E] | E)-> Polinomio[E]:
        ...
    
    @abstractmethod    
    def __pow__(self,n:int)-> Polinomio[E]:
        ...
    
    @property
    @abstractmethod
    def derivada(self)->Polinomio[E]:
        ...
    
    @abstractmethod
    def integral(self,v:E)->Polinomio[E]:
        ...
    
    @abstractmethod
    def __str__(self) -> str:
        ...
    
    @abstractmethod   
    def __eq__(self,other)->bool:
        ...


class PolinomioF(Polinomio[Fraction]):
    
    def __init__(self,coeficientes: list[Fraction])->None:
        super().__init__(coeficientes)
      
    @staticmethod
    def of_list(coeficientes: list[Fraction]) -> PolinomioF:
        return PolinomioF(coeficientes)
    
    @staticmethod
    def of(*n:Fraction) -> PolinomioF:
        coeficientes = list(n)
        return PolinomioF(coeficientes)
    
    @staticmethod
    def zero() -> PolinomioF:
        return PolinomioF([Fraction(0,1)])
    
    @staticmethod
    def one() -> PolinomioF:
        return PolinomioF([Fraction(1,1)])
    
    @property
    def grado(self) -> int:
        return len(self.coeficientes()) - 1
    
    @property
    def constains_coeficiente_zero(self)->bool:
        return Fraction(0,1) in self.coeficientes()
    
    def value(self,v:Fraction)->Fraction:
        p: Fraction = Fraction(1,1)
        s: Fraction = self.coeficiente(0)
        for i in range(1,self.grado+1):
            p = p * v
            s = s + p*self.coeficiente(i) 
        return s
    
    def __add__(self,other:Polinomio[Fraction])-> PolinomioF:
        n = max(self.grado,other.grado)
        p1:list[Fraction] = self.coeficientes() + [Fraction(0,1) for _ in range(n-self.grado)]
        p2:list[Fraction] = other.coeficientes() + [Fraction(0,1) for _ in range(n-other.grado)]
        p:list[Fraction] = list(p1[i]+p2[i] for i in range(n+1))
        return PolinomioF.of_list(p)
        
    def __sub__(self,other:Polinomio[Fraction])-> PolinomioF:
        n = max(self.grado,other.grado)
        p1:list[Fraction] = self.coeficientes() + [Fraction(0,1) for _ in range(n-self.grado)]
        p2:list[Fraction] = other.coeficientes() + [Fraction(0,1) for _ in range(n-other.grado)]
        p:list[Fraction] = list(p1[i]-p2[i] for i in range(n+1))
        return PolinomioF.of_list(p)
    
    def __mul__(self,other:Polinomio[Fraction] | Fraction)-> PolinomioF:
        if isinstance(other, PolinomioF):
            n = self.grado+other.grado
            p = [Fraction(0,1) for i in range(n+1)]
            for i in range(0,self.grado+1):
                for j in range(0,other.grado+1):
                    p[i+j] = p[i+j] + self.coeficiente(i)*other.coeficiente(j)
            return PolinomioF.of_list(p)
        elif isinstance(other, Fraction):
            c:Fraction = other
            coef:list[Fraction] = list(c*self.coeficiente(i) for i in range(self.grado+1))
            return PolinomioF.of_list(coef)
        else:
            raise Exception(f'No se puede multiplicar por {other}')
        
    def __pow__(self,n:int)-> PolinomioF:
        assert n >=0,f'elexponente no puede ser negativo y es {n}'
        r: PolinomioF = PolinomioF.one()
        for _ in range(n):
            r = r*self
        return r 
    
    @property
    def derivada(self)->PolinomioF:
        coeficientes:list[Fraction] = [self.coeficiente(i)*i for i in range(1,self.grado+1)]
        return PolinomioF.of_list(coeficientes)
    
    def integral(self,v:Fraction = Fraction(0,1))->PolinomioF:
        coeficientes:list[Fraction] = [v]+[self.coeficiente(i)/(i+1) for i in range(self.grado+1)]
        return PolinomioF.of_list(coeficientes)
    
    def __str__(self) -> str:
        coefstr = [f'{self.coeficiente(i)}x^{i}' if i > 0 else f'{self.coeficiente(i)}' 
                            for i in range(self.grado,-1,-1)]
        return '+'.join(coefstr)
    
    def __eq__(self,other)->bool:
        r:bool=False
        if isinstance(other, PolinomioF):
            r = self.coeficientes() == other.coeficientes()
        return r
    
def test_par():
    p1 = Par.of(Fraction(4,56),45)
    p2 = Par.of(Fraction(4,56),46)
    p3 = Par.of(Fraction(4,56),45)
    print(p1 == p3)
    print(p1 == p2)


def test_polinomio():
    p0: PolinomioF = PolinomioF.of(Fraction(1,1),Fraction(1,1))
    p1: PolinomioF = PolinomioF.of(Fraction(3,1),Fraction(-4,1),Fraction(0,1),Fraction(7))
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
 
if __name__ == '__main__':
    test_polinomio()
    test_par()
    
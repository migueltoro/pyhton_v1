'''
Created on 22 nov 2021

@author: migueltoro
'''

from __future__ import annotations
from functools import total_ordering
from random import randint
from us.lsi.tools.Preconditions import checkArgument
from us.lsi.tools.Iterable import str_iterable

def mcd(a:int, b:int)->int:
    checkArgument(a>=0 and b>0,'El coeficiente a debe ser mayor o igual que cero y b mayor que cero y son: \
    a = {0}, b = {1}'.format(a,b))
    while b > 0:
        a, b = b, a%b
    return a

@total_ordering
class Fraccion:
    
    def __init__(self, n:int, d:int=1):
        checkArgument(d != 0,'El denominador no puede ser cero')
        self._numerador = n
        self._denominador = d
        self.__normaliza()
        
    def __normaliza(self)->None:
        n = self._numerador
        d = self._denominador
        sg = 1 if d > 0 else -1
        m = mcd(abs(n),abs(d))*sg
        self._numerador = n//m
        self._denominador = d//m
        
    @staticmethod
    def of(n:int,d:int=1)->Fraccion:  
        return Fraccion(n,d)
    
    @staticmethod
    def random(lm:int)->Fraccion:  
        n = randint(-lm,lm)
        d = randint(1,lm)
        return Fraccion(n,d)
        
    def add(self,other)->Fraccion:
        resultado_numerador = self._numerador*other._denominador +self._denominador*other._numerador
        resultado_denominador = self._denominador*other._denominador
        resultado = Fraccion(resultado_numerador,resultado_denominador)
        return resultado
    
    @property
    def numerador(self)->int:
        return self._numerador
    
    def set_numerador(self,n)->None:
        self._numerador = n
        self.__normaliza()
    
    def denominador(self)->int:
        return self._denominador
    
    def set_denominador(self,d)->None:
        self._denominador = d
        self.__normaliza()
    
    def __eq__(self, other)->bool:
        if isinstance(other, Fraccion):
            return self._numerador == other._numerador and self._denominador == other._denominador
        return False
    
    def __ne__(self, other)->bool:
        return not (self == other)
    
    def __lt__(self, other)->bool:
        return self._numerador*other._denominador < self._denominador*other._numerador
    
    def __hash__(self)->int:
        return  hash(self._numerador)*31 + hash(self._denominador)
    
    def __str__(self)->str:
        if self._denominador == 1:
            return '{0:d}'.format(self._numerador)
        else:
            return '{0:d}/{1:d}'.format(self._numerador,self._denominador)

if __name__ == '__main__':
    f1 = Fraccion.of(3)
    print(f1.numerador)
    print(f1.denominador())
    f2 = Fraccion.of(3, 6)
    print(f1 >= f2)
    f3 = Fraccion.of(2, -12)
    print(f3)
    f3.set_denominador(10)
    print(f3)
    ls = (Fraccion.random(1000) for _ in range(50))
    print(str_iterable(ls))

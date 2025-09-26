'''
Created on 22 nov 2021

@author: migueltoro
'''
from __future__ import annotations
from functools import total_ordering
from random import randint
from us.lsi.tools.Iterable import str_iter

def mcd(a:int, b:int)->int:
    assert a>=0 and b>0,f'El coeficiente a debe ser mayor o igual que cero y b mayor que cero y son: a = {a}, b = {b}'
    while b > 0:
        a, b = b, a%b
    return a
    
#Fraccion inmutable
@total_ordering
class Fraccion:
    
    def __init__(self,n:int,d:int)->None:
        self.__numerador = n
        self.__denominador = d
        assert self.__denominador != 0,f'El denominador no puede ser cero y es {self.__denominador}'
        self.__normaliza()       
        
        
    def __normaliza(self)->None:
        n = self.__numerador
        d = self.__denominador
        sg = 1 if d > 0 else -1
        m = mcd(abs(n),abs(d))*sg
        self.__numerador = n//m
        self.__denominador = d//m
        
    @staticmethod
    def of(n:int,d:int=1)->Fraccion: 
        assert d != 0,f'El denominador no puede ser cero y es {d}' 
        return Fraccion(n,d)
    
    @staticmethod
    def random(lm:int)->Fraccion:  
        n = randint(-lm,lm)
        d = randint(1,lm)
        return Fraccion(n,d)
    
    def __neg__(self):
        return Fraccion(-self.numerador,self.denominador)
        
    def __add__(self,other:Fraccion)->Fraccion:
        n = self.numerador*other.denominador +self.denominador*other.numerador
        d = self.denominador*other.denominador
        resultado = Fraccion(n,d)
        return resultado
    
    def __sub__(self,other:Fraccion)->Fraccion:
        n = self.numerador*other.denominador - self.denominador*other.numerador
        d = self.denominador*other.denominador
        resultado = Fraccion(n,d)
        return resultado
        
    def __mul__(self,other:Fraccion)->Fraccion:
        n = self.numerador*other.numerador
        d = self.denominador*other.denominador
        return Fraccion(n,d)
    
    def __truediv__(self,other:Fraccion)->Fraccion:
        n = self.numerador*other.denominador
        d = self.denominador*other.numerador
        return Fraccion(n,d)
    
    def __invert__(self)->Fraccion:
        assert self.__numerador != 0,f'El denominador no puede ser cero y es {self.__numerador}'
        return Fraccion.of(self.denominador,self.numerador)
    
    @property
    def numerador(self)->int:
        return self.__numerador
    
    @property
    def denominador(self)->int:
        return self.__denominador
    
    def __eq__(self, other)->bool:
        if isinstance(other, Fraccion):
            return self.numerador == other.numerador and self.denominador == other.denominador
        return False
    
    def __lt__(self, other)->bool:
        return self.numerador*other.denominador < self.denominador*other.numerador
    
    def __hash__(self)->int:
        return  hash(self.numerador)*31 + hash(self.denominador)
    
    def __str__(self)->str:
        if self.denominador == 1:
            return '{0:d}'.format(self.numerador)
        else:
            return '{0:d}/{1:d}'.format(self.numerador,self.denominador)

if __name__ == '__main__':
    f1 = Fraccion.of(3)
    print('1:',f1.numerador)
    print('2:',f1.denominador)
    f2 = Fraccion.of(3, 6)
    print('3:',f1 >= f2)
    f3 = Fraccion.of(2, -12)
    print(f3)
    print('4:',f3+f2)
    print('5:',f3-f2)
    print('6:',f3*f2)
    print('7:',f3/f2)
    print('8:', -f3/f2)
    print('9:', f3)
    print('9:', f2)
    print('9:', ~(f3/f2))
    ls:list[Fraccion] = [Fraccion.random(1000) for _ in range(50)]
    print('10:',str_iter(ls))

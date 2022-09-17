'''
Created on 22 nov 2021

@author: migueltoro
'''
from __future__ import annotations
from functools import total_ordering
from random import randint
from us.lsi.tools.Preconditions import check_argument
from us.lsi.tools.Iterable import strfiter
from us.lsi.tools.Functions import mcd
from us.lsi.tipos.Field import Field
from us.lsi.tipos.FieldElement import FieldElement


class FraccionField(Field):
       
    @staticmethod
    def of()->FraccionField: 
        return FraccionField()
    @property
    def one(self)-> Fraccion:
        return Fraccion.of(1)
    @property
    def zero(self)->Fraccion:
        return Fraccion.of(0)
    
#Fraccion mutable
@total_ordering
class Fraccion(FieldElement['Fraccion']):
    
    def __init__(self,n:int,d:int):
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
        check_argument(d != 0,f'El denominador no puede ser cero y es {d}') 
        return Fraccion(n,d)
    
    @staticmethod
    def random(lm:int)->Fraccion:  
        n = randint(-lm,lm)
        d = randint(1,lm)
        return Fraccion(n,d)
    
    @property
    def field(self)->FraccionField:
        return FraccionField.of()
    
    def __neg__(self):
        return Fraccion(-self.numerador,self.denominador)
        
    def __add__(self,other:Fraccion)->Fraccion:
        n = self.numerador*other._denominador +self.denominador*other.numerador
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
        check_argument(self._numerador != 0,f'El denominador no puede ser cero y es {self._numerador}')
        return Fraccion.of(self.denominador,self.numerador)
    
    @property
    def numerador(self)->int:
        return self._numerador
    
    def set_numerador(self,n)->None:
        self._numerador = n
        self.__normaliza()
    
    @property
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
    print('1:',f1.numerador)
    print('2:',f1.denominador)
    f2 = Fraccion.of(3, 6)
    print('3:',f1 >= f2)
    f3 = Fraccion.of(2, -12)
    print(f3)
    f3.set_denominador(10)
    print('4:',f3+f2)
    print('5:',f3-f2)
    print('6:',f3*f2)
    print('7:',f3/f2)
    print('8:', -f3/f2)
    print('9:', f3)
    print('9:', f2)
    print('9:', ~(f3/f2))
    ls:list[Fraccion] = [Fraccion.random(1000) for _ in range(50)]
    print('10:',strfiter(ls))
    print(f1.field.zero)

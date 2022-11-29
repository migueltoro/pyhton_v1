'''
Created on 19 oct 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Generic
from fractions import Fraction
from typing_extensions import Protocol

E = TypeVar("E")

class RingElement(Protocol[E]):

    def __add__(self,other:E)->E:  
        pass 
    def __sub__(self,other:E)->E:  
        pass 
    def __mul__(self,other:E)->E:  
        pass 


class FieldElement(Protocol[E]):

    def __add__(self,other:E)->E:  
        pass 
    def __sub__(self,other:E)->E:  
        pass 
    def __mul__(self,other:E)->E:  
        pass 
    def __truediv__(self,other:E)->E:
        pass


R = TypeVar("R",bound=FieldElement)

class Field(Generic[R]):
            
    @property
    def one(self)->R:
        pass
    @property 
    def zero(self)->R:
        pass
    @staticmethod
    def of_file(text:str)->R:
        pass
    
class FractionField(Field[Fraction]):
    
    @property
    def one(self)->Fraction:
        return Fraction(1)
    @property 
    def zero(self)->Fraction:
        return Fraction(0)
    @staticmethod
    def of_file(text:str)->Fraction:
        return Fraction(text)

class ComplexField(Field[complex]):
    
    @property
    def one(self)->complex:
        return complex(1,0)
    @property 
    def zero(self)->complex:
        return complex(0,0)
    @staticmethod
    def of_file(text:str)->complex:
        return complex(text)
    
class FloatField(Field[float]):
    
    @property
    def one(self)->float:
        return 1.
    @property 
    def zero(self)->float:
        return 0.
    @staticmethod
    def of_file(text:str)->float:
        return float(text) 
       

if __name__ == '__main__':
    f:Fraction = FractionField().one
    print(f)
    cf:complex = ComplexField().one
    print(cf)
    ff:float = FloatField().one
    print(ff)
    
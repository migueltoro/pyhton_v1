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
    
    @staticmethod       
    def one()->R:
        pass
    @staticmethod 
    def zero()->R:
        pass
    @staticmethod
    def parse(text:str)->R:
        pass
    @staticmethod
    def str(v:R)->str:
        pass
    
    
class FractionField(Field[Fraction]):
    
    @staticmethod   
    def one()->Fraction:
        return Fraction(1)
    @staticmethod 
    def zero()->Fraction:
        return Fraction(0)
    @staticmethod   
    def parse(text:str)->Fraction:
        return Fraction(text)
    @staticmethod   
    def str(v:Fraction)->str:
        return str(v)

class ComplexField(Field[complex]):
    
    @staticmethod
    def one()->complex:
        return complex(1,0)
    @staticmethod
    def zero()->complex:
        return complex(0,0)
    @staticmethod
    def parse(text:str)->complex:
        return complex(text)
    @staticmethod
    def str(v:complex)->str:
        return f'{v.real:.2f}{"+"if v.imag > 0 else ""}{v.imag:.2f}i'
    
class FloatField(Field[float]):
    
    @staticmethod
    def one()->float:
        return 1.
    @staticmethod 
    def zero()->float:
        return 0.
    @staticmethod 
    def parse(text:str)->float:
        return float(text)
    @staticmethod
    def str(v:float)->str:
        return f'{v:.2f}'
       

if __name__ == '__main__':
    f:Fraction = FractionField().one()
    print(f)
    cf:complex = ComplexField().one()
    print(cf)
    ff:float = FloatField().one()
    print(ff)
    
'''
Created on 27 oct 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Protocol, Any
from fractions import Fraction


E = TypeVar('E', contravariant=True)
R = TypeVar('R')

class Comparable(Protocol[E]):

    def __eq__(self:E, other:Any) -> bool: ...
       
    def __lt__(self:E, other: E) -> bool: ...

    def __gt__ (self:E, other:E)->bool: ...
    
    def __ne__ (self:E, other:Any)->bool: ...
        
    def __le__(self:E, other:E) -> bool: ...
    
    def __ge__ (self:E, other:E)->bool: ...
    

class Sum(Protocol[R]):

    def __add__(self:R, other:R) -> R: ...

class SumDiv(Protocol[R]):

    def __add__(self:R, other:R) -> R: ...

    def __truediv__(self:R, other:R) -> R: ...

class RingElement(Protocol[R]):

    def __add__(self,other:R)->R:  ...
        
    def __sub__(self,other:R)->R:  ...
         
    def __mul__(self,other:R)->R:  ...
        


class FieldElement(Protocol[R]):

    def __add__(self,other:R)->R:  ...
        
    def __sub__(self,other:R)->R:  ...
         
    def __mul__(self,other:R)->R:  ...
         
    def __truediv__(self,other:R)->R: ...
        


F = TypeVar("F",bound=FieldElement)

class Field(Protocol[F]):
    
    @staticmethod       
    def one()->F: ...
        
    @staticmethod 
    def zero()->F: ...
        
    @staticmethod
    def parse(text:str)->F: ...
        
    @staticmethod
    def str(v:F)->str: ...
           
    
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
        return f'{v.real:.2f}{"+"if v.imag > 0 else "-"}{abs(v.imag):.2f}i'
    
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
    pass
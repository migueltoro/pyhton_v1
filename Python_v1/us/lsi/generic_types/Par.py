'''
Created on 12 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import Generic, TypeVar
from fractions import Fraction
from functools import total_ordering
from us.lsi.generic_types.Comparable import Comparable


A = TypeVar('A')
B = TypeVar('B')


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

E = TypeVar('E', bound=Comparable)
R = TypeVar('R', bound=Comparable)
    
@total_ordering
class ParOrd(Par[E,R]):
      
    @staticmethod
    def of(first:E,second:R) -> ParOrd[E,R]:
        return ParOrd(first,second)
    
    def __lt__(self, other:Par[E,R])->bool:
        return self.first < other.first or  (self.first == other.first and self.second < other.second)
    
        
if __name__ == '__main__':
    p1 = Par.of(Fraction(4,56),45)
    p2 = Par.of(Fraction(4,56),46)
    p3 = Par.of(Fraction(4,56),45)
    print(p1 == p3)
    p1.__second = 7
    p4 = ParOrd.of(45,46)
    p5 = ParOrd.of(50,1)
    print(p4 >= p5)
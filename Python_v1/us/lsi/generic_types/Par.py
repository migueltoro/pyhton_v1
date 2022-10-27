'''
Created on 16 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import Generic, TypeVar
from fractions import Fraction
from functools import total_ordering
from us.lsi.generic_types.Comparable import Comparable

A = TypeVar('A', bound=Comparable)
B = TypeVar('B', bound=Comparable)


@total_ordering
class Par(Generic[A,B]):
    
    def __init__(self,first: A,second: B)->None:
        self.first=first
        self.second= second
      
    @staticmethod
    def of(first:A,second:B) -> Par[A,B]:
        return Par(first,second)
    
    def __eq__(self,other)->bool:
        r:bool=False
        if isinstance(other, Par):
            r = self.first == other.first and self.second == other.second
        return r
    
    def __lt__(self, other:Par[A,B])->bool:
        return self.first < other.first or  (self.first == other.first and self.second < other.second)
    
    def __str__(self) -> str:
        return f'({self.first},{self.second})'
 
if __name__ == '__main__':
    p1 = Par.of(Fraction(4,56),45)
    p2 = Par.of(Fraction(4,56),46)
    p3 = Par.of(Fraction(4,56),45)
    print(p2 >= p1)
    print(p1 == p3)
    p1.second = 7
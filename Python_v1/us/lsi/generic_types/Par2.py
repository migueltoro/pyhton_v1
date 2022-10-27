'''
Created on 27 oct 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import Generic, TypeVar
from fractions import Fraction
from functools import total_ordering
from us.lsi.generic_types.Comparable import Comparable
from attr import define, astuple, asdict

A = TypeVar('A', bound=Comparable)
B = TypeVar('B', bound=Comparable)


@define
@total_ordering
class Par2(Generic[A,B]):
    first:A
    second:B
         
    @staticmethod
    def of(first:A,second:B) -> Par2[A,B]:
        return Par2(first,second)
    
    @property
    def astuple(self)->tuple[A,B]:
        return (self.first,self.second)
    
    def __eq__(self,other)->bool:
        r:bool=False
        if isinstance(other, Par2):
            r = self.first == other.first and self.second == other.second
        return r
    
    def __lt__(self, other:Par2[A,B])->bool:
        return self.first < other.first or  (self.first == other.first and self.second < other.second)
    
    def __str__(self) -> str:
        return f'({self.first},{self.second})'

if __name__ == '__main__':
    p1 = Par2.of(Fraction(4,56),45)
    p2 = Par2.of(Fraction(4,56),46)
    p3 = Par2.of(Fraction(4,56),45)
    print(p2 >= p1)
    print(p1 == p3)
    print(astuple(p1))
    print(asdict(p2))
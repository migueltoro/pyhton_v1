'''
Created on 16 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import Generic, TypeVar
from fractions import Fraction

A = TypeVar('A')
B = TypeVar('B')


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
    
    def __str__(self) -> str:
        return f'({self.first},{self.second})'

if __name__ == '__main__':
    p = Par.of(Fraction(4,56),complex(4,56))
    print(p)
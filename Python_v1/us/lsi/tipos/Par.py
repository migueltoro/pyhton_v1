'''
Created on 16 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar
from fractions import Fraction

A = TypeVar('A')
B = TypeVar('B')


@dataclass(frozen=True)
class Par(Generic[A,B]):
    first: A
    second: B 
      
    @staticmethod
    def of(first:A,second:B) -> Par[A,B]:
        return Par(first,second)
    
    def __str__(self) -> str:
        return f'({self.first},{self.second})'

if __name__ == '__main__':
    p = Par.of(Fraction(4,56),complex(4,56))
    print(p)
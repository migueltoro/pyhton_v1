'''
Created on 16 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class IntPar:
    first: int
    second: int 
      
    @staticmethod
    def of(first:int,second:int) -> IntPar:
        return IntPar(first,second)
    
    def __str__(self) -> str:
        return f'({self.first},{self.second})'

if __name__ == '__main__':
    p = IntPar.of(3,4)
    print(p)
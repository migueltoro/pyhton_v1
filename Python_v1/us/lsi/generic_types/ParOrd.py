'''
Created on 13 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar

from functools import total_ordering
from us.lsi.tools.Types import Comparable
from us.lsi.ejemplos_b2.Ejemplos_genericos import Par
from dataclasses import dataclass, astuple, asdict


E = TypeVar('E', bound=Comparable)
R = TypeVar('R', bound=Comparable)

   
@total_ordering
class ParOrd(Par[E,R]):
    
    def __init__(self,first:E,second:R)->None:
        super().__init__(first,second)
     
    @staticmethod
    def of(first:E,second:R) -> ParOrd[E,R]:
        return ParOrd(first,second)
    
    def __lt__(self, other:Par[E,R])->bool:
        return self.first < other.first or  (self.first == other.first and self.second < other.second)


if __name__ == '__main__':
    p4 = ParOrd.of(45,46)
    p5 = ParOrd.of(50,1)
    print(p4 >= p5)
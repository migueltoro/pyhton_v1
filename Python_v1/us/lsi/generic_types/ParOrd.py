'''
Created on 13 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar
from functools import total_ordering
from us.lsi.generic_types.Comparable import Comparable
from us.lsi.generic_types.Par import Par

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
    p4 = ParOrd.of(45,46)
    p5 = ParOrd.of(50,1)
    print(p4 >= p5)
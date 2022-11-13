'''
Created on 12 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import Generic, TypeVar
from fractions import Fraction


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


    
        
if __name__ == '__main__':
    p1 = Par.of(Fraction(4,56),45)
    p2 = Par.of(Fraction(4,56),46)
    p3 = Par.of(Fraction(4,56),45)
    print(p1 == p3)
    
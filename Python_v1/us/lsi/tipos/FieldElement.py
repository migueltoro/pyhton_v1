'''
Created on 16 ago 2022

@author: migueltoro
'''
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from us.lsi.tipos.Field import Field

E = TypeVar('E')

class FieldElement(ABC,Generic[E]):

    @abstractmethod
    def __add__(self,a: E)-> E:
        pass
    @abstractmethod
    def __truediv__(self,a:E)->E:
        pass
    @abstractmethod
    def field(self)->Field[E]:
        pass
    @abstractmethod
    def __mul__(self, a:E)->E:
        pass
    @abstractmethod
    def __neg__(self)-> E:
        pass
    @abstractmethod
    def __invert__(self)->E:
        pass
    @abstractmethod
    def __sub__(self,a: E)->E:
        pass

if __name__ == '__main__':
    pass
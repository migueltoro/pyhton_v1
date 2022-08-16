'''
Created on 16 ago 2022

@author: migueltoro
'''
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

E = TypeVar('E')


class Field(ABC,Generic[E]):
    
    @abstractmethod
    def one(self)-> E:
        pass
    @abstractmethod
    def zero(self)->E:
        pass

if __name__ == '__main__':
    pass
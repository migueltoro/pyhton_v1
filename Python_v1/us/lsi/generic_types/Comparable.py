'''
Created on 27 oct 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Protocol
from abc import abstractmethod

E = TypeVar('E', contravariant=True)

class Comparable(Protocol[E]):

    @abstractmethod
    def __eq__(self:E, other) -> bool:
        pass
    @abstractmethod
    def __lt__(self:E, other: E) -> bool:
        pass
    @abstractmethod
    def __gt__ (self, other):
        pass
    @abstractmethod
    def __ne__ (self, other):
        pass
    @abstractmethod
    def __le__(self:E, other: E) -> bool:
        pass
    @abstractmethod
    def __ge__ (self, other):
        pass

if __name__ == '__main__':
    pass
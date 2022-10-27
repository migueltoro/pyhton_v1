'''
Created on 27 oct 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Protocol
from abc import abstractmethod

E = TypeVar('E', contravariant=True)

class Comparable(Protocol[E]):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __eq__(self:E, other) -> bool:
        pass
    @abstractmethod
    def __lt__(self:E, other: E) -> bool:
        pass


if __name__ == '__main__':
    pass
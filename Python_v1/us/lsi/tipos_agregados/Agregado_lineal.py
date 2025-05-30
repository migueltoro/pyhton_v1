'''
Created on 26 ago 2024

@author: migueltoro
'''

from __future__ import annotations
from typing import Generic, TypeVar
from abc import ABC, abstractmethod


E = TypeVar('E')


class Agregado_lineal(ABC,Generic[E]):
    
    def __init__(self)->None:
        self._elements:list[E] = []
    
    @abstractmethod
    def add(self,e:E)->None:
        pass
        
    def add_all(self,ls:list[E])->None:
        for e in ls:
            self.add(e)
    
    def remove(self)->E:  
        assert len(self._elements) > 0, 'El agregado esta vacío'
        return self._elements.pop(0) 
    
    def remove_all(self)->list[E]:
        ls:list[E] = []
        while not self.is_empty():
            ls.append(self.remove())
        return ls
    
    def size(self)->int:
        return len(self._elements)
    
    def is_empty(self)->bool:
        return len(self._elements) == 0
    
    def elements(self)->list[E]:
        return self._elements

if __name__ == '__main__':
    pass
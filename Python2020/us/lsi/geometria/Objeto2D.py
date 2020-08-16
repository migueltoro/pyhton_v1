'''
Created on 21 jul. 2020

@author: migueltoro
'''

from typing import TypeVar
from abc import ABC, abstractmethod
from dataclasses import dataclass

Objeto2D = TypeVar('Objeto2D')

@dataclass(frozen=True,order=True)
class Objeto2D(ABC):
    
    @abstractmethod
    def rota(self, p, angulo) -> Objeto2D:        
        pass
    
    @abstractmethod
    def traslada(self, v) -> Objeto2D:
        pass
    
    @abstractmethod    
    def homotecia(self, p, factor) -> Objeto2D:
        pass
    
    @abstractmethod
    def proyecta_sobre_recta(self, r) -> Objeto2D:
        pass
    
    @abstractmethod
    def simetrico_con_respecto_a_recta(self, r) -> Objeto2D:
        pass

if __name__ == '__main__':
    pass
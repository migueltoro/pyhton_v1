'''
Created on 21 jul. 2020

@author: migueltoro
'''
from __future__ import annotations
from typing import TypeVar
from abc import ABC, abstractmethod
from  matplotlib.patches import Patch

Punto2D = TypeVar('Punto2D')
Vector2D = TypeVar('Vector2D')
Recta2D = TypeVar('Recta2D')


class Objeto2D(ABC):
    
    @abstractmethod
    def copy(self)-> Objeto2D:
        pass
    
    @abstractmethod
    def rota(self, p:Punto2D, angulo:float) -> Objeto2D:        
        pass
    
    @abstractmethod
    def traslada(self, v:Vector2D) -> Objeto2D:
        pass
    
    @abstractmethod    
    def homotecia(self, p:Punto2D, factor:float) -> Objeto2D:
        pass
    
    @abstractmethod
    def proyecta_sobre_recta(self, r:Recta2D) -> Objeto2D:
        pass
    
    @abstractmethod
    def simetrico_con_respecto_a_recta(self, r:Recta2D) -> Objeto2D:
        pass
    
    @property
    @abstractmethod
    def shape(self)->Patch:
        pass

if __name__ == '__main__':
    pass
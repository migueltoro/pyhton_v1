'''
Created on 2 jul 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.geometria.Vector2D import Vector2D
from matplotlib.patches import Patch 
from abc import ABC, abstractmethod

class Objeto2D(ABC):
    
    @abstractmethod 
    def copy(self)-> Objeto2D:
        pass
    
    @abstractmethod
    def rota(self, p, angulo:float) -> Objeto2D:        
        pass
    
    @abstractmethod
    def traslada(self, v:Vector2D) -> Objeto2D:
        pass
    
    @abstractmethod     
    def homotecia(self, p, factor:float) -> Objeto2D:
        pass
    
    @abstractmethod  
    def proyecta_sobre_recta(self,r) -> Objeto2D:
        pass
    
    @abstractmethod  
    def simetrico_con_respecto_a_recta(self, r) -> Objeto2D:
        pass
    
    @property
    @abstractmethod
    def shape(self)->Patch:
        pass


if __name__ == '__main__':
    pass
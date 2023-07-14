'''
Created on 2 jul 2023

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Punto2D import Punto2D

@dataclass(frozen=True,order=True)
class Recta2D:
    punto: Punto2D
    vector: Vector2D
     
    @staticmethod
    def of(p:Punto2D,v:Vector2D) -> Recta2D:
        return Recta2D(p,v)
    
    @staticmethod
    def of_puntos(p1:Punto2D,p2:Punto2D) -> Recta2D:
        return Recta2D(p1,p2.vector_to(p1))
    
    def __str__(self) -> str:
        return '({0},{1})'.format(str(self.punto),str(self.vector))
    
    def punto_en_recta(self,factor:float = 0.) -> Punto2D:
        return self.punto + self.vector * factor
    
    def paralela(self,p:Punto2D) -> Recta2D:
        return Recta2D.of(p,self.vector)
    
    def ortogonal(self,p:Punto2D) -> Recta2D:
        return Recta2D.of(p,self.vector.ortogonal)
    
    def proyecta_sobre_recta(self,p:Punto2D) -> Punto2D: 
        v1:Vector2D = self.punto.vector_to(p).proyecta_sobre(self.vector)
        return self.punto + v1
    
    def simetrico_con_respecto_a_recta(self,p:Punto2D) -> Punto2D:
        pp:Punto2D = self.proyecta_sobre_recta(p)
        return pp + pp.vector_to(p) * 2.

    
if __name__ == '__main__':
    pass
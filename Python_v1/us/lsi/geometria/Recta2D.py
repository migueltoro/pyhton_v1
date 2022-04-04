'''
Created on 16 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Punto2D import Punto2D
from dataclasses import dataclass


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

if __name__ == '__main__':
    p1 = Punto2D.origen()
    p2 = Punto2D.of(0., 1.)
    r = Recta2D.of_puntos(p1, p2)
    print(r)
    p3 = Punto2D.of(1.0,7.0)
    print(p3.proyecta_sobre_recta(r))
    print(p3.simetrico_con_respecto_a_recta(r))
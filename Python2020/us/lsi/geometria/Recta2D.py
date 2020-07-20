'''
Created on 16 jul. 2020

@author: migueltoro
'''

from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Punto2D import Punto2D
from dataclasses import dataclass
from typing import TypeVar

Recta2D = TypeVar('Recta2D')

@dataclass(frozen=True,order=True)
class Recta2D:
    punto: Punto2D
    vector: Vector2D
     
    @staticmethod
    def of_punto_vector(p:Punto2D,v:Vector2D) -> Recta2D:
        return Recta2D(p,v)
    
    @staticmethod
    def vector_of_puntos(p1:Punto2D,p2:Punto2D) -> Recta2D:
        return Recta2D(p1,p2.minus_punto(p1))
    
    def __str__(self) -> str:
        return '({0},{1})'.format(str(self.punto),str(self.vector))
    
    def punto_en_recta(self,factor:float = 0.) -> Punto2D:
        return self.punto.add_vector(self.vector.multiply(factor))
    
    def paralela(self,p:Punto2D) -> Recta2D:
        return Recta2D.of_punto_vector(p,self.vector)
    
    def ortogonal(self,p:Punto2D) -> Recta2D:
        return Recta2D.of_punto_vector(p,self.vector.ortogonal)

if __name__ == '__main__':
    p1 = Punto2D.origen()
    p2 = Punto2D.of(1., 1.)
    r = Recta2D.vector_of_puntos(p1, p2)
    print(r)
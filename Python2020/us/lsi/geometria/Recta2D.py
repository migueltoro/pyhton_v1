'''
Created on 16 jul. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Punto2D import Punto2D


@dataclass(frozen=True,order=True)
class Recta2D:
    punto: Punto2D
    vector: Vector2D
      
    @staticmethod
    def of_punto_vector(p,v):
        return Recta2D(p,v)
    
    @staticmethod
    def of_puntos(p1,p2):
        return Recta2D(p1,p2.minus_punto(p1))
    
    def punto(self,factor = 0.):
        return self.punto.add_vector(self.vector.multiply(factor))
    
    def paralela(self,p):
        return Recta2D.of_punto_vector(p,self.vector)
    
    def ortogonal(self,p):
        return Recta2D.of_punto_vector(p,self.vector.ortogonal)

if __name__ == '__main__':
    pass
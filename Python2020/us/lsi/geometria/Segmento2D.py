'''
Created on 16 jul. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Recta2D import Recta2D
from typing import TypeVar

Segmento2D = TypeVar('Segmento2D')

@dataclass(frozen=True,order=True)
class Segmento2D:
    p1: Punto2D
    p2: Punto2D
      
    @staticmethod
    def of_puntos(p1:Punto2D,p2:Punto2D) -> Segmento2D:
        return Segmento2D(p1,p2)
    
    def __str__(self):
        return '({0},{1})'.format(str(self.p1),str(self.p2))
    
    @property
    def copy(self) -> Segmento2D:
        return Segmento2D(self.p1,self.p2)
    
    @property
    def vector(self) -> Vector2D:
        return Punto2D.vector_of_puntos(self.p1,self.p2)
    
    @property
    def longitud(self) -> float:        
        return self.p1.distancia_a(self.p2)

    def rota(self,p:Punto2D,angulo) -> Segmento2D:
        return Segmento2D.vector_of_puntos(self.p1.rota(p,angulo),self.p2.rota(p,angulo))

    def traslada(self, v:Vector2D) -> Segmento2D:
        return Segmento2D.vector_of_puntos(self.p1.traslada(v), self.p2.traslada(v))
    
    def homotecia(self, p:Punto2D, factor) -> Segmento2D:
        return Segmento2D.of(self.p1.homotecia(p,factor), self.p2.homotecia(p,factor))
    
    def proyecta_sobre_recta(self,r:Recta2D) -> Segmento2D:
        return Segmento2D.of(self.p1.proyecta_sobre_recta(r), self.p2.proyecta_sobre_recta(r))
    
    def simetrico(self,r:Recta2D) -> Segmento2D:
        return Segmento2D.of(self.p1.simetrico(r), self.p2.simetrico(r))    

if __name__ == '__main__':
    print(Segmento2D.of_puntos(Punto2D.of(1., 1.),Punto2D.of(-1., -1.)))
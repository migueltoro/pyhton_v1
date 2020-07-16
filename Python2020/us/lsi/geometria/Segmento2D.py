'''
Created on 16 jul. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Punto2D import Punto2D

@dataclass(frozen=True,order=True)
class Segmento2D:
    p1: Punto2D
    p2: Punto2D
      
    @staticmethod
    def of_puntos(p1,p2):
        return Segmento2D(p1,p2)
    
    @property
    def copy(self):
        return Segmento2D(self.p1,self.p2)
    
    @property
    def vector(self) :
        return Vector2D.of_puntos(self.p1,self.p2)
    
    @property
    def longitud(self) :        
        return self.p1.distancia_a(self.p2)

    
    @property
    def rota(self,p,angulo):
        return Segmento2D.of_puntos(self.p1.rota(p,angulo),self.p2.rota(p,angulo))

    @property
    def traslada(self, v):
        return Segmento2D.of_puntos(self.p1.traslada(v), self.p2.traslada(v))
    
    @property
    def homotecia(self, p, factor) :
        return Segmento2D.of(self.p1.homotecia(p,factor), self.p2.homotecia(p,factor))
    
    @property
    def proyecta_sobre_recta(self,r) :
        return Segmento2D.of(self.p1.proyecta_sobre_recta(r), self.p2.proyecta_sobre_recta(r))
    
    @property
    def simetrico(self,r) :
        return Segmento2D.of(self.p1.simetrico(r), self.p2.simetrico(r))
    

if __name__ == '__main__':
    pass
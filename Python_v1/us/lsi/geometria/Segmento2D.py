'''
Created on 16 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.geometria.Recta2D import Recta2D
from us.lsi.geometria.Objeto2D import Objeto2D
from us.lsi.tools import Draw
from matplotlib.patches import Patch # type: ignore

@dataclass(frozen=True,order=True)
class Segmento2D(Objeto2D):
    p1: Punto2D
    p2: Punto2D
      
    @staticmethod
    def of(p1:Punto2D,p2:Punto2D) -> Segmento2D:
        return Segmento2D(p1,p2)
    
    def __str__(self):
        return '({0},{1})'.format(str(self.p1),str(self.p2))
    
    def copy(self) -> Segmento2D:
        return Segmento2D(self.p1,self.p2)
    
    @property
    def vector(self) -> Vector2D:
        return self.p1.vector_to(self.p2)
    
    @property
    def modulo(self) -> float:        
        return self.p1.distancia(self.p2)

    def rota(self,p:Punto2D,angulo) -> Segmento2D:
        return Segmento2D.of(self.p1.rota(p,angulo),self.p2.rota(p,angulo))

    def traslada(self, v:Vector2D) -> Segmento2D:
        return Segmento2D.of(self.p1.traslada(v), self.p2.traslada(v))
    
    def homotecia(self, p:Punto2D, factor) -> Segmento2D:
        return Segmento2D.of(self.p1.homotecia(p,factor), self.p2.homotecia(p,factor))
    
    def proyecta_sobre_recta(self,r:Recta2D) -> Segmento2D:
        return Segmento2D.of(r.proyecta_sobre_recta(self.p1), r.proyecta_sobre_recta(self.p2))
    
    def simetrico_con_respecto_a_recta(self,r:Recta2D) -> Segmento2D:
        return Segmento2D.of(r.simetrico_con_respecto_a_recta(self.p1), r.simetrico_con_respecto_a_recta(self.p2)) 
       
    @property
    def shape(self)->Patch:
        return Draw.shape_polygon([(self.p1.x,self.p1.y),(self.p2.x,self.p2.y)],closed=False)

if __name__ == '__main__':
    print(Segmento2D.of(Punto2D.of(1., 1.),Punto2D.of(-1., -1.)))
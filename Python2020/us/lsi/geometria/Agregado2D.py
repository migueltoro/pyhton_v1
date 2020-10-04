'''
Created on 21 jul. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from typing import TypeVar,List
from us.lsi.geometria.Objeto2D import Objeto2D
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.geometria.Recta2D import Recta2D
from us.lsi.geometria.Poligono2D import Poligono2D
from math import pi
from us.lsi.geometria.Segmento2D import Segmento2D


Agregado2D = TypeVar('Agregado2D')

@dataclass(frozen=True)
class Agregado2D(Objeto2D):
    objetos: List[Objeto2D]
    
    @staticmethod
    def of(objetos: List[Objeto2D]) -> Agregado2D:
        return Agregado2D(objetos)
    
    def __str__(self) -> str:
        return '({0})'.format(','.join(str(p) for p in self.objetos))
    
    def rota(self, p:Punto2D, angulo:float) -> Agregado2D:
        return Agregado2D.of([x.rota(p,angulo) for x in self.objetos])

    def traslada(self, v:Vector2D) -> Agregado2D:
        return Agregado2D.of([x.traslada(v) for x in self.objetos])
    
    def homotecia(self, p:Punto2D, factor:float) -> Agregado2D:
        return Agregado2D.of([x.homotecia(p,factor) for x in self.objetos])
        
    def proyecta_sobre_recta(self,r:Recta2D) -> Agregado2D:
        return Agregado2D.of([x.proyecta_sobre_recta(r) for x in self.vertices])
    
    def simetrico_con_respecto_a_recta(self, r:Recta2D) -> Agregado2D:
        return Agregado2D.of_vertices([x.simetrico(r) for x in self.objetos])
       

if __name__ == '__main__':
    p = Punto2D.of(2., 3.)
    v = Vector2D.of_xy(1., 0.)
    pol = Poligono2D.cuadrado(Punto2D.origen(),v)
    s = Segmento2D.of_puntos(Punto2D.of(1., 3.), Punto2D.of(0., 3.))
    a = Agregado2D.of([p,pol,s])
    print(a)
    print(a.rota(Punto2D.origen(),pi/2))
    print(p.rota(Punto2D.origen(),pi/2))
    print(pol.rota(Punto2D.origen(),pi/2))
    print(a.rota(Punto2D.origen(),pi/3))
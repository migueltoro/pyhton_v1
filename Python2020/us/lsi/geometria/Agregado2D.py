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
from us.lsi.geometria.Segmento2D import Segmento2D
from us.lsi.tools import Draw
from math import pi

Agregado2D = TypeVar('Agregado2D')

@dataclass(frozen=False)
class Agregado2D(Objeto2D):
    objetos: List[Objeto2D]
        
    @staticmethod
    def of(objetos: List[Objeto2D]) -> Agregado2D:
        return Agregado2D(objetos)
    
    def __str__(self) -> str:
        return '({0})'.format(','.join(str(p) for p in self.objetos))
    
    def add(self,mas_objetos:List[Objeto2D])->None:
        self.objetos = self.objetos + mas_objetos
    
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
    
    def shape(self):
        return [p.shape() for p in self.objetos]
       

if __name__ == '__main__':
    p = Punto2D.of(1., -1.)
    pr = Punto2D.of(0., 0.)
    vr = Vector2D.of_xy(1,1).multiply_double(5.)
    r = Recta2D.of(pr, vr)
    p2 = p.proyecta_sobre_recta(r)
    p3 = p.simetrico_con_respecto_a_recta(r)
    pol = Poligono2D.cuadrado(Punto2D.of(3.,4.),Vector2D.of_xy(1,-2))
    pol2 = pol.simetrico_con_respecto_a_recta(r)
    s = Segmento2D.of_puntos(pr, pr.add_vector(vr))
    a = Agregado2D.of([p,p2,p3,s,pol,pol2])
    b = a.rota(Punto2D.origen(),-pi/3)
    print(p)
    print(p2)
    print(p3)
    print(pol)
    
#    print(a.rota(Punto2D.origen(),pi/2))
#    print(p.rota(Punto2D.origen(),pi/2))
#    print(pol.rota(Punto2D.origen(),pi/2))
#    print(a.rota(Punto2D.origen(),pi/3))
    shape = a.shape()
    Draw.color='b'
    shape = shape + b.shape()
    Draw.draw_shapes(shape) 
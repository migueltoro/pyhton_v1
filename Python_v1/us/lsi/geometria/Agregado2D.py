'''
Created on 21 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.geometria.Recta2D import Recta2D
from us.lsi.geometria.Objeto2D import Objeto2D
from us.lsi.geometria.Poligono2D import Poligono2D
from us.lsi.geometria.Segmento2D import Segmento2D
from us.lsi.tools import Draw
from math import pi

@dataclass(frozen=False)
class Agregado2D(Objeto2D):
    objetos: list[Objeto2D]
        
    @staticmethod
    def of(objetos: list[Objeto2D]) -> Agregado2D:
        return Agregado2D(objetos)
    
    @staticmethod
    def empty() -> Agregado2D:
        return Agregado2D([])
    
    def __str__(self) -> str:
        return '({0})'.format(','.join(str(p) for p in self.objetos))
    
    def add_colum(self,objeto:Objeto2D)->None:
        self.objetos.append(objeto)
        
    def add_list(self,objetos:list[Objeto2D])->None:
        for e in objetos:
            self.objetos.append(e)
           
    def copy(self):
        return Agregado2D.of([e.copy for e in self.objetos])
    
    def rota(self, p:Punto2D, angulo:float) -> Agregado2D:
        return Agregado2D.of([x.rota(p,angulo) for x in self.objetos])

    def traslada(self, v:Vector2D) -> Agregado2D:
        return Agregado2D.of([x.traslada(v) for x in self.objetos])
    
    def homotecia(self, p:Punto2D, factor:float) -> Agregado2D:
        return Agregado2D.of([x.homotecia(p,factor) for x in self.objetos])

    def proyecta_sobre_recta(self,r) -> Agregado2D:
        return Agregado2D.of([x.proyecta_sobre_recta(r) for x in self.objetos])
    
    def simetrico_con_respecto_a_recta(self,r) -> Agregado2D:
        return Agregado2D.of([x.simetrico_con_respecto_a_recta(r) for x in self.objetos])
    
    @property
    def shape(self):
        return [p.shape for p in self.objetos]
       

if __name__ == '__main__':
    p = Punto2D.of(1., -1.)
    pr = Punto2D.of(0., 0.)
    vr = Vector2D.of(1,1)*5.
    r = Recta2D.of(pr, vr)
    p2 = r.proyecta_sobre_recta(p)
    p3 = r.simetrico_con_respecto_a_recta(p)
    pol = Poligono2D.cuadrado(Punto2D.of(3.,4.),Vector2D.of(1,-2))
    pol2 = pol.simetrico_con_respecto_a_recta(r)
    s = Segmento2D.of(pr, pr+vr)
    a:Agregado2D = Agregado2D.of([p,p2,p3,s,pol])
    a.add_colum(pol)
    b = a.rota(Punto2D.origen(),-pi/3)
    print(p)
    print(p2)
    print(p3)
    print(pol)

    print(a.rota(Punto2D.origen(),pi/2))
    print(p.rota(Punto2D.origen(),pi/2))
    print(pol.rota(Punto2D.origen(),pi/2))
    print(a.rota(Punto2D.origen(),pi/3))
    shape = a.shape
    Draw.color='b'
    shape = shape + b.shape
    Draw.draw_shapes(shape) 
    c = Agregado2D.empty()
    c.add_colum(p)
    print(c)
    Draw.draw_shapes(c.shape)
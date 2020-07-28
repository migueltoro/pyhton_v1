'''
Created on 16 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from math import pi 
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.geometria.Segmento2D import Segmento2D
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Recta2D import Recta2D
from us.lsi.geometria.Objeto2D import Objeto2D
from us.lsi.tools import Preconditions
from dataclasses import dataclass
from typing import TypeVar

Circulo2D = TypeVar('Circulo2D')

@dataclass(frozen=True,order=True)
class Circulo2D(Objeto2D):
    centro: Punto2D
    radio:float

    @staticmethod
    def of(centro: Punto2D, radio:float) -> Circulo2D:
        Preconditions.checkArgument(radio>=0, 'El radio debe ser mayor o igual a cero y es {0:.2f}'.format(radio))
        return Circulo2D(centro, radio)
    
    def __str__(self) -> str:
        return '({0},{1:.2f})'.format(str(self.centro),self.radio)
    
    
    @property
    def area(self) -> float:
        return pi*self.radio*self.radio

    @property
    def perimetro(self) -> float:
        return 2*pi*self.radio
        
    def rota(self, p:Punto2D, angulo:float) -> Circulo2D:        
        return Circulo2D.of(self.centro.rota(p,angulo), self.radio)
    
    def traslada(self, v: Vector2D) -> Circulo2D:
        return Circulo2D.of(self.centro.traslada(v),self.radio)
        
    def homotecia(self, p: Punto2D, factor:float) -> Circulo2D:
        return Circulo2D.of(self.centro.homotecia(p,factor), self.radio*factor)
    
    def proyecta_sobre_recta(self, r: Recta2D) -> Segmento2D:
        c = self.centro.proyectaSobre(r)
        u = r.vector.unitario()
        return Segmento2D.of_puntos(c.add_vector(u.multiply(self.radio)),c.add_vector(u.multiply(-self.radio)))
    
    def simetrico_con_respecto_a_recta(self, r: Recta2D) -> Circulo2D:
        return Circulo2D.of(self.centro.simetrico(r), self.radio)
    

if __name__ == '__main__':
    p = Punto2D.of(2.1,4.5)
    c = Circulo2D.of(p,5.6)
    print(c)
    print(c.area)
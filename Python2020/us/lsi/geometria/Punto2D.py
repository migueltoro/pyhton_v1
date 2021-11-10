'''
Created on 16 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from math import sqrt, pi
from dataclasses import dataclass
from us.lsi.geometria.Cuadrante import Cuadrante
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Objeto2D import Objeto2D
from us.lsi.tools import Draw


@dataclass(frozen=True,order=True)
class Punto2D(Objeto2D):
    x: float
    y: float
    
    @staticmethod
    def origen() -> Punto2D:
        return Punto2D(0.,0.)   
      
    @staticmethod
    def of(x:float,y:float) -> Punto2D:
        return Punto2D(x,y)
    
    @staticmethod
    def parse(linea:str) -> Punto2D:
        x,y = linea.split(',')
        return Punto2D(float(x),float(y))
    
    @staticmethod
    def of_puntos(p1:Punto2D,p2:Punto2D) -> Vector2D:
        return p2.minus_punto(p1)
    
    @property
    def copy(self: Punto2D) ->  Punto2D:
        return Punto2D(self.x,self.y)
    
    @property
    def vector(self: Punto2D) ->  Vector2D:
        return Vector2D(self.x,self.y)
    
    @property
    def distancia_al_origen(self: Punto2D) -> float:
        return self.distancia_a(Punto2D.origen())

    
    @property
    def cuadrante(self) -> Cuadrante:
        match self:
            case Punto2D(x,y) if x >=0 and y >= 0 :
                c = Cuadrante.PRIMERO
            case Punto2D(x,y) if x <=0 and y >=0 :
                c = Cuadrante.SEGUNDO
            case Punto2D(x,y) if x <=0 and y <=0 :
                c = Cuadrante.TERCERO
            case _ :
                c = Cuadrante.CUARTO
        return c
                
    
    def distancia_a(self,p:Punto2D) -> float:
        dx = self.x-p.x;
        dy = self.y-p.y
        return sqrt(dx*dx+dy*dy);
    
    def add_vector(self,v:Vector2D) -> Punto2D:
        return Punto2D.of(self.x+v.x,self.y+v.y)
    
    def minus_vector(self,v:Vector2D) -> Punto2D:
        return Punto2D.of(self.x-v.x,self.y-v.y)
    
    def minus_punto(self,p:Punto2D) -> Vector2D:
        return Vector2D.of_xy(self.x-p.x,self.y-p.y)
    
    def traslada(self,v:Vector2D) ->Punto2D:
        return self.add_vector(v)
    
    def rota(self, p:Punto2D, angulo:float) -> Punto2D:
        v = self.minus_punto(p).rota(angulo)
        return p.add_vector(v)      
    
    def homotecia(self,p:Punto2D,factor:float) -> Punto2D:
        return p.add_vector(p.minus_punto(self).multiply(factor))
    
    def proyecta_sobre_recta(self,r:'Recta2D') -> Punto2D: 
        v1 = self.minus_punto(r.punto)
        vu = r.vector.unitario
        f = v1.multiply_escalar(vu)
        v2 = vu.multiply_double(f)  
        return r.punto.add_vector(v2)
    
    def simetrico_con_respecto_a_recta(self,r:'Recta2D') -> Punto2D:
        p = self.proyecta_sobre_recta(r)
        return self.add_vector(p.minus_punto(self).multiply_double(2.))
    
    def shape(self):
        return Draw.shape_point([self.x,self.y])
    
    def __str__(self) -> str:
        return '({0:.2f},{1:.2f})'.format(self.x,self.y)

if __name__ == '__main__':
    p = Punto2D.parse('2.3,-4.55')
    p1 = Punto2D.parse('2.3,4.55')
    print(p)
    print(p.cuadrante)
    print(p1.cuadrante)
    print(p.distancia_al_origen)
    print(p.minus_punto(Punto2D.of(1., 5.)))
    print(p.rota(Punto2D.origen(),pi/2))
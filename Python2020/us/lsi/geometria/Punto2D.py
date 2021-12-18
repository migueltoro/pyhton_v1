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
from  matplotlib.patches import Patch


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
        linea = linea[1:-1]
        x,y = linea.split(',')
        return Punto2D(float(x),float(y))
    
    @property
    def copy(self: Punto2D) ->  Punto2D:
        return Punto2D(self.x,self.y)
    
    @property
    def vector(self: Punto2D) ->  Vector2D:
        return Vector2D(self.x,self.y)

    @property
    def cuadrante(self) -> Cuadrante:
        match self:
            case Punto2D(x,y) if x >=0 and y >= 0 :
                return Cuadrante.PRIMERO
            case Punto2D(x,y) if x <=0 and y >=0 :
                return Cuadrante.SEGUNDO
            case Punto2D(x,y) if x <=0 and y <=0 :
                return Cuadrante.TERCERO
            case _ :
                return Cuadrante.CUARTO
                
    
    def distancia_a(self,p:Punto2D) -> float:
        dx = self.x-p.x;
        dy = self.y-p.y
        return sqrt(dx*dx+dy*dy)
    
    @property
    def distancia_al_origen(self: Punto2D) -> float:
        return self.distancia_a(Punto2D.origen())
    
    def __add__(self,v:Vector2D) -> Punto2D:
        return Punto2D.of(self.x+v.x,self.y+v.y)
    
    def __sub__(self,v:Vector2D) -> Punto2D:
        return Punto2D.of(self.x-v.x,self.y-v.y)
    
    def vector_to(self,p:Punto2D) -> Vector2D:
        return Vector2D.of(p.x-self.x,p.y-self.y)
    
    def traslada(self,v:Vector2D) ->Punto2D:
        return self.__add__(v)
    
    def rota(self, p:Punto2D, angulo:float) -> Punto2D:
        v = self.vector_to(p).rota(angulo)
        return p + v       
    
    def homotecia(self,p:Punto2D,factor:float) -> Punto2D:
        return p + p.vector_to(self) * factor
    
    def proyecta_sobre_recta(self,r:'Recta2D') -> Punto2D: 
        v1 = r.punto.vector_to(self).proyecta_sobre(r.vector)
        return r.punto + v1
    
    def simetrico_con_respecto_a_recta(self,r:'Recta2D') -> Punto2D:
        p = self.proyecta_sobre_recta(r)
        return self + self.vector_to(p) * 2.
    @property
    def shape(self)->Patch:
        return Draw.shape_circle([self.x,self.y],radio=0.05,fill=True)
    
    def __str__(self) -> str:
        return '({0:.2f},{1:.2f})'.format(self.x,self.y)

if __name__ == '__main__':
    p = Punto2D.parse('(2.3,-4.55)')
    p1 = Punto2D.parse('(2.3,4.55)')
    p3 = Punto2D.parse('(3.,4.)')
    p4 = Punto2D.parse('(0.,0.)')
    print(p)
    print(p.cuadrante)
    print(p1.cuadrante)
    print(p.distancia_al_origen)
    print(p.vector_to(Punto2D.of(1., 5.)))
    print(p.rota(Punto2D.origen(),pi/2))
    print(p3.distancia_a(p4))
    
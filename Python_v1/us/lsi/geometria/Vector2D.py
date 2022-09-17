'''
Created on 16 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from math import sin, cos, radians, atan2, degrees, sqrt, acos
from dataclasses import dataclass
from us.lsi.tools import Preconditions


@dataclass(frozen=True,order=True)
class Vector2D:
    x: float
    y: float
      
    @staticmethod
    def of(x:float,y:float) -> Vector2D:
        return Vector2D(x,y)
    
    @staticmethod
    def parse(txt:str) -> Vector2D:
        txt = txt[1:-1]
        x,y = txt.split(',')
        return Vector2D(float(x),float(y))
    
    @staticmethod
    def of_grados(modulo:float,angulo:float) -> Vector2D:
        Preconditions.check_argument(modulo > 0, 'El modulo debe ser mayor o igual a cero y es {0:.2f}'.format(modulo))
        return Vector2D.of_radianes(modulo,radians(angulo))
    
    @staticmethod
    def of_radianes(modulo:float, angulo:float)-> Vector2D:
        Preconditions.check_argument(modulo >= 0, 'El modulo debe ser mayor o igual a cero y es {0:.2f}'.format(modulo))
        return Vector2D.of(modulo*cos(angulo),modulo*sin(angulo))       
    
    @property
    def modulo(self) -> float:
        return sqrt(self.x*self.x+self.y*self.y)
    
    @property
    def angulo(self) -> float:
        return atan2(self.y,self.x)
    
    @property
    def copy(self) -> Vector2D:
        return Vector2D(self.x,self.y)
    
    @property
    def ortogonal(self)-> Vector2D:
        return Vector2D.of(-self.y,self.x)
    
    @property
    def unitario(self)-> Vector2D:
        return Vector2D.of_radianes(1.,self.angulo)
    
    def __neg__(self)-> Vector2D:
        return Vector2D.of(-self.x, -self.y)
    
    def __add__(self,v:Vector2D)-> Vector2D:
        return Vector2D.of(self.x+v.x,self.y+v.y)
    
    def __sub__(self,v:Vector2D)-> Vector2D:
        return Vector2D.of(self.x-v.x,self.y-v.y)
    
    def rota(self, angulo:float)-> Vector2D:
        return Vector2D.of_radianes(self.modulo,self.angulo+angulo)
        
    def __mul__(self,factor:float)-> Vector2D:
        return Vector2D.of(self.x*factor,self.y*factor)
    
    def multiply_vectorial_2d(self,v:Vector2D) -> float:
        return self.x*v.y-self.y*v.x
    
    def multiply_escalar(self,v:Vector2D) -> float:
        return self.x*v.x+self.y*v.y
    
    def proyecta_sobre(self,v:Vector2D)->Vector2D:
        vu = v.unitario
        f = self.multiply_escalar(vu)
        return vu*f
    
    def angulo_con(self,v:Vector2D) -> float:
        return acos(self.multiply_escalar(v) / (self.modulo * v.modulo))
    
    def __str__(self)->str:
        return '({0:.2f},{1:.2f})'.format(self.x,self.y)

if __name__ == '__main__':
    v0 = Vector2D.parse('(-23.4,67')
    print(v0)
    v = Vector2D.of(1.,1.)
    print(v)
    print(v.modulo)
    print(degrees(v.angulo))
    print(v.ortogonal)
    print(degrees(v.angulo_con(v.ortogonal)))
    v2 = Vector2D.of(1.,0.)
    v3 = Vector2D.of(0.,1.)
    print(v2.multiply_vectorial_2d(v3))
    v3 = Vector2D.of(2.,3.)
    v4 = Vector2D.of(5.,0.)
    print(v3.proyecta_sobre(v4))
    
    
    
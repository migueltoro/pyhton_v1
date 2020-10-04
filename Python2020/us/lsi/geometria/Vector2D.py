'''
Created on 16 jul. 2020

@author: migueltoro
'''

from math import sin, cos, radians, atan2, degrees, sqrt, acos
from dataclasses import dataclass
from us.lsi.tools import Preconditions
from typing import TypeVar

Vector2D = TypeVar('Vector2D')

@dataclass(frozen=True,order=True)
class Vector2D:
    x: float
    y: float
      
    @staticmethod
    def of_xy(x:float,y:float) -> Vector2D:
        return Vector2D(x,y)
    
    @staticmethod
    def parse(text:str) -> Vector2D:
        x,y = text.split(',')
        return Vector2D(float(x),float(y))
    
    @staticmethod
    def of_grados(modulo:float,angulo:float) -> Vector2D:
        Preconditions.checkArgument(modulo > 0, 'El modulo debe ser mayor o igual a cero y es {0:.2f}'.format(modulo))
        return Vector2D.of_radianes(modulo,radians(angulo))
    
    @staticmethod
    def of_radianes(modulo:float, angulo:float)-> Vector2D:
        Preconditions.checkArgument(modulo >= 0, 'El modulo debe ser mayor o igual a cero y es {0:.2f}'.format(modulo))
        return Vector2D.of_xy(modulo*cos(angulo),modulo*sin(angulo))       
    
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
        return Vector2D.of_xy(-self.y,self.x)
    
    @property
    def unitario(self)-> Vector2D:
        return Vector2D.of_radianes(1.,self.angulo)
    
    @property
    def opuesto(self)-> Vector2D:
        return Vector2D.of_xy(-self.x, -self.y)
    
    def add_vector(self,v:Vector2D)-> Vector2D:
        return Vector2D.of_xy(self.x+v.x,self.y+v.y)
    
    def minus_vector(self,v:Vector2D)-> Vector2D:
        return Vector2D.of_xy(self.x-v.x,self.y-v.y)
    
    def rota(self, angulo:float)-> Vector2D:
        return Vector2D.of_radianes(self.modulo,self.angulo+angulo)
        
    def multiply_double(self,factor:float)-> Vector2D:
        return Vector2D.of_xy(self.x*factor,self.y*factor)
    
    def multiply_vectorial_2d(self,v:Vector2D) -> float:
        return self.x*v.y-self.y*v.x
    
    def multiply_escalar(self,v:Vector2D) -> float:
        return self.x*v.x+self.y*v.y
    
    def angulo_con(self,v:Vector2D) -> float:
        return acos(self.multiply_escalar(v) / (self.modulo * v.modulo))
    
    def __str__(self)->str:
        return '({0:.2f},{1:.2f})'.format(self.x,self.y)

if __name__ == '__main__':
    v = Vector2D.of_xy(1.,1.)
    print(v)
    print(v.modulo)
    print(degrees(v.angulo))
    print(v.ortogonal)
    print(degrees(v.angulo_con(v.ortogonal)))
    v2 = Vector2D.of_xy(1.,0.)
    v3 = Vector2D.of_xy(0.,1.)
    print(v2.multiply_vectorial_2d(v3))
    
    
    
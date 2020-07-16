'''
Created on 16 jul. 2020

@author: migueltoro
'''

from math import sin, cos, radians
from dataclasses import dataclass
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.tools import Preconditions

@dataclass(frozen=True,order=True)
class Vector2D:
    x: float
    y: float
      
    @staticmethod
    def of_xy(x,y):
        return Vector2D(x,y)
    
    @staticmethod
    def of_puntos(p1,p2):
        return p2.minus_punto(p1)
    
    @staticmethod
    def parse(text):
        x,y = text.split(',')
        return Vector2D(float(x),float(y))
    
    @staticmethod
    def of_grados(modulo,angulo):
        Preconditions.checkArgument(modulo > 0, 'El módulo debe ser mayor o igual a cero y es {0:%.2f}'.format(modulo))
        return Vector2D.of_radianes(modulo,radians(angulo))
    
    @staticmethod
    def of_radianes(modulo, angulo):
        Preconditions.checkArgument(modulo >= 0, 'El módulo debe ser mayor o igual a cero y es {0:%.2f}'.format(modulo))
        return Vector2D.of_xy(modulo*cos(angulo),modulo*sin(angulo))       
    
    @property
    def copy(self):
        return Vector2D(self.x,self.y)
    
    @property
    def as_punto(self):
        return Punto2D.of(self.x, self.y)
    
    @property
    def ortogonal(self):
        return Vector2D.of_xy(-self.y,self.x)
    
    @property
    def unitario(self):
        return Vector2D.of_radianes(1.,self.angulo)
    
    @property
    def opuesto(self):
        return Vector2D.of_xy(-self.x, -self.y)
    
    def add_vector(self,v):
        return Vector2D.of_xy(self.x+v.x,self.y+v.y)
    
    def minus_vector(self,v):
        return Vector2D.ofXY(self.x-v.x,self.y-v.y)
    
    def rota(self, angulo):
        return Vector2D.ofRadianes(self.modulo,self.angulo+angulo)
        
    def multiply_double(self,factor):
        return Vector2D.ofXY(self.x*factor,self.y*factor)

    
    def multiplica_vectorial_2d(self,v):
        return self.x*v.y-self.y*v.x
    
    def multiplica_escalar(self,v):
        return self.x*v.x+self.y*v.y
    
    def __str__(self):
        return '({0:.2f},{1:.2f})'.format(self.x,self.y)

if __name__ == '__main__':
    pass
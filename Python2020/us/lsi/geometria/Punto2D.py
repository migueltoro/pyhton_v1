'''
Created on 16 jul. 2020

@author: migueltoro
'''

from math import sqrt
from dataclasses import dataclass
from us.lsi.geometria.Cuadrante import Cuadrante
from us.lsi.geometria.Vector2D import Vector2D

@dataclass(frozen=True,order=True)
class Punto2D:
    x: float
    y: float
    
    @staticmethod
    def origen():
        return Punto2D(0.,0.)   
      
    @staticmethod
    def of(x,y):
        return Punto2D(x,y)
    
    @staticmethod
    def parse(linea):
        x,y = linea.split(',')
        return Punto2D(float(x),float(y))
    
    @property
    def copy(self):
        return Punto2D(self.x,self.y)
    
    @property
    def distancia_al_origen(self):
        return self.distancia_a(Punto2D.origen())
    
    @property
    def as_vector(self):
        return Vector2D.of_xy(self.x,self.y)
    
    @property
    def cuadrante(self):
        if self.x >=0 and self.y >= 0 :
            c = Cuadrante.PRIMERO;
        elif self.x <=0 and self.y >=0 :
            c = Cuadrante.SEGUNDO;
        elif self.x <=0 and self.y <=0 :
            c = Cuadrante.TERCERO;
        else :
            c = Cuadrante.CUARTO
        return c;
    
    def distancia_a(self,p):
        dx = self.x-p.x;
        dy = self.y-p.y
        return sqrt(dx*dx+dy*dy);
    
    def add_vector(self,v):
        return Punto2D.of(self.x+v.x,self.y+v.y)
    
    def minus_vector(self,v):
        return Punto2D.of(self.x-v.x,self.y-v.y)
    
    def minus_punto(self,p):
        return Vector2D.of_xy(self.x-p.x,self.y-p.y)
    
    def traslada(self,v):
        return self.add_vector(v)
    
    def rota(self, p, angulo):
        v = self.minus_punto(p).rota(angulo)
        return p.add(v)      
    
    def homotecia(self,p,factor):
        return p.add_vector(Vector2D.of_puntos(self,p).multiply(factor))
    
    def proyecta_sobre_recta(self,r):       
        return r.punto().add(self.minus(r.punto().proyectaSobre(r.getVector())))
    
    def simetrico_con_respecto_a_recta(self,r):
        p = self.proyecta_sobre_recta(r)
        return p.vector().multiply(2.).minus(self.vector()).punto()
    
    def __str__(self):
        return '({0:.2f},{1:.2f})'.format(self.x,self.y)

if __name__ == '__main__':
    p = Punto2D.parse('2.3,-4.55')
    print(p)
    print(p.cuadrante)
    print(p.distancia_al_origen)
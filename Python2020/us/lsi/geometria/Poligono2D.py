'''
Created on 16 jul. 2020

@author: migueltoro
'''

from math import pi
from dataclasses import dataclass
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.tools import Preconditions

@dataclass(frozen=True,order=True)
class Poligono2D:
    vertices: []
      
    @staticmethod
    def of_vertices(vertices):
        return Poligono2D(vertices)
   
    @staticmethod
    def triangulo(p1, p2, p3) :
        return Poligono2D([p1, p2, p3])
    
    @staticmethod
    def triangulo_equilatero(p1, lado):
        return Poligono2D([p1, p1.add(lado), p1.add(lado.rota(pi/3))])
    
    @staticmethod
    def cuadrado(p, lado) :
        p1 = p.add_vector(lado)
        p2 = p.add_vector(lado).add_vector(lado.ortogonal())
        p3 = p.add_vector(lado.ortogonal())
        return Poligono2D([p,p1,p2,p3])
    
    @staticmethod
    def rectangulo(p, base, altura):
        p1 = p.add_vector(base)
        p2 = p.add_vector(base).add(base.ortogonal().multiply(altura))
        p3 = p.add_vector(base.rota(pi/2).unitario().multiply(altura))
        return Poligono2D([p,p1,p2,p3])
    
    @staticmethod
    def rectanguloHorizontal(x_min, x_max, y_min, y_max) :
        p0 = Punto2D.of(x_min, y_min)
        p1 = Punto2D.of(x_max, y_min)
        p2 = Punto2D.of(x_max, y_max)
        p3 = Punto2D.of(x_min, y_max)
        return Poligono2D([p0,p1,p2,p3])
    
    def __str__(self):
        return '({0})'.format(','.join(str(p) for p in self.vertices))
           
    @property
    def copy(self):
        return Poligono2D(self.vertices)
    
    @property
    def area(self):
        n = self.getNumeroDeVertices();
        area = sum(self.diagonal(0,i).multiplica_vectorial(self.diagonal(i,i+1)) for i in range(1,n-1))
        return area/2   
    
    @property
    def numero_de_vertices(self):
        return len(self.vertices)
    
    def vertice(self,i):
        n = self.numero_de_vertices
        Preconditions.checkElementIndex(i, n)
        return self.vertices
    
    def lado(self,i) :
        n = self.numero_de_vertices
        Preconditions.checkElementIndex(i, n);
        return Vector2D.of_puntos(self.vertice(i),self.vertice((i+1)%n))
    
    def diagonal(self,i,j):
        n = self.numero_de_vertices
        Preconditions.checkElementIndex(i, n);
        Preconditions.checkElementIndex(j, n);
        return Vector2D.of_puntos(self.vertices(i),self.vertices(j))
    
    def rota(self, p, angulo) :
        return Poligono2D.of_puntos([x.rota(p,angulo) for x in self.vertices])

    def traslada(self, v) :
        return Poligono2D.of_puntos([x.traslada(v) for x in self.vertices])
    
    def homotecia(self, p, factor) :
        return Poligono2D.of_puntos([x.homotecia(p,factor) for x in self.vertices])
        
    def proyecta_sobre_recta(self,r) :
        return {x.proyecta_sobre_recta(r) for x in self.vertices}
    
    def simetrico(self, r) :
        return Poligono2D.of_puntos([x.simetrico(r) for x in self.vertices])

if __name__ == '__main__':
    pass
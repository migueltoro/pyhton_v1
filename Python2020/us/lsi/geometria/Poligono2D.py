
'''
Created on 16 jul. 2020

@author: migueltoro
'''


from math import pi
from dataclasses import dataclass
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.geometria.Recta2D import Recta2D
from us.lsi.geometria.Objeto2D import Objeto2D
from us.lsi.tools import Preconditions
from typing import List, TypeVar, Set

Poligono2D = TypeVar('Poligono2D')

@dataclass(frozen=True,order=True)
class Poligono2D(Objeto2D):
    vertices: List[Punto2D]
      
    @staticmethod
    def of_vertices(vertices: List[Punto2D]) -> Poligono2D:
        return Poligono2D(vertices)
   
    @staticmethod
    def triangulo(p1:Punto2D, p2:Punto2D, p3:Punto2D) -> Poligono2D:
        return Poligono2D([p1, p2, p3])
    
    @staticmethod
    def triangulo_equilatero(p1:Punto2D, lado:Vector2D)-> Poligono2D:
        return Poligono2D([p1, p1.add(lado), p1.add(lado.rota(pi/3))])
    
    @staticmethod
    def cuadrado(p:Punto2D,lado:Vector2D) -> Poligono2D:
        p1 = p.add_vector(lado)
        lo = lado.ortogonal
        p2 = p1.add_vector(lo)
        p3 = p.add_vector(lo)
        return Poligono2D([p,p1,p2,p3])
    
    @staticmethod
    def rectangulo(p:Punto2D, base:Vector2D, altura:float) -> Poligono2D:
        p1 = p.add_vector(base)
        p2 = p.add_vector(base).add_vector(base.ortogonal.multiply_double(altura))
        p3 = p.add_vector(base.rota(pi/2).unitario.multiply_double(altura))
        return Poligono2D([p,p1,p2,p3])
    
    @staticmethod
    def rectanguloHorizontal(x_min:Punto2D, x_max:Punto2D, y_min:Punto2D, y_max:Punto2D) -> Poligono2D:
        p0 = Punto2D.of(x_min, y_min)
        p1 = Punto2D.of(x_max, y_min)
        p2 = Punto2D.of(x_max, y_max)
        p3 = Punto2D.of(x_min, y_max)
        return Poligono2D([p0,p1,p2,p3])
    
    def __str__(self) -> str:
        return '({0})'.format(','.join(str(p) for p in self.vertices))
           
    @property
    def copy(self) -> Poligono2D:
        return Poligono2D(self.vertices)
    
    @property
    def area(self) -> float:
        n = self.numero_de_vertices
        area = sum(self.diagonal(0,i).multiply_vectorial_2d(self.diagonal(i,i+1)) for i in range(1,n-1))
        return area/2   
    
    @property
    def numero_de_vertices(self) -> int:
        return len(self.vertices)
    
    def vertice(self,i)-> Punto2D:
        n = self.numero_de_vertices
        Preconditions.checkElementIndex(i, n)
        return self.vertices[i]
    
    def lado(self,i:int) -> Vector2D:
        n = self.numero_de_vertices
        Preconditions.checkElementIndex(i, n);
        return Punto2D.of(self.vertice(i),self.vertice((i+1)%n))
    
    def diagonal(self,i:int,j:int) -> Vector2D:
        n = self.numero_de_vertices
        Preconditions.checkElementIndex(i, n);
        Preconditions.checkElementIndex(j, n);
        return Punto2D.of(self.vertice(i),self.vertice(j))
    
    def rota(self, p:Punto2D, angulo:float) -> Poligono2D:
        return Poligono2D.of_vertices([x.rota(p,angulo) for x in self.vertices])

    def traslada(self, v:Vector2D) -> Poligono2D:
        return Poligono2D.of_vertices([x.traslada(v) for x in self.vertices])
    
    def homotecia(self, p:Punto2D, factor:float) -> Poligono2D:
        return Poligono2D.of_vertices([x.homotecia(p,factor) for x in self.vertices])
        
    def proyecta_sobre_recta(self,r:Recta2D) -> Set[Punto2D]:
        return {x.proyecta_sobre_recta(r) for x in self.vertices}
    
    def simetrico_con_respecto_a_recta(self, r:Recta2D) -> Poligono2D:
        return Poligono2D.of_vertices([x.simetrico(r) for x in self.vertices])

if __name__ == '__main__':
    v = Vector2D.of_xy(1., 0.)
    pol = Poligono2D.cuadrado(Punto2D.origen(),v)
    print(pol)
    print(pol.rota(Punto2D.of(1.,1.), pi/2))
    print(pol.area)
    r = Poligono2D.rectangulo(Punto2D.of(1.,1.),v,2.)
    print(r)
    print("{0:.2f}".format(r.area))
    
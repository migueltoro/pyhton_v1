
'''
Created on 16 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from math import pi
from dataclasses import dataclass
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Punto2D import Punto2D, Objeto2D, Recta2D
from us.lsi.tools import Preconditions
from us.lsi.tools import Draw
from matplotlib.patches import Patch # type: ignore

@dataclass(frozen=True,order=True)
class Poligono2D(Objeto2D):
    vertices: list[Punto2D]
      
    @staticmethod
    def of(vertices: list[Punto2D]) -> Poligono2D:
        return Poligono2D(vertices)
   
    @staticmethod
    def triangulo(p1:Punto2D, p2:Punto2D, p3:Punto2D) -> Poligono2D:
        return Poligono2D([p1, p2, p3])
    
    @staticmethod
    def triangulo_equilatero(p1:Punto2D, lado:Vector2D)-> Poligono2D:
        return Poligono2D([p1, p1+lado, p1+lado.rota(pi/3)])
    
    @staticmethod
    def cuadrado(p:Punto2D,lado:Vector2D) -> Poligono2D:
        p1 = p+lado
        lo = lado.ortogonal
        p2 = p1+lo
        p3 = p+lo
        return Poligono2D.of([p,p1,p2,p3])
    
    @staticmethod
    def rectangulo(p:Punto2D, base:Vector2D, altura:float) -> Poligono2D:
        p1 = p+base
        p2 = p+base+base.ortogonal.unitario*altura
        p3 = p+base.rota(pi/2).unitario*altura
        return Poligono2D.of([p,p1,p2,p3])
    
    @staticmethod
    def rectanguloHorizontal(x_min:float, x_max:float, y_min:float, y_max:float) -> Poligono2D:
        p0 = Punto2D.of(x_min, y_min)
        p1 = Punto2D.of(x_max, y_min)
        p2 = Punto2D.of(x_max, y_max)
        p3 = Punto2D.of(x_min, y_max)
        return Poligono2D.of([p0,p1,p2,p3])
    
    def __str__(self) -> str:
        return '({0})'.format(','.join(str(p) for p in self.vertices))
    
    @property
    def n(self) -> int:
        return len(self.vertices)
          
    @property
    def copy(self) -> Poligono2D:
        return Poligono2D.of(self.vertices)
    
    @property
    def area(self) -> float:
        area = sum(self.diagonal(0,i).multiply_vectorial_2d(self.diagonal(0,i+1)) for i in range(1,self.n-1))
        return area/2  
    
    @property
    def perimetro(self)->float:
        return sum(self.lado(i).modulo for i in range(self.n))
    
    def vertice(self,i)-> Punto2D:
        Preconditions.check_element_index(i, self.n)
        return self.vertices[i]
    
    def lado(self,i:int) -> Vector2D:
        Preconditions.check_element_index(i, self.n);
        return self.vertice(i).vector_to(self.vertice((i+1)%self.n))
    
    def diagonal(self,i:int,j:int) -> Vector2D:
        Preconditions.check_element_index(i, self.n);
        Preconditions.check_element_index(j, self.n);
        return self.vertice(i).vector_to(self.vertice(j))
    
    def rota(self, p:Punto2D, angulo:float) -> Poligono2D:
        return Poligono2D.of([x.rota(p,angulo) for x in self.vertices])

    def traslada(self, v:Vector2D) -> Poligono2D:
        return Poligono2D.of([x.traslada(v) for x in self.vertices])
    
    def homotecia(self, p:Punto2D, factor:float) -> Poligono2D:
        return Poligono2D.of([x.homotecia(p,factor) for x in self.vertices])
        
    def proyecta_sobre_recta(self,r:Recta2D) -> Poligono2D:
        return Poligono2D.of([x.proyecta_sobre_recta(r) for x in self.vertices])
    
    def simetrico_con_respecto_a_recta(self, r:Recta2D) -> Poligono2D:
        return Poligono2D.of([x.simetrico_con_respecto_a_recta(r) for x in self.vertices])
    
    @property
    def shape(self)->Patch:
        return Draw.shape_multiline([(p.x,p.y) for p in self.vertices],closed=True)


if __name__ == '__main__':
    v = Vector2D.of(1., 0.)
    pol = Poligono2D.cuadrado(Punto2D.origen(),v)
    print(pol)
    print(pol.area)
    print(pol.perimetro)
    print(pol.rota(Punto2D.of(1.,1.), pi/2))
    r = Poligono2D.rectangulo(Punto2D.of(1.,1.),v,2.)
    print(r)
    print("{0:.2f}".format(r.area))
    
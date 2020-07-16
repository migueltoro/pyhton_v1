'''
Created on 16 jul. 2020

@author: migueltoro
'''

from math import pi 
from dataclasses import dataclass
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.geometria.Segmento2D import Segmento2D
from us.lsi.tools import Preconditions

@dataclass(frozen=True,order=True)
class Circulo2D:
    centro: Punto2D    
    radio: float

    @staticmethod
    def of(centro, radio) :
        Preconditions.checkArgument(radio>=0, 'El radio debe ser mayor o igual a cero y es {0:.2f}',radio)
        return Circulo2D(centro, radio)
    
    def __str__(self):
        return '({0},{1:.2f})'.format(str(self.centro),self.radio)
    
    @property
    def area(self) :
        return pi*self.radio*self.radio

    @property
    def perimetro(self) :
        return 2*pi*self.radio
        
    def rota(self, p, angulo) :        
        return Circulo2D.of(self.centro.rota(p,angulo), self.radio)
    
    def traslada(self, v) :
        return Circulo2D.of(self.centro.traslada(v),self.radio)
        
    def homotecia(self, p, factor) :
        return Circulo2D.of(self.centro.homotecia(p,factor), self.radio*factor)
    
    def proyecta_sobre_recta(self, r) :
        c = self.centro.proyectaSobre(r)
        u = r.vector.unitario()
        return Segmento2D.of_puntos(c.add_vector(u.multiply(self.radio)),c.add_vector(u.multiply(-self.radio)))
    
    def simetrico(self, r) :
        return Circulo2D.of(self.centro.simetrico(r), self.radio)
    

if __name__ == '__main__':
    pass
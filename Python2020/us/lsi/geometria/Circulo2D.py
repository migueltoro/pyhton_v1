'''
Created on 16 jul. 2020

@author: migueltoro
'''

from math import pi 
from dataclasses import dataclass
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.tools import Preconditions

@dataclass(frozen=True,order=True)
class Circulo2D:
    centro: Punto2D    
    radio: float

    @staticmethod
    def of(centro, radio) :
        Preconditions.checkArgument(radio>=0, 'El radio debe ser mayor o igual a cero y es {0:.2f}',radio)
        return Circulo2D(centro, radio)
    
    @property
    def area(self) :
        return pi*self.radio*self.radio

    @property
    def perimetro(self) :
        return 2*pi*self.radio

if __name__ == '__main__':
    pass
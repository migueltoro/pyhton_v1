'''
Created on 23 jul. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from datetime import time
from us.lsi.tools.Dates import parse_time, str_time
from us.lsi.coordenadas.Coordenadas3D import Coordenadas3D
from typing import TypeVar,List

Marca = TypeVar('Marca')

@dataclass(frozen=True,order=True)
class Marca:
    tiempo: time
    coordenadas: Coordenadas3D
    
    @staticmethod   
    def parse(linea: List[str]) -> Marca:
        tiempo,latitud,longitud,altitud = linea
        tiempo = parse_time(tiempo,'%H:%M:%S')
        coordenadas = Coordenadas3D.of(float(latitud), float(longitud), float(altitud)/1000)
        return Marca(tiempo, coordenadas)        
    
    def distance(self,other):
        return self.coordenadas.distance(other.coordenadas)
    
    def __str__(self):
        return '({0},{1})'.format(str_time(self.tiempo,"%H:%M:%S"),self.coordenadas) 

if __name__ == '__main__':
    linea = '00:00:00,36.74991256557405,-5.147951105609536,712.2000122070312'.split(',')
    m = Marca.parse(linea)
    print(m)

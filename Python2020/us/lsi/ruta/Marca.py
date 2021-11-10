'''
Created on 23 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import time
from us.lsi.tools.Dates import parse_time, str_time
from us.lsi.coordenadas.Coordenadas3D import Coordenadas3D

@dataclass(frozen=True,order=True)
class Marca:
    tiempo: time
    coordenadas: Coordenadas3D
    
    @staticmethod 
    def of(tiempo:time,latitud:float,longitud:float,altitud:float)->Marca:
        coordenadas = Coordenadas3D.of(latitud,longitud,altitud)
        return Marca(tiempo,coordenadas)
        
    @staticmethod   
    def parse(linea: list[str]) -> Marca:
        tiempo,latitud,longitud,altitud = linea
        tiempo = parse_time(tiempo,'%H:%M:%S')
        coordenadas = Coordenadas3D.of(float(latitud), float(longitud), float(altitud)/1000)
        return Marca(tiempo, coordenadas)        
    
    @property
    def latitud(self):
        return self.coordenadas.latitud
    
    @property
    def longitud(self):
        return self.coordenadas.longitud
    
    @property
    def altitud(self):
        return self.coordenadas.altitud
        
    def distancia(self,other):
        return self.coordenadas.distancia(other.coordenadas)
    
    def __str__(self):
        return '({0},{1:>20},{2:>20},{3:>20})'.format(str_time(self.tiempo,"%H:%M:%S"),
                                                      self.latitud,
                                                      self.longitud,
                                                      self.altitud) 

if __name__ == '__main__':
    linea = '00:00:00,36.74991256557405,-5.147951105609536,712.2000122070312'.split(',')
    m = Marca.parse(linea)
    print(m)
    m2 = Marca.of(m.tiempo,m.latitud,m.longitud,m.altitud)
    print(m2)

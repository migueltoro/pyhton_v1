'''
Created on Jun 5, 2019

@author: Miguel Toro
'''

from __future__ import annotations
from math import sqrt
from us.lsi.coordenadas.Coordenadas2D import Coordenadas2D 
from dataclasses import dataclass, asdict, astuple
from us.lsi.tools.Preconditions import checkArgument

@dataclass(frozen=True,order=True)
class Coordenadas3D:
    latitud: float
    longitud: float
    altitud: float
    
    @staticmethod
    def of(latitud:float,longitud:float,altitud:float) -> Coordenadas3D:
        checkArgument(-90<=latitud and latitud<=90,  
                      f'latitud {latitud} no es correcta')
        checkArgument(-180<=longitud and longitud<=180, 
                      f'logitud {longitud} no es correcta')
        return Coordenadas3D(latitud,longitud,altitud)
    
    @staticmethod
    def parse(text:str) -> Coordenadas3D:
        lat,long,alt = text[1:-1].split(',')
        return Coordenadas3D.of(float(lat),float(long),float(alt))
    
    @property
    def to2D(self:Coordenadas3D) -> Coordenadas2D:
        return Coordenadas2D(self.latitud,self.longitud)    
          
    def distancia(self:Coordenadas3D,other:Coordenadas3D) -> float: 
        c1 = self.to2D
        c2 = other.to2D
        d_2d = c1.distancia(c2)
        inc_alt = self.altitud-other.altitud
        return sqrt(inc_alt**2 + d_2d**2)
    
    def es_cercana(self:Coordenadas3D, c:Coordenadas3D, d:float) -> bool:
        return self.distancia(c) <= d
        
    def __str__(self:Coordenadas3D) -> str:
        return '({0},{1},{2})' \
            .format(self.latitud,self.longitud,self.altitud)
    

if __name__ == '__main__':
    sevilla = Coordenadas2D.of(37.3828300, -5.9731700)
    cadiz = Coordenadas2D.of(36.5008762, -6.2684345)
    print(sevilla.distancia(cadiz)) 
    c1 = Coordenadas3D.of(36.74991256557405,-5.147951105609536,0.7122000122070312)
    c2 = Coordenadas3D.of(36.75008556805551,-5.148005923256278,0.7127999877929688)
    d1 = c1.to2D
    d2 = c2.to2D
    print(c1)
    print(c2)
    print(d1)
    print(d2)
    print(c1.to2D.es_cercana(c2.to2D, 3.4))
    print(c1.to2D.distancia(c2.to2D))
    print(c1.distancia(c2))
    print(astuple(c1))
    print(asdict(c2))
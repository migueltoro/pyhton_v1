'''
Created on Jun 5, 2019

@author: Miguel Toro
'''

from math import sqrt
from us.lsi.coordenadas.Coordenadas2D import Coordenadas2D 
from dataclasses import dataclass, asdict, astuple
from typing import TypeVar

Coordenadas3D = TypeVar('Coordenadas3D')

@dataclass(frozen=True,order=True)
class Coordenadas3D:
    latitude: float
    longitude: float
    altitude: float
    
    @staticmethod
    def of(latitude:float,longitude:float,altitude:float) -> Coordenadas3D:
        return Coordenadas3D(latitude,longitude,altitude)
    
    @property
    def to2D(self:Coordenadas3D) -> Coordenadas2D:
        return Coordenadas2D(self.latitude,self.longitude)
        
          
    def distance(self:Coordenadas3D,other:Coordenadas3D) -> float: 
        c1 = self.to2D
        c2 = other.to2D
        d_2d = c1.distance(c2)
        inc_alt = self.altitude-other.altitude
        return sqrt(inc_alt**2 + d_2d**2)
        
    def __str__(self:Coordenadas3D) -> str:
        return '({0:>20},{1:>20},{2:>20})'.format(self.latitude,self.longitude,self.altitude)
    

if __name__ == '__main__':
    sevilla = Coordenadas2D.of(37.3828300, -5.9731700)
    cadiz = Coordenadas2D.of(36.5008762, -6.2684345)
    print(sevilla.distance(cadiz)) 
    c1 = Coordenadas3D.of(36.74991256557405,-5.147951105609536,0.7122000122070312)
    c2 = Coordenadas3D.of(36.75008556805551,-5.148005923256278,0.7127999877929688)
    d1 = c1.to2D
    d2 = c2.to2D
    print(c1)
    print(c2)
    print(d1)
    print(d2)
    print(c1.to2D.esCercana(c2.to2D, 3.4))
    print(c1.to2D.distance(c2.to2D))
    print(c1.distance(c2))
    print(astuple(c1))
    print(asdict(c2))
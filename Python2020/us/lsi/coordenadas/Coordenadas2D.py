from __future__ import annotations
from math import sin, cos, sqrt, atan2, radians
from dataclasses import dataclass, asdict, astuple
from statistics import mean
from us.lsi.tools.Preconditions import checkArgument
from typing import Iterable


@dataclass(frozen=True,order=True)
class Coordenadas2D:
    latitud: float
    longitud: float
      
    @staticmethod
    def of(latitud:float,longitud:float) -> Coordenadas2D:
        checkArgument(-90<=latitud and latitud<=90,  
                      f'latitud {latitud} no es correcta')
        checkArgument(-180<=longitud and longitud<=180, 
                      f'logitud {longitud} no es correcta')
        return Coordenadas2D(latitud,longitud)
       
    @staticmethod
    def parse(text:str) -> Coordenadas2D:
        lat,long = text[1:-1].split(',')
        return Coordenadas2D.of(float(lat),float(long))
    
    @staticmethod
    def center(coordenadas:Iterable[Coordenadas2D]) -> Coordenadas2D: 
        latMean = mean(x.latitud for x in coordenadas)
        lngMean = mean(x.longitud for x in coordenadas)
        return Coordenadas2D.of(latMean,lngMean)
    
    @property
    def copy(self)->Coordenadas2D:
        return Coordenadas2D(self.latitud,self.longitud)
     
    # a = sin^2(inclat/2) + cos(lat1) * cos(lat2) * sin^2(inclong/2)
    # d = R * 2 * atan2(sqrt(a),sqrt(1-a))

    
    def distancia(self:Coordenadas2D, other:Coordenadas2D) -> float:  
        radio_tierra = 6373.0
        latitud_a, longitud_a = radians(self.latitud), radians(self.longitud)
        latitud_b, longitud_b = radians(other.latitud), radians(other.longitud)    
        inc_lat  = latitud_b - latitud_a
        inc_long = longitud_b - longitud_a

        a = sin(inc_lat / 2)**2 + cos(latitud_a) * \
            cos(latitud_b) * sin(inc_long / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return radio_tierra * c

    
    def es_cercana(self:Coordenadas2D, c:Coordenadas2D, d:float) -> bool:
        return self.distancia(c) <= d
    
    
    def __str__(self:Coordenadas2D) -> str:
        return '({0},{1})'.format(self.latitud,self.longitud)  

if __name__ == '__main__':
    s = Coordenadas2D.parse('(37.3828300, -5.9731700)')   
    print(s)
    print(astuple(s))
    print(asdict(s))
    sevilla = Coordenadas2D(37.3828300, -5.9731700)
    cadiz = Coordenadas2D(36.5008762, -6.2684345)
    print(sevilla.distancia(cadiz)) 
    print(astuple(sevilla))
    print(asdict(cadiz))
    
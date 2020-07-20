from math import sin, cos, sqrt, atan2, radians
from dataclasses import dataclass, asdict, astuple
from us.lsi.tools.Iterable import average
from typing import TypeVar,List

Coordenadas2D = TypeVar('Coordenadas2D')

@dataclass(frozen=True,order=True)
class Coordenadas2D:
    latitude: float
    longitude: float
      
    @staticmethod
    def of(latitude:float,longitude:float) -> Coordenadas2D:
        return Coordenadas2D(latitude,longitude)
        
    
    # a = sin^2(inclat/2) + cos(lat1) * cos(lat2) * sin^2(inclong/2)
    # d = R * 2 * atan2(sqrt(a),sqrt(1-a))

    
    def distance(self:Coordenadas2D, other:Coordenadas2D) -> float:  
        radio_tierra = 6373.0
        latitud_a, longitud_a = radians(self.latitude), radians(self.longitude)
        latitud_b, longitud_b = radians(other.latitude), radians(other.longitude)    
        inc_lat  = latitud_b - latitud_a
        inc_long = longitud_b - longitud_a

        a = sin(inc_lat / 2)**2 + cos(latitud_a) * cos(latitud_b) * sin(inc_long / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return radio_tierra * c
    
    
    def esCercana(self:Coordenadas2D, c:Coordenadas2D, d:float) -> bool:
        return self.distance(c) <= d
    
    @staticmethod
    def center(coordenadas:List[Coordenadas2D]) -> Coordenadas2D: 
        averageLat = average(x.latitude for x in coordenadas)
        averageLng = average(x.longitude for x in coordenadas)
        return Coordenadas2D.of(averageLat,averageLng)
    
    
    def __str__(self:Coordenadas2D) -> str:
        return '({0},{1})'.format(self.latitude,self.longitude)
       

if __name__ == '__main__':
    sevilla = Coordenadas2D(37.3828300, -5.9731700)
    cadiz = Coordenadas2D(36.5008762, -6.2684345)
    print(sevilla.distance(cadiz)) 
    print(astuple(sevilla))
    print(asdict(cadiz))
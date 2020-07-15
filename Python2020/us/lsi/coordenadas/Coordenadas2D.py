from math import sin, cos, sqrt, atan2, radians
from dataclasses import dataclass, asdict, astuple
from us.lsi.tools.Iterable import average

@dataclass(frozen=True,order=True)
class Coordenadas2D:
    latitude: float
    longitude: float
      
    @staticmethod
    def of(latitude,longitude):
        return Coordenadas2D(latitude,longitude)
        
    
    def distance(self, other):  
        radio_tierra = 6373.0
        latitud_a, longitud_a = radians(self.latitude), radians(self.longitude)
        latitud_b, longitud_b = radians(other.latitude), radians(other.longitude)    
        inc_lat  = latitud_b - latitud_a
        inc_long = longitud_b - longitud_a

        a = sin(inc_lat / 2)**2 + cos(latitud_a) * cos(latitud_b) * sin(inc_long / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return radio_tierra * c
    
    
    def esCercana(self, c, d):
        return self.distance(c) <= d
    
    @staticmethod
    def center(coordenadas): 
        averageLat = average(x.latitude for x in coordenadas)
        averageLng = average(x.longitude for x in coordenadas)
        return Coordenadas2D.of(averageLat,averageLng)
    
    
    def __str__(self):
        return '({0},{1})'.format(self.latitude,self.longitude)
       

if __name__ == '__main__':
    sevilla = Coordenadas2D(37.3828300, -5.9731700)
    cadiz = Coordenadas2D(36.5008762, -6.2684345)
    print(sevilla.distance(cadiz)) 
    print(astuple(sevilla))
    print(asdict(cadiz))
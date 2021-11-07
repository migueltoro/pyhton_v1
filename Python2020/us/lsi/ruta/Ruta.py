'''
Created on 23 jul. 2020

@author: migueltoro
'''

from typing import TypeVar,List
from us.lsi.ruta.Marca import Marca
from us.lsi.ruta.Intervalo import Intervalo
from us.lsi.tools.File import lineas_de_csv
from us.lsi.tools import Preconditions
from us.lsi.tools import Graphics
from us.lsi.tools import Draw
from itertools import accumulate 
from us.lsi.tools.Iterable import str_iterable,limit

Ruta = TypeVar('Ruta')

class Ruta:
    
    def __init__(self, marcas:List[Marca]):
        self.marcas=marcas
    
    @staticmethod
    def ruta_of_file(fichero: str) -> Ruta:
        marcas = [Marca.parse(x) for x in lineas_de_csv(fichero, delimiter =",")]
        return Ruta(marcas);
    
    def __str__(self):
        return '\n'.join(str(m) for m in self.marcas) 

    @property
    def tiempo(self) -> float:
        n = len(self.marcas)
        return sum(self.intervalo(i).tiempo for i in range(0,n))
   
    @property
    def longitud(self) -> float:
        n = len(self.marcas)
        return sum(self.intervalo(i).longitud for i in range(0,n))
    
    @property
    def velocidad_media(self) -> float:
        return self.longitud/self.tiempo
    
    def intervalo(self, i:int) -> Intervalo:
        n = len(self.marcas)
        Preconditions.checkElementIndex(i, n+1)
        return Intervalo.of(self.marcas[i],self.marcas[(i+1)%n])
        
    @property
    def desnivel_creciente_acumulado(self) -> float:
        n = len(self.marcas)
        return sum(self.intervalo(i).longitud for i in range(0,n-1) if self.intervalo(i).desnivel > 0)
    
    @property
    def desnivel_decreciente_acumulado(self) -> float:
        n = len(self.marcas)
        return sum(self.intervalo(i).longitud for i in range(0,n-1) if self.intervalo(i).desnivel < 0)
    
    @property    
    def distance(self):
        n=len(self.marcas)
        return accumulate(self.intervalo(i).longitud if i>=0 else 0 for i in range(-1, n))
    
    @property
    def distance_y(self):
        i=0
        r=0
        n=len(self.marcas)
        yield r
        while(i<n):
            r = r + self.intervalo(i).longitud
            yield r
            i = i+1
            
    def mostrar_altitud(self):
        n = len(self.marcas)
        alturas = [self.marcas[i].coordenadas.altitude for i in range(0,n)]
        distancias = list(self.distance)
        datos = list(zip(distancias,alturas))      
        Draw.draw_multiline(datos,y_label='Altura',x_label='kms',title='Recorrido de Ronda')
        
    def mostrar_altitud_google(self,fileOut):
        alturas = [str(self.marcas[i].coordenadas.altitude) for i in range(len(self.marcas))]
        distances = list(self.distance)[:-1]
        campos = ["Posicion","Altura"]
        Graphics.lineChart(fileOut,"Ruta Ronda",campos,(distances,alturas))

if __name__ == '__main__':
    r = Ruta.ruta_of_file("../../../resources/ruta.csv");
#    print(r.marcas[:30])
#    print(str_iterable(r.distance,sep="\n",ts=lambda e:"{0:.3f}".format(e)))
    print("__________")
    print(str_iterable(r.distance_y,sep="\n",ts=lambda e:"{0:.3f}".format(e)))
    r.mostrar_altitud()
    r.mostrar_altitud_google("../../../ficheros/alturas.html")
    
    
    
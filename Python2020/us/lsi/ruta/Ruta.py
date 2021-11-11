'''
Created on 23 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.ruta.Marca import Marca
from us.lsi.ruta.Intervalo import Intervalo
from us.lsi.tools.File import lineas_de_csv
from us.lsi.tools.Preconditions import checkElementIndex
from us.lsi.tools import Graphics
from us.lsi.tools import Draw
from itertools import accumulate 
from us.lsi.tools.GraphicsMaps import  polyline, set_tipo, TipoMapa

class Ruta:
    
    def __init__(self, marcas:list[Marca]):
        self.marcas=marcas
        self.n = len(marcas)
    
    @staticmethod
    def ruta_of_file(fichero: str) -> Ruta:
        marcas = [Marca.parse(x) for x in lineas_de_csv(fichero, delimiter =",")]
        return Ruta(marcas)
    
    def __str__(self):
        return '\n'.join(str(m) for m in self.marcas) 

    @property
    def tiempo(self) -> float:
        return sum(self.intervalo(i).tiempo for i in range(0,self.n-1))
   
    @property
    def longitud(self) -> float:
        return sum(self.intervalo(i).longitud for i in range(0,self.n-1))
    
    @property
    def velocidad_media(self) -> float:
        return self.longitud/self.tiempo
    
    def intervalo(self, i:int) -> Intervalo:
        checkElementIndex(i, self.n-1)
        return Intervalo.of(self.marcas[i],self.marcas[i+1])
        
    @property
    def desnivel_creciente_acumulado(self) -> float:
        return sum(self.intervalo(i).longitud for i in range(0,self.n-1) if self.intervalo(i).desnivel > 0)
    
    @property
    def desnivel_decreciente_acumulado(self) -> float:
        return sum(self.intervalo(i).longitud for i in range(0,self.n-1) if self.intervalo(i).desnivel < 0)
            
    def mostrar_altitud(self):
        distancias = list(accumulate((self.intervalo(i).longitud for i in range(0, self.n-1)),initial=0))
        alturas = [self.marcas[i].coordenadas.altitud for i in range(0,self.n)]
        datos = list(zip(distancias,alturas))      
        Draw.draw_multiline(datos,y_label='Altura',x_label='kms',title='Recorrido de Ronda')
        
    def mostrar_altitud_google(self,fileOut):
        distancias = list(accumulate((self.intervalo(i).longitud for i in range(0, self.n-1)),initial=0))
        alturas = [str(self.marcas[i].coordenadas.altitud) for i in range(len(self.marcas))]
        campos = ["Posicion","Altura"]
        Graphics.lineChart(fileOut,"Ruta Ronda",campos,(distancias,alturas))
        
    def mostrar_mapa_google(self,fileOut:str)->None:
        set_tipo(TipoMapa.Google)
        coordenadas = [c.coordenadas.to2D for c in self.marcas]
        polyline(fileOut,coordenadas)
    
    def mostrar_mapa_bing(self,fileOut:str)->None:
        set_tipo(TipoMapa.Bing)
        coordenadas = [c.coordenadas.to2D for c in self.marcas]
        polyline(fileOut,coordenadas)

if __name__ == '__main__':
    r = Ruta.ruta_of_file("../../../resources/ruta.csv");
#    print(r.marcas[:30])
    print(r.n)
    print("__________")
    r.mostrar_altitud()
    r.mostrar_altitud_google("../../../ficheros/alturasGoogle.html")
#    r.mostrar_mapa_google("../../../ficheros/mapaGoogle.html")
    r.mostrar_mapa_bing("../../../ficheros/mapaBing.html")
    
    
    
    
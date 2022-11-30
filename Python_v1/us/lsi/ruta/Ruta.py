'''
Created on 23 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.ruta.Marca import Marca
from us.lsi.ruta.Intervalo import Intervalo
from us.lsi.tools.File import iterable_de_csv, absolute_path
from us.lsi.tools.Preconditions import check_element_index
from us.lsi.tools import Graphics
from us.lsi.tools import Draw
from itertools import accumulate 
from us.lsi.tools.GraphicsMaps import  polyline, set_tipo, TipoMapa

class Ruta:
    
    def __init__(self, marcas:list[Marca])->None:
        self.__marcas = marcas
        self.__n = len(marcas)
    
    @staticmethod
    def of_file(fichero: str) -> Ruta: 
        marcas = [Marca.parse(x) for x in iterable_de_csv(fichero)]
        return Ruta(marcas)
    
    @property
    def marcas(self)->list[Marca]:
        return self.__marcas
    
    @property
    def n(self)->int:
        return self.__n
    
    def __str__(self)->str:
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
        check_element_index(i, self.__n-1)
        return Intervalo.of(self.marcas[i],self.marcas[i+1])
        
    @property
    def desnivel_creciente_acumulado(self) -> float:
        return sum(self.intervalo(i).longitud for i in range(0,self.n-1) if self.intervalo(i).desnivel > 0)
    
    @property
    def desnivel_decreciente_acumulado(self) -> float:
        return sum(self.intervalo(i).longitud for i in range(0,self.n-1) if self.intervalo(i).desnivel < 0)
            
    def mostrar_altitud(self)->None:
        distancias = list(accumulate((self.intervalo(i).longitud for i in range(0, self.n-1)),initial=0))
        alturas = [self.marcas[i].coordenadas.altitud for i in range(0,self.n)]     
        Draw.draw_multiline(distancias,alturas,y_label='Altura',x_label='kms',title='Recorrido de Ronda')
        
    def mostrar_altitud_google(self,fileOut):
        distancias = list(accumulate((self.intervalo(i).longitud for i in range(0, self.n-1)),initial=0))
        alturas = [str(self.marcas[i].coordenadas.altitud) for i in range(len(self.marcas))]
        campos = ["Posicion","Altura"]
        Graphics.line_chart(fileOut,"Ruta Ronda",campos,(distancias,alturas))
       
    def mostrar_mapa_google(self,fileOut:str)->None:
        set_tipo(TipoMapa.Google)
        coordenadas = [c.coordenadas.to2D for c in self.marcas]
        polyline(fileOut,coordenadas)
    
    def mostrar_mapa_bing(self,fileOut:str)->None:
        set_tipo(TipoMapa.Google)
        coordenadas = [c.coordenadas.to2D for c in self.marcas]
        polyline(fileOut,coordenadas)

if __name__ == '__main__':
    print("/resources/ruta.csv")
    r = Ruta.of_file(absolute_path("/resources/ruta.csv"));
    print(r.marcas[:30])
    print(r)
    print("__________")
    r.mostrar_altitud()
#    r.mostrar_altitud_google("../../../ficheros/alturasGoogle.html")
#    r.mostrar_mapa_google("../../../ficheros/mapaGoogle.html")
#    r.mostrar_mapa_bing("../../../ficheros/mapaBing.html")
    
    
    
    
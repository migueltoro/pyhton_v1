'''
Created on 20 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.Vuelo import Vuelo
from us.lsi.aeropuertos.Aerolineas import Aerolineas
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.tools.File import lineas_de_fichero, absolute_path

class Vuelos:
    __vuelos: Vuelos
    
    def __init__(self,vuelos: list[Vuelo])->None:
        self._vuelos=vuelos
        self._codigos_vuelos = {v.codigo:v for v in self._vuelos}
    
    @staticmethod  
    def of()->Vuelos:
        return Vuelos.__vuelos

    @staticmethod  
    def lee_vuelos(fichero: str)->Vuelos:
        vuelos:list[Vuelo] = [Vuelo.parse(x) for x in lineas_de_fichero(fichero)]
        Vuelos.__vuelos = Vuelos(vuelos)
        return Vuelos.__vuelos
    @property
    def lista(self)->list[Vuelo]:
        return self._vuelos
    
    def vuelo_codigo(self,codigo:str)->Vuelo:
        return self._codigos_vuelos[codigo]
    
    def vuelo_index(self,index:int)->Vuelo:
        return self._vuelos[index]

    @property
    def size(self)->int:
        return len(self._vuelos)

    def add_vuelo(self,v:Vuelo)->None:
        self._vuelos.append(v)
    
    def remove_vuelo(self,v:Vuelo)->None:
        self._vuelos.remove(v)
        
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self._vuelos)
        return f'Vuelos\n\t{txt}'

if __name__ == '__main__':
    Aeropuertos.lee_aeropuertos(absolute_path("/resources/aeropuertos.csv"))
    Aerolineas.lee_aerolineas(absolute_path("/resources/aerolineas.csv"))
    Vuelos.lee_vuelos(absolute_path("/resources/vuelos.csv"))
    print(Vuelos.of().vuelo_codigo('MX0435'))
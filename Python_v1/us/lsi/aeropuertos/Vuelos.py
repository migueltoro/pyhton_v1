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
    
    def __init__(self,vuelos: list[Vuelo],codigos_vuelos: dict[str,Vuelo]=None)->Vuelos:
        self._vuelos=vuelos
        self._codigos_vuelos=codigos_vuelos
    
    @staticmethod  
    def get()->Vuelos:
        return Vuelos.__vuelos

    @staticmethod  
    def random(num_vuelos:int)->Vuelos:
        vuelos:list[Vuelo] = [Vuelo.random() for _ in range(0,num_vuelos)]
        return Vuelos(vuelos)

    @staticmethod  
    def lee_vuelos(fichero: str)->Vuelos:
        vuelos:list[Vuelo] = [Vuelo.parse(x) for x in lineas_de_fichero(fichero)]
        Vuelos.__vuelos = Vuelos(vuelos)
        return Vuelos.__vuelos
    
    def vuelo(self,codigo:str)->Vuelo:
        if not self._codigos_vuelos:
            self._codigos_vuelos = {v.codigo:v for v in self._vuelos}
        return self._codigos_vuelos[codigo]
    
    def get_vuelo(self,index:int)->Vuelo:
        return self._vuelos.get(index);

    def size(self)->int:
        return len(self._vuelos)

    def add_vuelo(self,v:Vuelo)->None:
        self._codigos_vuelos = None
        self._vuelos.add(v)
    
    def remove_vuelo(self,v:Vuelo)->None:
        self._codigos_vuelos = None
        self._vuelos.remove(v)
        
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self._vuelos)
        return f'Vuelos\n\t{txt}'

if __name__ == '__main__':
    Aeropuertos.lee_aeropuertos(absolute_path("/resources/aeropuertos.csv"))
    Aerolineas.lee_aerolineas(absolute_path("/resources/aerolineas.csv"))
    Vuelos.lee_vuelos(absolute_path("/resources/vuelos.csv"))
    print(Vuelos.get().vuelo('MX0435'))
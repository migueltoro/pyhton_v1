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
    __gestor_de_vuelos: Vuelos
    
    def __init__(self,vuelos: list[Vuelo])->None:
        self.__vuelos=vuelos
        self.__codigos_vuelos = {v.codigo:v for v in self.__vuelos}
    
    @staticmethod  
    def of()->Vuelos:
        return Vuelos.__gestor_de_vuelos

    @staticmethod  
    def parse(fichero: str)->Vuelos:
        vuelos:list[Vuelo] = [Vuelo.parse(x) for x in lineas_de_fichero(fichero)]
        Vuelos.__gestor_de_vuelos = Vuelos(vuelos)
        return Vuelos.__gestor_de_vuelos
    
    @property
    def todos(self)->list[Vuelo]:
        return self.__vuelos
    
    def vuelo_codigo(self,codigo:str)->Vuelo:
        return self.__codigos_vuelos[codigo]
    
    def vuelo_index(self,index:int)->Vuelo:
        return self.__vuelos[index]

    @property
    def size(self)->int:
        return len(self.__vuelos)

    def add_vuelo(self,v:Vuelo)->None:
        self.__vuelos.append(v)
    
    def remove_vuelo(self,v:Vuelo)->None:
        self.__vuelos.remove(v)
        
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self.__vuelos)
        return f'Vuelos\n\t{txt}'

if __name__ == '__main__':
    Aeropuertos.parse(absolute_path("/aeropuertos/aerolineas.csv"))
    Aerolineas.parse(absolute_path("/aerolineas/ocupaciones_vuelos.csv"))
    Vuelos.parse(absolute_path("/aerolineas/__vuelos.csv"))
    print(Vuelos.of().vuelo_codigo('MX0435'))
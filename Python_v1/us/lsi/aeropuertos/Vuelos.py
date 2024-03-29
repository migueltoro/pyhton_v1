'''
Created on 20 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.Vuelo import Vuelo
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.tools.File import lineas_de_fichero, root_project, absolute_path
from typing import Optional

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
    
    def vuelo_codigo(self,codigo:str)->Optional[Vuelo]:
        return self.__codigos_vuelos.get(codigo,None)
    
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
    espacio_aereo_root = root_project()
    a = Aeropuertos.parse(absolute_path("/aeropuertos/aeropuertos.csv",espacio_aereo_root))
    Vuelos.parse(absolute_path("/aeropuertos/vuelos.csv",espacio_aereo_root))
    print(Vuelos.of().vuelo_codigo('MX0435'))
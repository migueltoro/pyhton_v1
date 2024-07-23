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
    __gestor_de_vuelos: Optional[Vuelos] = None
    
    def __init__(self,file:str)->None:
        self.__vuelos= [Vuelo.parse(x) for x in lineas_de_fichero(file,encoding='Windows-1252')]
        self.__codigos_vuelos = {v.codigo:v for v in self.__vuelos}

    @staticmethod  
    def of(file:str=absolute_path("aeropuertos/vuelos.csv"))->Vuelos:
        if Vuelos.__gestor_de_vuelos is None:
            Vuelos.__gestor_de_vuelos = Vuelos(file)
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
    a = Aeropuertos.of()
    v = Vuelos.of()
    print(v.vuelo_codigo('MX0435'))
    
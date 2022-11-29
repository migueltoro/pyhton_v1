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
    __vuelos_class: Vuelos
    
    def __init__(self,vuelos: list[Vuelo])->None:
        self.__vuelos=vuelos
        self.__codigos_vuelos = {v.codigo:v for v in self.__vuelos}
    
    @staticmethod  
    def of()->Vuelos:
        return Vuelos.__vuelos_class

    @staticmethod  
    def of_file(fichero: str)->Vuelos:
        vuelos:list[Vuelo] = [Vuelo.of_file(x) for x in lineas_de_fichero(fichero)]
        Vuelos.__vuelos_class = Vuelos(vuelos)
        return Vuelos.__vuelos_class
    
    @property
    def lista(self)->list[Vuelo]:
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
    Aeropuertos.of_file(absolute_path("/resources/aeropuertos.csv"))
    Aerolineas.of_file(absolute_path("/resources/ocupaciones_vuelos.csv"))
    Vuelos.of_file(absolute_path("/resources/__vuelos.csv"))
    print(Vuelos.of().vuelo_codigo('MX0435'))
'''
Created on 20 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.Vuelo import Vuelo
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from datetime import date
from typing import Optional

class Vuelos:
    
    __gestor_de_vuelos: Optional[Vuelos] = None
    
    
    def __init__(self,file:str)->None:
        vuelos:list[Vuelo] = [Vuelo.parse(x) for x in lineas_de_fichero(file)]
        self.__lista_de_vuelos = vuelos

    @staticmethod
    def of(file:str=absolute_path("aeropuertos/vuelos.csv"))->Vuelos:
        if Vuelos.__gestor_de_vuelos is None:
            Vuelos.__gestor_de_vuelos = Vuelos(file)
        return Vuelos.__gestor_de_vuelos

    
    @property
    def todos(self):
        return self.__lista_de_vuelos
    
    def vuelo_index(self,i:int)->Vuelo:
        assert 0 <= i < len(self.__lista_de_vuelos), f'Índice {i} fuera de rango [0,{len(self.__lista_de_vuelos)-1}]'
        return self.__lista_de_vuelos[i]
    
    @property
    def size(self)->int:
        return len(self.__lista_de_vuelos)
    
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self.__lista_de_vuelos)
        return f'Ocupaciones_vuelos\n\t{txt}'


if __name__ == '__main__':
    oc = Vuelos.of()
    print(oc.vuelo_index(0))
    print(list(oc for oc in oc.todos if oc.fecha_salida == date(2020,6,8)))
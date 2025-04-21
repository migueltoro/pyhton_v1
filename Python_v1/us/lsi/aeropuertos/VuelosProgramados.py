'''
Created on 20 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.VueloProgramado import VueloProgramado
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.tools.File import lineas_de_fichero, root_project, absolute_path
from typing import Optional

class VuelosProgramados:
    
    __gestor_de_vuelos: Optional[VuelosProgramados] = None
    
    def __init__(self,file:str)->None:
        self.__vuelos= [VueloProgramado.parse(x) for x in lineas_de_fichero(file,encoding='Windows-1252')]
        self.__codigos_vuelos = {v.codigo:v for v in self.__vuelos}

    @staticmethod  
    def of(file:str=absolute_path("aeropuertos/vuelos.csv"))->VuelosProgramados:
        if VuelosProgramados.__gestor_de_vuelos is None:
            VuelosProgramados.__gestor_de_vuelos = VuelosProgramados(file)
        return VuelosProgramados.__gestor_de_vuelos
    
    @property
    def todos(self)->list[VueloProgramado]:
        return self.__vuelos
    
    def vuelo_codigo(self,codigo:str)->Optional[VueloProgramado]:
        return self.__codigos_vuelos.get(codigo,None)
    
    def vuelo_index(self,index:int)->VueloProgramado:
        return self.__vuelos[index]

    @property
    def size(self)->int:
        return len(self.__vuelos)

    def add_vuelo(self,v:VueloProgramado)->None:
        self.__vuelos.append(v)
    
    def remove_vuelo(self,v:VueloProgramado)->None:
        self.__vuelos.remove(v)
        
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self.__vuelos)
        return f'VuelosProgramados\n\t{txt}'

    

if __name__ == '__main__':
    espacio_aereo_root = root_project()
    a = Aeropuertos.of()
    v = VuelosProgramados.of()
    print(v.vuelo_codigo('MX0435'))
    
'''
Created on 20 ago 2022

@author: migueltoro
'''
from __future__ import annotations
from us.lsi.aeropuertos.Aeropuerto import Aeropuerto
from us.lsi.tools.File import lineas_de_fichero, absolute_path, root_project
from us.lsi.tools.Iterable import grouping_set
from typing import Optional


class Aeropuertos:
    
    __gestor_de_aeropuertos:Optional[Aeropuertos] = None
    
    def __init__(self,file:str)->None:
        self.__aeropuertos= [Aeropuerto.parse(x) for x in lineas_de_fichero(file,encoding='Windows-1252')]  
        self.__codigos_aeropuertos: dict[str,Aeropuerto] = {a.codigo:a for a in self.__aeropuertos}
        self.__ciudad_de_aeropuerto: dict[str,str] = {a.codigo:a.ciudad for a in self.__aeropuertos}
        self.__aeropuertos_en_ciudad:dict[str,set[Aeropuerto]] = grouping_set(self.__aeropuertos,lambda a: a.ciudad)
    
    @staticmethod
    def of(file:str=absolute_path("aeropuertos/aeropuertos.csv"))->Aeropuertos:
        if Aeropuertos.__gestor_de_aeropuertos is None:
            Aeropuertos.__gestor_de_aeropuertos = Aeropuertos(file)
        return Aeropuertos.__gestor_de_aeropuertos
       
    def add_aeropuerto(self, a: Aeropuerto)->None:
        self.__aeropuertos.append(a)
    
    def remove_aeropuerto(self, a: Aeropuerto)->None:
        self.__aeropuertos.remove(a)

    def aeropuerto_codigo(self,codigo: str)->Optional[Aeropuerto]:
        return self.__codigos_aeropuertos.get(codigo,None)
    
    def ciudad_de_aeropuerto(self, codigo:str)->Optional[str]:
        return self.__ciudad_de_aeropuerto.get(codigo,None)
    
    def aeropuertos_en_ciudad(self,ciudad:str)->set[Aeropuerto]: 
        return self.__aeropuertos_en_ciudad[ciudad]
    
    @property
    def size(self)->int:
        return len(self.__aeropuertos)
    
    @property
    def todos(self)->list[Aeropuerto]:
        return self.__aeropuertos
    
    def aeropuerto(self,codigo:str)->Optional[Aeropuerto]:
        return self.__codigos_aeropuertos.get(codigo,None)
    
    def aeropuerto_index(self,i:int)->Aeropuerto:
        assert 0 <= i < len(self.__aeropuertos), f'Índice {i} fuera de rango [0,{len(self.__aeropuertos)-1}]'
        return self.__aeropuertos[i]
    
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self.__aeropuertos)
        return f'Aeropuertos\n\t{txt}'
    
    

if __name__ == '__main__':
    espacio_aereo_root = root_project()
#    a = Aeropuertos.parse(absolute_path("aeropuertos/aeropuertos.csv"))
#    print(a)
#    print(a.aeropuerto_index(0))
    print(Aeropuertos.of().aeropuerto_index(0))
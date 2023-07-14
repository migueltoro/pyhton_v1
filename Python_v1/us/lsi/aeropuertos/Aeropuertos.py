'''
Created on 20 ago 2022

@author: migueltoro
'''
from __future__ import annotations
from us.lsi.aeropuertos.Aeropuerto import Aeropuerto
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from us.lsi.tools.Iterable import grouping_set


class Aeropuertos:
    __gestor_de_aeropuertos: Aeropuertos
    
    def __init__(self,aeropuertos:list[Aeropuerto])->None:
        self.__aeropuertos= aeropuertos
        self.__codigos_aeropuertos: dict[str,Aeropuerto] = {a.codigo:a for a in self.__aeropuertos}
        self.__ciudad_de_aeropuerto: dict[str,str] = {a.codigo:a.ciudad for a in aeropuertos}
        self.__aeropuertos_en_ciudad:dict[str,set[Aeropuerto]] = grouping_set(self.__aeropuertos,lambda a: a.ciudad)
    
    @staticmethod
    def of()->Aeropuertos:
        return Aeropuertos.__gestor_de_aeropuertos
    
    @staticmethod  
    def of_file(fichero:str)-> Aeropuertos:
        aeropuertos:list[Aeropuerto] = [Aeropuerto.parse(x) for x in lineas_de_fichero(fichero,encoding='Windows-1252')]  
        Aeropuertos.__gestor_de_aeropuertos = Aeropuertos(aeropuertos)
        return Aeropuertos.__gestor_de_aeropuertos
    
    def add_aeropuerto(self, a: Aeropuerto)->None:
        self.__aeropuertos.append(a)
    
    def remove_aeropuerto(self, a: Aeropuerto)->None:
        self.__aeropuertos.remove(a)

    def aeropuerto_codigo(self,codigo: str)->Aeropuerto:
        return self.__codigos_aeropuertos[codigo]
    
    def ciudad_de_aeropuerto(self, codigo:str)->str:
        return self.__ciudad_de_aeropuerto[codigo]
    
    def aeropuertos_en_ciudad(self,ciudad:str)->set[Aeropuerto]: 
        return self.__aeropuertos_en_ciudad[ciudad]
    
    @property
    def size(self)->int:
        return len(self.__aeropuertos)
    
    @property
    def todos(self)->list[Aeropuerto]:
        return self.__aeropuertos
    
    def aeropuerto_index(self,i:int)->Aeropuerto:
        return self.__aeropuertos[i]
    
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self.__aeropuertos)
        return f'Aeropuertos\n\t{txt}'
    

if __name__ == '__main__':
    a = Aeropuertos.of_file(absolute_path("/resources/aeropuertos.csv"))
    print(a)
    print(a.aeropuerto_index(0))
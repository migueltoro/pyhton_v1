'''
Created on 20 ago 2022

@author: migueltoro
'''
from __future__ import annotations
from us.lsi.aeropuertos.Aeropuerto import Aeropuerto
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from us.lsi.tools.Iterable import grouping_set


class Aeropuertos:
    __aeropuertos: Aeropuertos
    
    def __init__(self,aeropuertos:list[Aeropuerto])->None:
        self._aeropuertos= aeropuertos
        self._codigos_aeropuertos: dict[str,Aeropuerto] = {a.codigo:a for a in self._aeropuertos}
        self._ciudad_de_aeropuerto: dict[str,str] = {a.codigo:a.ciudad for a in aeropuertos}
        self._aeropuertos_en_ciudad:dict[str,set[Aeropuerto]] = grouping_set(self._aeropuertos,lambda a: a.ciudad)
    
    @staticmethod
    def of()->Aeropuertos:
        return Aeropuertos.__aeropuertos
    
    @staticmethod  
    def lee_aeropuertos(fichero:str)-> Aeropuertos:
        aeropuertos:list[Aeropuerto] = [Aeropuerto.parse(x) for x in lineas_de_fichero(fichero,encoding='Windows-1252')]  
        Aeropuertos.__aeropuertos = Aeropuertos(aeropuertos)
        return Aeropuertos.__aeropuertos
    
    def add_aeropuerto(self, a: Aeropuerto)->None:
        self._aeropuertos.append(a)
    
    def remove_aeropuerto(self, a: Aeropuerto)->None:
        self._aeropuertos.remove(a)

    def aeropuerto(self,codigo: str)->Aeropuerto:
        return self._codigos_aeropuertos[codigo]
    
    def ciudad_de_aeropuerto(self, codigo:str)->str:
        return self._ciudad_de_aeropuerto[codigo]
    
    def aeropuertos_en_ciudad(self,ciudad:str)->set[Aeropuerto]: 
        return self._aeropuertos_en_ciudad[ciudad]
    
    def size(self)->int:
        return len(self._aeropuertos)
    
    @property
    def lista(self)->list[Aeropuerto]:
        return self._aeropuertos
    
    def aeropuerto_index(self,i:int)->Aeropuerto:
        return self._aeropuertos[i]
    
    def aeropuerto_codigo(self,codigo:str)->Aeropuerto:
        return self._codigos_aeropuertos[codigo]
    
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self._aeropuertos)
        return f'Aeropuertos\n\t{txt}'
    

if __name__ == '__main__':
    a = Aeropuertos.lee_aeropuertos(absolute_path("/resources/aeropuertos.csv"))
    print(a)
    print(a.aeropuerto_index(0))
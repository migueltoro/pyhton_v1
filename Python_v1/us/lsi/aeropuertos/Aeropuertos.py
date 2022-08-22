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
    
    def __init__(self,aeropuertos:list[Aeropuerto],codigos_aeropuertos:dict[str,Aeropuerto]=None,
            ciudad_de_aeropuerto:dict[str,str]=None,
            aeropuertos_en_ciudad:dict[str,set[Aeropuerto]]=None)->Aeropuertos:
        self._aeropuertos= aeropuertos
        self._codigos_aeropuertos=codigos_aeropuertos,
        self._ciudad_de_aeropuerto = ciudad_de_aeropuerto
        self._aeropuertos_en_ciudad = aeropuertos_en_ciudad
    
    @staticmethod  
    def get()->Aeropuertos: 
        return Aeropuertos.__aeropuertos
    
    @staticmethod  
    def lee_aeropuertos(fichero:str)-> Aeropuertos:
        aeropuertos:list[Aeropuerto] = [Aeropuerto.parse(x) for x in lineas_de_fichero(fichero,encoding='Windows-1252')]  
        Aeropuertos.__aeropuertos =  Aeropuertos(aeropuertos)
        return Aeropuertos.__aeropuertos
    
    def add_aeropuerto(self, a: Aeropuerto)->None:
        self._aeropuertos_en_ciudad = None
        self._ciudad_de_aeropuerto = None
        self._codigosAeropuertos = None
        self._aeropuertos.add(a)
    
    def remove_aeropuerto(self, a: Aeropuerto)->None:
        self._aeropuertos_en_ciudad = None
        self._ciudad_de_aeropuerto = None
        self._codigosAeropuertos = None
        self._aeropuertos.remove(a)

    
    def aeropuerto(self,codigo: str)->Aeropuerto:
        if not self._codigosAeropuertos:
            self._codigosAeropuertos = {a.codigo:a for a in self._aeropuertos}
        return self._codigosAeropuertos[codigo]
    
    def ciudad_de_aeropuerto(self, codigo:str)->str:
        if not self._ciudad_de_aeropuerto:
            self._ciudad_de_aeropuerto = {a.codigo:a.ciudad for a in self._aeropuertos}
        return self._ciudad_de_aeropuerto[codigo]
    
    def aeropuertos_en_ciudad(self,ciudad:str)->set[str]: 
        if not self._aeropuertosEnCiudad:
            self.aeropuertosEnCiudad = grouping_set(self._aeropuertos,lambda a: a.ciudad)
        return self._aeropuertosEnCiudad[ciudad]
    
    @property
    def size(self)->int:
        return len(self._aeropuertos)
    
    @property
    def aeropuertos(self):
        return self._aeropuertos
    
    def get_aeropuerto(self,i:int)->Aeropuerto:
        return self._aeropuertos[i]
    
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self._aeropuertos)
        return f'Aeropuertos\n\t{txt}'
    

if __name__ == '__main__':
    Aeropuertos.lee_aeropuertos(absolute_path("/resources/aeropuertos.csv"))
    print(Aeropuertos.get())
    print(Aeropuertos.get().get_aeropuerto(0))
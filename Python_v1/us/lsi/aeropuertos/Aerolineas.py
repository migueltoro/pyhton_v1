'''
Created on 20 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.Aerolinea import Aerolinea
from typing import Optional
from us.lsi.tools.File import lineas_de_fichero,  absolute_path, encoding

class Aerolineas:  
    __gestor_de_aerolineas: Optional[Aerolineas] = None
    
    def __init__(self,file:str)->None:
        aerolineas:list[Aerolinea] = [Aerolinea.parse(x) for x in lineas_de_fichero(file, encoding='Windows-1252')]
        self.__aerolineas = aerolineas
        self.__codigos_aerolineas = {a.codigo:a for a in aerolineas}
        
    @staticmethod
    def of(file:str= absolute_path("aeropuertos/aerolineas.csv"))->Aerolineas:
        if Aerolineas.__gestor_de_aerolineas is None:
            Aerolineas.__gestor_de_aerolineas = Aerolineas(file)
        return Aerolineas.__gestor_de_aerolineas

    @property
    def todas(self)->list[Aerolinea]:
        return self.__aerolineas

    def aerolinea_codigo(self,codigo:str)->Optional[Aerolinea]:
        return self.__codigos_aerolineas.get(codigo,None)
    
    @property
    def size(self):
        return len(self.__aerolineas)
    
    def aerolinea_index(self,i:int)->Aerolinea:
        assert 0 <= i < len(self.__aerolineas), f'Índice {i} fuera de rango [0,{len(self.__aerolineas)-1}]'
        return list(self.__aerolineas)[i]
    
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self.__aerolineas)
        return f'Aerolineas\n\t{txt}'


if __name__ == '__main__':
    print(encoding(absolute_path("aeropuertos/aerolineas.csv")))
    '''
    espacio_aereo_root = root_project()
    print(encoding(absolute_path("aeropuertos/aerolineas.csv",espacio_aereo_root)))
    a = Aerolineas.parse(absolute_path("aeropuertos/aerolineas.csv",espacio_aereo_root))
    print(a)
    '''
    print(Aerolineas.of().aerolinea_index(0))
    
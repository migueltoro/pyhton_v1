'''
Created on 20 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.Aerolinea import Aerolinea
from us.lsi.tools.File import lineas_de_fichero, absolute_path, encoding

class Aerolineas:  
    __gestor_de_aerolineas: Aerolineas
    
    def __init__(self,ocupaciones_vuelos:list[Aerolinea])->None:
        self.__aerolineas = ocupaciones_vuelos
        self.__codigos_aerolineas = {a.codigo:a for a in ocupaciones_vuelos}
        
    @staticmethod
    def of()->Aerolineas:
        return Aerolineas.__gestor_de_aerolineas
               
    @staticmethod
    def parse(fichero:str)->Aerolineas:
        datos: list[Aerolinea] = [Aerolinea.parse(x) for x in lineas_de_fichero(fichero,encoding='Windows-1252')]
        Aerolineas.__gestor_de_aerolineas = Aerolineas(datos)
        return Aerolineas.__gestor_de_aerolineas

    @property
    def todas(self)->list[Aerolinea]:
        return self.__aerolineas

    def aerolinea_codigo(self,codigo:str)->Aerolinea:
        return self.__codigos_aerolineas[codigo]
    
    @property
    def size(self):
        return len(self.__aerolineas)
    
    def aerolinea_index(self,i:int)->Aerolinea:
        return self.__aerolineas[i]
    
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self.__aerolineas)
        return f'Aerolineas\n\t{txt}'


if __name__ == '__main__':
    print(encoding(absolute_path("/aeropuertos/aerolineas.csv")))
    a = Aerolineas.parse(absolute_path("/aeropuertos/aerolineas.csv"))
    print(a)
    print(a.aerolinea_index(0))
    
'''
Created on 20 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.Ocupacion_vuelo import Ocupacion_vuelo
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from datetime import date
from typing import Optional

class Ocupaciones_vuelos:
    __gestor_de_ocupaciones_vuelos: Optional[Ocupaciones_vuelos] = None
    
    
    def __init__(self,file:str)->None:
        ocupaciones:list[Ocupacion_vuelo] = [Ocupacion_vuelo.parse(x) for x in lineas_de_fichero(file)]
        self.__lista_ocupaciones_vuelos = ocupaciones

    @staticmethod
    def of(file:str=absolute_path("aeropuertos/ocupacionesVuelos.csv"))->Ocupaciones_vuelos:
        if Ocupaciones_vuelos.__gestor_de_ocupaciones_vuelos is None:
            Ocupaciones_vuelos.__gestor_de_ocupaciones_vuelos = Ocupaciones_vuelos(file)
        return Ocupaciones_vuelos.__gestor_de_ocupaciones_vuelos

    
    @property
    def todas(self):
        return self.__lista_ocupaciones_vuelos
    
    def ocupacion_index(self,i:int)->Ocupacion_vuelo:
        return self.__lista_ocupaciones_vuelos[i]
    
    @property
    def size(self)->int:
        return len(self.__lista_ocupaciones_vuelos)
    
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self.__lista_ocupaciones_vuelos)
        return f'Ocupaciones_vuelos\n\t{txt}'


if __name__ == '__main__':
    oc = Ocupaciones_vuelos.of()
    print(oc.ocupacion_index(0))
    print(list(oc for oc in oc.todas if oc.fecha_salida == date(2020,6,8)))
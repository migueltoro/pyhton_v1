'''
Created on 20 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.Vuelos import Vuelos
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.aeropuertos.Aerolineas import Aerolineas
from us.lsi.aeropuertos.Ocupacion_vuelo import Ocupacion_vuelo
from us.lsi.tools.File import lineas_de_fichero, root_project, absolute_path
from datetime import date

class Ocupaciones_vuelos:
    __gestor_de_ocupaciones_vuelos: Ocupaciones_vuelos
    
    
    def __init__(self,ocupaciones:list[Ocupacion_vuelo])->None:
        self.__lista_ocupaciones_vuelos = ocupaciones

    @staticmethod
    def of()->Ocupaciones_vuelos:
        return Ocupaciones_vuelos.__gestor_de_ocupaciones_vuelos

    @staticmethod
    def parse(fichero:str)->Ocupaciones_vuelos:
        r:list[Ocupacion_vuelo] = [Ocupacion_vuelo.parse(x) for x in lineas_de_fichero(fichero)]
        Ocupaciones_vuelos.__gestor_de_ocupaciones_vuelos = Ocupaciones_vuelos(r)
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
    espacio_aereo_root = root_project()
    Aeropuertos.parse(absolute_path("/aeropuertos/aeropuertos.csv",espacio_aereo_root))
    Aerolineas.parse(absolute_path("/aeropuertos/aerolineas.csv",espacio_aereo_root))
    Vuelos.parse(absolute_path("/aeropuertos/vuelos.csv",espacio_aereo_root))
    oc = Ocupaciones_vuelos.parse(absolute_path("/aeropuertos/ocupacionesVuelos.csv",espacio_aereo_root))
    print(oc.ocupacion_index(0))
    print(list(oc for oc in oc.todas if oc.fecha_salida == date(2020,6,8)))
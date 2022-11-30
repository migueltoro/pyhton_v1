'''
Created on 20 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.Vuelos import Vuelos
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.aeropuertos.Aerolineas import Aerolineas
from us.lsi.aeropuertos.Ocupacion_vuelo import Ocupacion_vuelo
from us.lsi.tools.File import lineas_de_fichero,absolute_path
from datetime import date

class Ocupaciones_vuelos:
    __ocupaciones_vuelos_class: Ocupaciones_vuelos
    
    
    def __init__(self,ocupaciones:list[Ocupacion_vuelo])->None:
        self.__lista_ocupaciones_vuelos = ocupaciones

    @staticmethod
    def of()->Ocupaciones_vuelos:
        return Ocupaciones_vuelos.__ocupaciones_vuelos_class

    @staticmethod
    def of_file(fichero:str)->Ocupaciones_vuelos:
        r:list[Ocupacion_vuelo] = [Ocupacion_vuelo.parse(x) for x in lineas_de_fichero(fichero)]
        Ocupaciones_vuelos.__ocupaciones_vuelos_class = Ocupaciones_vuelos(r)
        return Ocupaciones_vuelos.__ocupaciones_vuelos_class
    
    @property
    def lista(self):
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
    Aeropuertos.of_file(absolute_path("/resources/aeropuertos.csv"))
    Aerolineas.of_file(absolute_path("/resources/__ocupaciones_vuelos_class.csv"))
    Vuelos.of_file(absolute_path("/resources/vuelos.csv"))
    oc = Ocupaciones_vuelos.of_file(absolute_path("/resources/ocupacionesVuelos.csv"))
    print(oc.ocupacion_index(0))
    print(list(oc for oc in oc.lista if oc.fecha_salida == date(2020,6,8)))
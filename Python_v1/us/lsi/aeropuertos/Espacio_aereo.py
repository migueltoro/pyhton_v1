'''
Created on 5 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.VuelosProgramados import VuelosProgramados
from us.lsi.aeropuertos.Aerolineas import Aerolineas
from us.lsi.aeropuertos.Vuelos import Vuelos
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.tools.File import absolute_path
from typing import Optional

class Espacio_aereo:
    
    __gestor_de_espacio_aereo: Optional[Espacio_aereo] = None
    
    def __init__(self,aerolineas: Aerolineas,vuelos_programados: VuelosProgramados,vuelos: Vuelos,
                 aeropuertos: Aeropuertos)->None:
        self.__aerolineas: Aerolineas = aerolineas
        self.__vuelos_programados: VuelosProgramados = vuelos_programados
        self.__vuelos: Vuelos = vuelos
        self.__aeropuertos: Aeropuertos = aeropuertos
    
    @staticmethod
    def of(faeropuertos:str=absolute_path("aeropuertos/aeropuertos.csv"),
            faerolineas:str=absolute_path("aeropuertos/aerolineas.csv"),
            fvuelos:str=absolute_path("aeropuertos/vuelosProgramados.csv"),
            focupaciones_vuelos:str=absolute_path("aeropuertos/vuelos.csv"))->Espacio_aereo:
        aeropuertos = Aeropuertos.of(faeropuertos)
        aerolineas = Aerolineas.of(faerolineas)
        vuelos =  VuelosProgramados.of(fvuelos)
        ocupaciones_vuelos = Vuelos.of(focupaciones_vuelos)       
        return Espacio_aereo(aerolineas,vuelos,ocupaciones_vuelos,aeropuertos)
 
    @property
    def aerolineas(self)->Aerolineas:
        return self.__aerolineas
    
    @property
    def vuelos_programados(self)->VuelosProgramados:
        return self.__vuelos_programados
    
    @property
    def vuelos(self)->Vuelos:
        return self.__vuelos
    
    @property
    def aeropuertos(self)-> Aeropuertos:
        return self.__aeropuertos   

if __name__ == '__main__':
    pass
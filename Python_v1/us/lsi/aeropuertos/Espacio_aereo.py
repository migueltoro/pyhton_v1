'''
Created on 5 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.Vuelos import Vuelos
from us.lsi.aeropuertos.Aerolineas import Aerolineas
from us.lsi.aeropuertos.Ocupaciones_vuelos import Ocupaciones_vuelos
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.tools.File import absolute_path

class Espacio_aereo:
    
    __espacio_aereo_class = None
    
    def __init__(self,aerolineas: Aerolineas,vuelos: Vuelos,ocupaciones_vuelos: Ocupaciones_vuelos,
                 aeropuertos: Aeropuertos)->None:
        self.__aerolineas: Aerolineas = aerolineas
        self.__vuelos: Vuelos = vuelos
        self.__ocupaciones_vuelos: Ocupaciones_vuelos = ocupaciones_vuelos
        self.__aeropuertos: Aeropuertos = aeropuertos
    
    @staticmethod
    def of(): 
        if Espacio_aereo.__espacio_aereo_class is None:
            Espacio_aereo.__espacio_aereo_class = Espacio_aereo.of_files()
        return Espacio_aereo.__espacio_aereo_class
    
    @staticmethod
    def of_files(faeropuertos:str=absolute_path("/aeropuertos/aeropuertos.csv"),
        faerolineas:str=absolute_path("/aeropuertos/aerolineas.csv"),         
        fvuelos:str = absolute_path("/aeropuertos/vuelos.csv"),
        focupaciones_vuelos:str =absolute_path("/aeropuertos/ocupacionesVuelos.csv"))->Espacio_aereo:
        aeropuertos = Aeropuertos.parse(faeropuertos)
        aerolineas = Aerolineas.parse(faerolineas)
        vuelos =  Vuelos.parse(fvuelos)
        ocupaciones_vuelos = Ocupaciones_vuelos.parse(focupaciones_vuelos)
        
        return Espacio_aereo(aerolineas,vuelos,ocupaciones_vuelos,aeropuertos)
 
    @property
    def aerolineas(self)->Aerolineas:
        return self.__aerolineas
    
    @property
    def vuelos(self)->Vuelos:
        return self.__vuelos
    
    @property
    def ocupaciones_vuelos(self)->Ocupaciones_vuelos:
        return self.__ocupaciones_vuelos
    
    @property
    def aeropuertos(self)-> Aeropuertos:
        return self.__aeropuertos
    

if __name__ == '__main__':
    pass
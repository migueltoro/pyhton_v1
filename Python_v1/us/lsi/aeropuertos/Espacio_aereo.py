'''
Created on 5 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.Vuelos import Vuelos
from us.lsi.aeropuertos.Aerolineas import Aerolineas
from us.lsi.aeropuertos.OcupacionesVuelos import OcupacionesVuelos
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.tools.File import absolute_path

class Espacio_aereo:
    
    __espacio_aereo = None
    
    def __init__(self,aerolineas: Aerolineas,vuelos: Vuelos,ocupaciones_vuelos: OcupacionesVuelos,
                 aeropuertos: Aeropuertos)->None:
        self.aerolineas: Aerolineas = aerolineas
        self.vuelos: Vuelos = vuelos
        self.ocupaciones_vuelos: OcupacionesVuelos = ocupaciones_vuelos
        self.aeropuertos: Aeropuertos = aeropuertos
    
    @staticmethod
    def of(): 
        if Espacio_aereo.__espacio_aereo is None:
            Espacio_aereo.__espacio_aereo = Espacio_aereo.espacio_aereo()
        return Espacio_aereo.__espacio_aereo
    
    @staticmethod
    def espacio_aereo(faeropuertos:str=absolute_path("/resources/aeropuertos.csv"),
        faerolineas:str=absolute_path("/resources/aerolineas.csv"),         
        fvuelos:str = absolute_path("/resources/vuelos.csv"),
        focupaciones_vuelos:str =absolute_path("/resources/ocupacionesVuelos.csv"))->Espacio_aereo:
        aeropuertos = Aeropuertos.lee_aeropuertos(faeropuertos)
        aerolineas = Aerolineas.lee_aerolineas(faerolineas)
        vuelos =  Vuelos.lee_vuelos(fvuelos)
        ocupaciones_vuelos = OcupacionesVuelos.lee_ocupaciones(focupaciones_vuelos)
        
        return Espacio_aereo(aerolineas,vuelos,ocupaciones_vuelos,aeropuertos)

if __name__ == '__main__':
    pass
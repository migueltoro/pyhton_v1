'''
Created on 20 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.Vuelos import Vuelos
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.aeropuertos.Aerolineas import Aerolineas
from us.lsi.aeropuertos.OcupacionVuelo import OcupacionVuelo
from us.lsi.tools.File import lineas_de_fichero,absolute_path
from datetime import date

class OcupacionesVuelos:
    __ocupaciones_vuelos: OcupacionesVuelos
    
    
    def __init__(self,ocupaciones:list[OcupacionVuelo])->None:
        self._lista_ocupaciones_vuelos = ocupaciones

    @staticmethod
    def of()->OcupacionesVuelos:
        return OcupacionesVuelos.__ocupaciones_vuelos

    @staticmethod
    def lee_ocupaciones(fichero:str)->OcupacionesVuelos:
        r:list[OcupacionVuelo] = [OcupacionVuelo.parse(x) for x in lineas_de_fichero(fichero)]
        OcupacionesVuelos.__ocupaciones_vuelos = OcupacionesVuelos(r)
        return OcupacionesVuelos.__ocupaciones_vuelos
    
    @property
    def lista(self):
        return self._lista_ocupaciones_vuelos
    
    def ocupacion(self,i:int)->OcupacionVuelo:
        return self._lista_ocupaciones_vuelos[i]
    
    @property
    def size(self)->int:
        return len(self._lista_ocupaciones_vuelos)
    
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self._lista_ocupaciones_vuelos)
        return f'OcupacionesVuelos\n\t{txt}'


if __name__ == '__main__':
    Aeropuertos.lee_aeropuertos(absolute_path("/resources/aeropuertos.csv"))
    Aerolineas.lee_aerolineas(absolute_path("/resources/aerolineas.csv"))
    Vuelos.lee_vuelos(absolute_path("/resources/vuelos.csv"))
    oc = OcupacionesVuelos.lee_ocupaciones(absolute_path("/resources/ocupacionesVuelos.csv"))
    print(oc.ocupacion(0))
    print(list(oc for oc in oc.lista if oc.fecha_salida == date(2020,6,8)))
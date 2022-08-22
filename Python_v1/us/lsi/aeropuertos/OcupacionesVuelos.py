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
import random
from datetime import date

class OcupacionesVuelos:
    __ocupaciones_vuelos = None
    
    def __init__(self,ocupaciones:list[OcupacionVuelo])->OcupacionesVuelos:
        self._ocupaciones_vuelos = ocupaciones
    
    @staticmethod
    def get()->OcupacionesVuelos:
        return OcupacionesVuelos.__ocupaciones_vuelos

    @staticmethod
    def random(num_ocupaciones:int, anyo:int)->OcupacionesVuelos:
        n = Vuelos.get().size();
        r = [OcupacionVuelo.random(Vuelos.get().get(random.randint(0,n)), anyo) for _ in range(num_ocupaciones)]
        OcupacionesVuelos.__ocupaciones_vuelos =  OcupacionesVuelos(r);
        return OcupacionesVuelos.__ocupacionesVuelos

    @staticmethod
    def lee_ocupaciones(fichero:str)->OcupacionesVuelos:
        r:list[OcupacionVuelo] = [OcupacionVuelo.parse(x) for x in lineas_de_fichero(fichero)]
        OcupacionesVuelos.__ocupaciones_vuelos = OcupacionesVuelos(r)
        return OcupacionesVuelos.__ocupaciones_vuelos

    @property
    def ocupaciones(self):
        return self._ocupaciones_vuelos
    
    def get_ocupacion(self,i:int)->OcupacionVuelo:
        return self._ocupaciones_vuelos[i]
    
    def size(self)->int:
        return len(self._ocupaciones_vuelos)
    
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self._ocupaciones_vuelos)
        return f'OcupacionesVuelos\n\t{txt}'


if __name__ == '__main__':
    Aeropuertos.lee_aeropuertos(absolute_path("/resources/aeropuertos.csv"))
    Aerolineas.lee_aerolineas(absolute_path("/resources/aerolineas.csv"))
    Vuelos.lee_vuelos(absolute_path("/resources/vuelos.csv"))
    OcupacionesVuelos.lee_ocupaciones(absolute_path("/resources/ocupacionesVuelos.csv"))
    print(OcupacionesVuelos.get().get_ocupacion(0))
    print(OcupacionVuelo.random(Vuelos.get().get_vuelo(10),2022))
    print(list(oc for oc in OcupacionesVuelos.get().ocupaciones if oc.fecha_salida == date(2020,6,8)))
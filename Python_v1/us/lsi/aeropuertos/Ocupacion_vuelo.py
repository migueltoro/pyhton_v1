'''
Created on 19 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import time,datetime,date
from calendar import day_name
from us.lsi.aeropuertos.Vuelo import Vuelo
from us.lsi.aeropuertos.Vuelos import Vuelos
from us.lsi.aeropuertos.Aerolineas import Aerolineas
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.tools.File import absolute_path

days = list(day_name)

@dataclass(frozen=True)
class Ocupacion_vuelo:
    codigo_vuelo:str
    fecha:datetime
    num_pasajeros: int
    
    @staticmethod 
    def of(codigoVuelo:str,fecha:datetime,numPasajeros: int)->Ocupacion_vuelo:
        return Ocupacion_vuelo(codigoVuelo,fecha,numPasajeros)
    
    @staticmethod 
    def parse(text:str)->Ocupacion_vuelo:
        campos:list[str] = text.split(",")
        codigo_vuelo:str = campos[0]
        t:time = Vuelos.of().vuelo_codigo(codigo_vuelo).hora
        d:date = datetime.strptime(campos[1],"%Y-%m-%d %H:%M:%S")
        fecha:datetime = datetime.combine(d, t)
        num_pasajeros:int = int(campos[2])       
        return Ocupacion_vuelo.of(codigo_vuelo,fecha,num_pasajeros)
    
    @property
    def vuelo(self)->Vuelo:
        return Vuelos.of().vuelo_codigo(self.codigo_vuelo)
    
    @property
    def llegada(self)->datetime: 
        vuelo:Vuelo = Vuelos.of().vuelo_codigo(self.codigo_vuelo)
        return datetime.combine(self.fecha.date(),vuelo.hora)+vuelo.duracion
    
    @property
    def fecha_salida(self)->date:
        return self.fecha.date()
    
    @property
    def hora_salida(self)->time: 
        return self.fecha.time();

    def __str__(self):
        return f'{self.codigo_vuelo},{self.fecha.strftime("%Y-%m-%d %H:%M:%S")},{self.num_pasajeros}'

if __name__ == '__main__':
    Aeropuertos.parse(absolute_path("/resources/aeropuertos.csv"))
    Aerolineas.parse(absolute_path("/resources/aerolineas.csv"))
    Vuelos.parse(absolute_path("/resources/vuelos.csv"))
    oc = Ocupacion_vuelo.parse('MX0435,2020-11-24 01:04:00,57')
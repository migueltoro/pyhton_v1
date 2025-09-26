'''
Created on 19 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import time,datetime,date
from calendar import day_name
from us.lsi.aeropuertos.Aerolineas import Aerolineas
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.aeropuertos.VueloProgramado import VueloProgramado
from us.lsi.aeropuertos.VuelosProgramados import VuelosProgramados
from us.lsi.tools.File import absolute_path
from us.lsi.tools.Optional import optional_get

days = list(day_name)


@dataclass(frozen=True)
class Vuelo:
    """
    Represents a flight that is an instance of the scheduled flight with the given code

    Attributes:
        codigo (str): The unique code identifying the scheduled flight.
        fecha (datetime): The date and time of the flight.
        num_pasajeros (int): The number of passengers on the flight.
        
    The flight's scheduled data will be provided by the associated scheduled flight.
    """
    codigo:str
    fecha:datetime
    num_pasajeros: int
    
    @staticmethod 
    def of(codigo:str,fecha:datetime,numPasajeros: int)->Vuelo:
        return Vuelo(codigo,fecha,numPasajeros)
    
    @staticmethod 
    def parse(text:str)->Vuelo:
        campos:list[str] = text.split(",")
        codigo:str = campos[0]
        fecha:datetime = datetime.strptime(campos[1],"%Y-%m-%d %H:%M:%S")
        num_pasajeros:int = int(campos[2])       
        return Vuelo.of(codigo,fecha,num_pasajeros)
   
    @property
    def vuelo_programado(self)->VueloProgramado:
        return optional_get(VuelosProgramados.of().vuelo_codigo(self.codigo))
    
    @property
    def llegada(self)->datetime: 
        vuelo:VueloProgramado = optional_get(VuelosProgramados.of().vuelo_codigo(self.codigo))
        return datetime.combine(self.fecha.date(),vuelo.hora)+vuelo.duracion
       
    @property
    def fecha_salida(self)->date:
        return self.fecha.date()
    
    @property
    def hora_salida(self)->time: 
        return self.fecha.time();

    def __str__(self)->str:
        return f'{self.codigo},{self.fecha.strftime("%Y-%m-%d %H:%M:%S")},{self.num_pasajeros}'

if __name__ == '__main__':
    Aeropuertos.of(absolute_path("aeropuertos/aeropuertos.csv"))
    Aerolineas.of(absolute_path("aeropuertos/aerolineas.csv"))
#    Vuelos.of(absolute_path("aeropuertos/vuelos.csv"))
    oc = Vuelo.parse('MX0435,2020-11-24 01:04:00,57')
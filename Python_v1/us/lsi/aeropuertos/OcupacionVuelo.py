'''
Created on 19 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import time,datetime,date,timedelta
from calendar import day_name
from us.lsi.aeropuertos.Vuelo import Vuelo
from us.lsi.aeropuertos.Vuelos import Vuelos
from us.lsi.aeropuertos.Aerolineas import Aerolineas
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
import random
from us.lsi.tools.Iterable import find_first, iterate
from us.lsi.tools.File import absolute_path

days = list(day_name)

@dataclass(frozen=True)
class OcupacionVuelo:
    codigo_vuelo:str
    fecha:datetime
    num_pasajeros: int
    
    @staticmethod 
    def of(codigoVuelo:str,fecha:datetime,numPasajeros: int)->OcupacionVuelo:
        return OcupacionVuelo(codigoVuelo,fecha,numPasajeros)
    
    @staticmethod 
    def parse(text:str)->OcupacionVuelo:
        campos:list[str] = text.split(",");
        codigo_vuelo:str = campos[0];
        t:time = Vuelos.get().vuelo(codigo_vuelo).hora
        d:date = datetime.strptime(campos[1],"%Y-%m-%d %H:%M:%S")
        fecha:datetime = datetime.combine(d, t)
        numPasajeros:int = int(campos[2])       
        return OcupacionVuelo.of(codigo_vuelo,fecha,numPasajeros)
    
    @staticmethod 
    def random(v:Vuelo, anyo:int)->OcupacionVuelo:
        codigo_vuelo:str = v.codigo
        np:int = v.numPlazas
        t:time = v.hora
        dw:int = v.diaSemana
        d:date = find_first(iterate(date(anyo,1,1),lambda dt: dt+timedelta(days=1)),lambda dt:dt.weekday() == dw)         
        d = d+timedelta(days=7*random.randint(0,53)) #53 semanas en un anyo
        fecha:datetime = datetime.combine(d, t)
        num_pasajeros:int = random.randint(0,np) if np>0 else 0
        return OcupacionVuelo.of(codigo_vuelo,fecha,num_pasajeros)
    
    @property
    def vuelo(self)->Vuelo:
        return Vuelos.get().vuelo(self.codigoVuelo)
    
    @property
    def llegada(self)->datetime: 
        vuelo:Vuelo = Vuelos.get().vuelo(self.codigoVuelo)
        return date(self.fecha.date(),vuelo.time())+ vuelo.duracion
    
    @property
    def fecha_salida(self)->date:
        return self.fecha.date()
    
    @property
    def hora_salida(self)->time: 
        return self.fecha.time();

    def __str__(self):
        return f'{self.codigo_vuelo},{self.fecha.strftime("%Y-%m-%d %H:%M:%S")},{self.num_pasajeros}'

if __name__ == '__main__':
    Aeropuertos.lee_aeropuertos(absolute_path("/resources/aeropuertos.csv"))
    Aerolineas.lee_aerolineas(absolute_path("/resources/aerolineas.csv"))
    Vuelos.lee_vuelos(absolute_path("/resources/vuelos.csv"))
    oc = OcupacionVuelo.parse('MX0435,2020-11-24 01:04:00,57')
'''
Created on 19 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import time,timedelta,datetime
from calendar import day_name
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.tools.Iterable import str_iter

days = list(day_name)

@dataclass(frozen=True)
class Vuelo:
    codigo_aerolinea: str
    numero: str
    codigo_destino: str
    codigo_origen: str
    precio: float
    num_plazas: int    
    duracion: timedelta
    hora: time
    dia_semana: int
   
    @staticmethod 
    def parse(text: str) -> Vuelo:
        campos: list[str] = text.split(",")
        codigo: str = campos[0]
        numero: str = campos[1]
        codigo_destino: str = campos[2]
        codigo_origen: str = campos[3]
        precio: float = float(campos[4])
        num_plazas: int = int(campos[5])
        duracion: timedelta = timedelta(minutes = int(campos[6]))
        hora: time = datetime.strptime(campos[7], "%H:%M").time()
        dia_semana: int = days.index(campos[8].capitalize());
        return Vuelo.of(codigo,numero,codigo_destino,codigo_origen,precio,num_plazas,duracion,hora,dia_semana)
    
    

    @staticmethod 
    def of(codigo_aerolinea: str, numero: str, codigo_destino: str, codigo_origen: str, 
           precio: float, numPlazas: int, duracion: timedelta, hora: time, diaSemana: int) -> Vuelo:
        return Vuelo(codigo_aerolinea,numero,codigo_destino,codigo_origen,precio,numPlazas,duracion,hora,diaSemana) 
    
    @property
    def ciudad_destino(self)-> str:
        return Aeropuertos.of().ciudad_de_aeropuerto(self.codigo_destino)
    
    @property
    def ciudad_origen(self)-> str:
        return Aeropuertos.of().ciudad_de_aeropuerto(self.codigo_origen) 
    
    @property
    def codigo(self)-> str:
        return self.codigo_aerolinea+self.numero
    
    def __str__(self):
        return  "{0},{1},{2},{3},{4:.2f},{5:d},{6:d},{7},{8}".format(
            self.codigo_aerolinea,
            self.numero,
            self.codigo_destino,
            self.codigo_origen,
            self.precio,
            self.num_plazas,
            int(self.duracion/timedelta(minutes=1)),
            time.strftime(self.hora,"%H:%M"),
            days[self.dia_semana])  
        
        

if __name__ == '__main__':
    v1: Vuelo = Vuelo.parse("TP,0705,BER,KTW,294,170,287,14:50,FRIDAY")
    print(v1)
    print(str_iter(day_name))
    print(datetime.strptime("FRIDAY",'%A').strftime('%A'))
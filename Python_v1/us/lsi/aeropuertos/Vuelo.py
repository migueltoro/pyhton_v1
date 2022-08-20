'''
Created on 19 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import time,timedelta,datetime
from calendar import day_name
import random
from us.lsi.aeropuertos.Aerolineas import Aerolineas
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos

days = list(day_name)

@dataclass(frozen=True)
class Vuelo:
    codigo_aerolinea: str
    numero: str
    codigo_destino: str
    codigo_origen: str
    precio: float
    numPlazas: int    
    duracion: timedelta
    hora: time
    diaSemana: int
   
    @staticmethod 
    def parse(text: str) -> Vuelo:
        campos: list[str] = text.split(",")
        codigo: str = campos[0]
        numero: str = campos[1]
        codigo_destino: str = campos[2]
        codigo_origen: str = campos[3]
        precio: float = float(campos[4])
        numPlazas: int = int(campos[5])
        duracion: timedelta = timedelta(minutes = int(campos[6]))
        hora: time = datetime.strptime(campos[7], "%H:%M").time()
        diaSemana: int = days.index(campos[8].capitalize());
        return Vuelo.of(codigo,numero,codigo_destino,codigo_origen,precio,numPlazas,duracion,hora,diaSemana)
    
    @staticmethod 
    def random()-> Vuelo: 
        e: int = random.randint(0,Aerolineas.get().size());
        codigo: str = Aerolineas.get().get(e).codigo();
        numero: str = f'{random.randint(0,1000):4d}'
        ad: int = random.randint(0,Aeropuertos.get().size())
        codigo_destino: str = Aeropuertos.get().get(ad).codigo()
        while True:
            ao: int = random.randint(0,Aeropuertos.get().size())
            if ao != ad:
                break
        codigo_origen:str = Aeropuertos.get().get(ao).codigo();
        precio:float = random.uniform(0, 100)
        numPlazas: int = random.randint(0,300);
        duracion: timedelta= timedelta(minutes=random.randint(0,360))
        hora: time = time(random.randint(0,24),random.randint(0,60));
        diaSemana: int = random.randint(7)
        return Vuelo.of(codigo,numero,codigo_destino,codigo_origen,precio,numPlazas,duracion,hora,diaSemana);

    @staticmethod 
    def of(codigo_aerolinea: str, numero: str, codigo_destino: str, codigo_origen: str, 
           precio: float, numPlazas: int, duracion: timedelta, hora: time, diaSemana: int) -> Vuelo:
        return Vuelo(codigo_aerolinea,numero,codigo_destino,codigo_origen,precio,numPlazas,duracion,hora,diaSemana) 
    
    @property
    def ciudad_destino(self)-> str:
        return Aeropuertos.get().ciudadDeAeropuerto(self.codigoDestino);
    
    @property
    def ciudad_origen(self)-> str:
        return Aeropuertos.get().ciudadDeAeropuerto(self.codigoOrigen); 
    
    @property
    def codigo(self)-> str:
        return self.codigo_aerolinea+self.numero;

    
    def __str__(self):
        return  "{0},{1},{2},{3},{4:.2f},{5:d},{6:d},{7},{8}".format(
            self.codigo_aerolinea,
            self.numero,
            self.codigo_destino,
            self.codigo_origen,
            self.precio,
            self.numPlazas,
            int(self.duracion/timedelta(minutes=1)),
            time.strftime(self.hora,"%H:%M"),
            days[self.diaSemana])  

if __name__ == '__main__':
    v1: Vuelo = Vuelo.parse("TP,0705,BER,KTW,294,170,287,14:50,FRIDAY")
    print(v1)
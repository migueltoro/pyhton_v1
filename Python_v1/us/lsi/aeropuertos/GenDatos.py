'''
Created on 5 nov 2022

@author: migueltoro

'''

import random
from us.lsi.aeropuertos.VueloProgramado import VueloProgramado
from us.lsi.aeropuertos.VuelosProgramados import VuelosProgramados
from us.lsi.aeropuertos.Aerolineas import Aerolineas
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.aeropuertos.Vuelo import Vuelo
from datetime import date, time, datetime, timedelta
from us.lsi.tools.Iterable import first, iterate
from typing import Optional

def vuelo_programado_random()-> VueloProgramado: 
    e: int = random.randint(0,Aerolineas.of().size())
    codigo: str = Aerolineas.of().aerolinea_index(e).codigo
    numero: str = f'{random.randint(0,1000):04d}'
    ad: int = random.randint(0,Aeropuertos.of().size)
    codigo_destino: str = Aeropuertos.of().aeropuerto_index(ad).codigo
    while True:
        ao: int = random.randint(0,Aeropuertos.of().size)
        if ao != ad:
            break
    codigo_origen:str = Aeropuertos.of().aeropuerto_index(ao).codigo
    precio:float = random.uniform(0, 100)
    num_plazas: int = random.randint(0,300);
    duracion: timedelta= timedelta(minutes=random.randint(0,360))
    hora: time = time(random.randint(0,23),random.randint(0,59));
    dia_semana: int = random.randint(0,6)
    return VueloProgramado.of(codigo,numero,codigo_destino,codigo_origen,precio,num_plazas,duracion,hora,dia_semana)


def vuelos_programados_random(num_vuelos:int)->list[VueloProgramado]:
    vuelos_programados:list[VueloProgramado] = [vuelo_programado_random() for _ in range(0,num_vuelos)]
    return vuelos_programados

def vuelo_random(v:VueloProgramado, anyo:int)->Vuelo:
    codigo_vuelo:str = v.codigo_vuelo_programado
    np:int = v.num_plazas
    t:time = v.hora
    dw:int = v.dia_semana
    d:Optional[date] = first(iterate(date(anyo,1,1),lambda dt: dt+timedelta(days=1)),lambda dt:dt.weekday() == dw)
    d2:date
    if d is not None:
        d2 = d         
    d2 = d2+timedelta(days=7*random.randint(0,53)) #53 semanas en un anyo
    fecha:datetime = datetime.combine(d2, t)
    num_pasajeros:int = random.randint(0,np) if np>0 else 0
    return Vuelo.of(codigo_vuelo,fecha,num_pasajeros)

def vuelos_random(num_ocupaciones:int, anyo:int)->list[Vuelo]:
    n = VuelosProgramados.of().size
    r = [vuelo_random(VuelosProgramados.of().vuelo_index(random.randint(0,n)), anyo) for _ in range(num_ocupaciones)]
    return r


if __name__ == '__main__':
    pass
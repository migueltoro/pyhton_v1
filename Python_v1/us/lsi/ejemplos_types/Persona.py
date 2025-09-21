'''
Created on 3 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass, astuple, asdict
from enum import Enum, auto
import locale
from us.lsi.ejemplos_types.Direccion import Direccion
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class Horoscopo(Enum):
    Acuario = auto()
    Piscis = auto()
    Aries = auto()
    Tauro = auto()
    Geminis = auto()
    Cancer = auto()
    Leo = auto()
    Virgo = auto()
    Libra = auto()
    Escorpio = auto()
    Sagitario = auto()
    Capricornio = auto()
  
    
horoscopos_con_fechas:list[tuple[str,tuple[int,int]]] = [
    ("Acuario", (1, 20)),
    ("Piscis", (2, 19)),
    ("Aries", (3, 21)),
    ("Tauro", (4, 21)),
    ("Géminis", (5, 21)),
    ("Cáncer", (6, 21)),
    ("Leo", (7, 23)),
    ("Virgo", (8, 23)),
    ("Libra", (9, 23)),
    ("Escorpio", (10, 23)),
    ("Sagitario", (11, 22)),
    ("Capricornio", (12, 22))
]

@dataclass(frozen=True,order=True)
class Persona:
    apellidos: str
    nombre: str
    dni: str
    fecha_de_nacimiento: datetime
    telefono: str
    direccion:Direccion
    
    def __post_init__(self):
        assert len(self.apellidos.strip()) > 0, f'Los apellidos no pueden estar en blanco'
        assert len(self.nombre.strip()) > 0, f'El nombre no puede estar en blanco'
        assert self.fecha_de_nacimiento < datetime.now(), f'La fecha debe estar en el pasado'
        assert Persona._check_dni(self.dni), f'El dni no es correcto'
        
    @staticmethod
    def of(apellidos: str, nombre: str, dni: str, fecha_de_nacimiento: datetime, telefono:str,direccion:Direccion) -> Persona:        
        return Persona(apellidos, nombre, dni, fecha_de_nacimiento, telefono, direccion)
    
    @staticmethod
    def parse(text:str, ft:str = "%Y-%m-%d %H:%M")->Persona:
        partes:list[str] = text.split(',')       
        apellidos: str =  partes[0].strip()
        nombre: str =  partes[1].strip()
        dni: str = partes[2].strip() 
        fecha_de_nacimiento: datetime = datetime.strptime(partes[3].strip(), ft)
        telefono: str = partes[4].strip()
        direccion: Direccion = Direccion.parse(partes[5].strip())
        return Persona.of(apellidos, nombre, dni, fecha_de_nacimiento, telefono, direccion)
    
    @staticmethod
    def parse_list(ls:list[str], ft:str = "%Y-%m-%d %H:%M")->Persona:
        apellidos: str =  ls[0].strip()
        nombre: str =  ls[1].strip()
        dni: str = ls[2].strip() 
        fecha_de_nacimiento: datetime = datetime.strptime(ls[3].strip(), ft)
        telefono: str = ls[4].strip()
        direccion: Direccion = Direccion.parse(ls[5].strip())
        return Persona.of(apellidos, nombre, dni, fecha_de_nacimiento, telefono, direccion)
    
    
    @staticmethod
    def _check_dni(text:str)->bool: # type: ignore[empty-body]
        ...
        
    @property
    def edad(self)->int: # type: ignore[empty-body]
        ... 
    
    @property
    def siguiente_cumple(self)->date: # type: ignore[empty-body]
        ...          
    @property
    def dia_semana_nacimiento(self)->str: # type: ignore[empty-body]
        ... 
    @property
    def dia_semana_siguiente_cumple(self)->str: # type: ignore[empty-body]
        ...
    @property
    def mes_cumple(self)->int: # type: ignore[empty-body]
        ...
    @property
    def horoscopo(self)->Horoscopo: # type: ignore[empty-body]
        ...  

       
    def __str__(self)->str:
        locale.setlocale(locale.LC_ALL, 'es_ES')
        fn = self.fecha_de_nacimiento
        return f'{self.nombre} {self.apellidos} de {self.edad} anyos, nacido el {fn.strftime("%A")} {fn.strftime("%d")} de {fn.strftime("%B")} de {fn.date().year}'
    

if __name__ == '__main__':
    p = Persona.parse('Casares Amador,Ramiro,00895902Y,1954-04-28 10:02,+34721510926,Ronda de Samanta Cobos 392;Málaga;29316')
    print(p)
#    print(p)
#    print(p.edad)
#    p = Persona.parse(' Ramirez Ayora, Juan, 30415004B,  29-06-2030 08:15')
    print(p)
#    p = Persona.parse('      , Juan, 30415004B,  29-06-2018 08:15')
    print(p)
    print(astuple(p))
    print(asdict(p))
    
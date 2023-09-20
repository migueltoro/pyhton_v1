'''
Created on 3 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass, astuple, asdict
from enum import Enum, auto
from us.lsi.tools.Preconditions import check_argument
import locale
from us.lsi.ejemplos_types.Direccion import Direccion
from datetime import date, datetime

class Horoscopo(Enum):
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
    Acuario = auto()
    Piscis = auto()

@dataclass(frozen=True,order=True)
class Persona:
    apellidos: str
    nombre: str
    dni: str
    fecha_de_nacimiento: datetime
    telefono: str
    direccion:Direccion
    
    @staticmethod
    def of(apellidos: str, nombre: str, dni: str, fecha_de_nacimiento: datetime, telefono:str,direccion:Direccion) -> Persona:
        check_argument(len(apellidos.strip()) > 0, f'Los apellidos no pueden estar en blanco' )
        check_argument(len(nombre.strip()) > 0, f'El nombre no puede estar en blanco' )
        check_argument(fecha_de_nacimiento < datetime.now(), f'La fecha debe estar en el pasado')
        check_argument(Persona._check_dni(dni), f'El dni no es correcto')
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
    def _check_dni(text:str)->bool:
        ls = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
        pn = text[0:-1]
        lt = text[-1:]
        n = int(pn) % 23
        return ls[n] == lt
        
    @property
    def edad(self)->int:
        nw = datetime.now()
        return nw.year-self.fecha_de_nacimiento.year
    
    
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
        return f'{self.nombre} {self.apellidos} de {self.edad} anyos, nacido el {fn.strftime("%A")} \
{fn.strftime("%d")} de {fn.strftime("%B")} de {fn.date().year}'
    

if __name__ == '__main__':
    p = Persona.parse('Casares Amador,Ramiro,00895902Y,2003-06-14 10:02,+34721510926,Ronda de Samanta Cobos 392;Málaga;29316')
    print(p)
#    print(p)
    print(p.edad)
#    p = Persona.parse(' Ramirez Ayora, Juan, 30415004B,  29-06-2030 08:15')
    print(p)
#    p = Persona.parse('      , Juan, 30415004B,  29-06-2018 08:15')
    print(p)
    print(astuple(p))
    print(asdict(p))
    
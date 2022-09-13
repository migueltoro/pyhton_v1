'''
Created on 17 ago 2022

@author: migueltoro
'''
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from us.lsi.tools.Preconditions import checkArgument
import locale

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
    
    @staticmethod
    def of(apellidos: str, nombre: str, dni: str, fecha_de_nacimiento: datetime) -> Persona:
        return Persona(apellidos, nombre, dni, fecha_de_nacimiento)
    
    @staticmethod
    def parse(text:str, ft:str = "%d-%m-%Y %H:%M")->Persona:
        partes:list[str] = text.split(',')
        apellidos: str =  partes[0].strip()
        nombre: str =  partes[1].strip()
        dni: str = partes[2].strip() 
        checkArgument(Persona._check_dni(dni), f'El dni no es correcto')
        fecha_de_nacimiento: datetime = datetime.strptime(partes[3].strip(), ft)
        return Persona(apellidos, nombre, dni, fecha_de_nacimiento)
    
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
#    @property
#    def siguiente_cumple(self) -> datetime: 
#        return None
#    @property
#    def dia_semana_nacimiento(self)->str: 
#        return None
#    @property
#    def dia_semana_siguiente_cumple(self)->str: 
#        return None
#    @property
#    def mes_cumple(self)->str: 
#        return None
#    @property
#    def horoscopo(self)->Horoscopo: 
#        return None
    
    def __str__(self)->str:
        locale.setlocale(locale.LC_ALL, 'es_ES')
        fn = self.fecha_de_nacimiento
        return f'{self.nombre} {self.apellidos} de {self.edad} anyos, nacido el {fn.strftime("%A")}\
 {fn.strftime("%d")} de {fn.strftime("%B")} de {fn.date().year}'
    

if __name__ == '__main__':
    p = Persona.parse('Ramirez Ayora, Juan, 30415004B,  29-06-2018 08:15')
    print(p)
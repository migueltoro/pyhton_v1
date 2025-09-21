from __future__ import annotations
from datetime import datetime, date
from dataclasses import dataclass
from enum import Enum, auto
from us.lsi.ejemplos_types.Direccion import Direccion

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

@dataclass(frozen=True,order=True)
class Persona:
    apellidos: str
    nombre: str
    dni: str
    fecha_de_nacimiento: datetime
    telefono: str
    direccion:Direccion
    
    @staticmethod
    def of(apellidos: str, nombre: str, dni: str, fecha_de_nacimiento: datetime, telefono:str,direccion:Direccion) -> Persona: ...
    @staticmethod
    def parse(text:str, ft:str = "%Y-%m-%d %H:%M")->Persona: ...
    @staticmethod
    def parse_list(ls:list[str], ft:str = "%Y-%m-%d %H:%M")->Persona: ...    
    @property
    def edad(self)->int: ...     
    @property
    def siguiente_cumple(self)->date: ...       
    @property
    def dia_semana_nacimiento(self)->str: ... 
    @property
    def dia_semana_siguiente_cumple(self)->str: ...
    @property
    def mes_cumple(self)->int: ...
    @property
    def horoscopo(self)->Horoscopo: ...  
    def __str__(self)->str: ...
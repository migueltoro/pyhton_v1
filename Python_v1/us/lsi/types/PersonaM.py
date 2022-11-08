'''
Created on 8 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from functools import total_ordering
from datetime import datetime
from enum import Enum, auto
from us.lsi.tools.Preconditions import check_argument
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
    
@total_ordering
class PersonaM:
    
    def __init__(self, apellidos: str,nombre: str, dni: str, fecha_de_nacimiento: datetime)->None:
        self._apellidos: str = apellidos
        self._nombre: str = nombre
        self._dni: str = dni
        self._fecha_de_nacimiento: datetime = fecha_de_nacimiento
    
    @staticmethod
    def of(apellidos: str, nombre: str, dni: str, fecha_de_nacimiento: datetime) -> PersonaM:
        check_argument(len(apellidos.strip()) > 0, f'Los apellidos no pueden estar en blanco' )
        check_argument(len(nombre.strip()) > 0, f'El nombre no puede estar en blanco' )
        check_argument(fecha_de_nacimiento < datetime.now(), f'La fecha debe estar en el pasado')
        check_argument(PersonaM._check_dni(dni), f'El dni no es correcto')
        return PersonaM(apellidos, nombre, dni, fecha_de_nacimiento)
    
    @staticmethod
    def parse(text:str, ft:str = "%d-%m-%Y %H:%M")->PersonaM:
        partes:list[str] = text.split(',')
        apellidos: str =  partes[0].strip()
        nombre: str =  partes[1].strip()
        dni: str = partes[2].strip() 
        fecha_de_nacimiento: datetime = datetime.strptime(partes[3].strip(), ft)
        return PersonaM.of(apellidos, nombre, dni, fecha_de_nacimiento)
    
    @staticmethod
    def _check_dni(text:str)->bool:
        ls = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
        pn = text[0:-1]
        lt = text[-1:]
        n = int(pn) % 23
        return ls[n] == lt
    
    @property
    def apellidos(self)-> str:
        return self._apellidos 
    
    @property
    def nombre(self)-> str:    
        return self._nombre
    
    @property
    def dni(self) -> str:
        return self._dni
    
    @property
    def fecha_de_nacimiento(self)->datetime:    
        return self._fecha_de_nacimiento
       
    @property
    def edad(self)->int:
        nw = datetime.now()
        return nw.year-self.fecha_de_nacimiento.year
    @property
    def siguiente_cumple(self) -> datetime: 
        pass
    @property
    def dia_semana_nacimiento(self)->str: 
        pass
    @property
    def dia_semana_siguiente_cumple(self)->str:
        pass
    @property
    def mes_cumple(self)->str: 
        pass
    @property
    def horoscopo(self)->Horoscopo: 
        pass
    
    def __eq__(self, other)->bool:
        if isinstance(other, PersonaM):
            return self._apellidos == other._apellidos and \
            self._nombre == other._nombre and \
            self._dni == other._dni and \
            self._fecha_de_nacimiento == other._fecha_de_nacimiento
        return False
    
    def __lt__(self, other)->bool:
        if self._apellidos < other._apellidos:
            return True
        elif  self._apellidos == other._apellidos and self._nombre < other._nombre:
            return True
        elif self._apellidos == other._apellidos and self._nombre == other._nombre and self._dni < other._dni:
            return True
        elif self._apellidos == other._apellidos and self._nombre == other._nombre and \
                self._dni == other._dni and self._fecha_de_nacimiento < other._fecha_de_nacimiento:
            return True
        return False
    
    def __hash__(self)->int:
        r:int = hash(self._apellidos)
        r += 31*r + hash(self._nombre)
        r += 31*r + hash(self._dni)
        r += 31*r + hash(self._fecha_de_nacimiento)
        return r
      
    
    def __str__(self)->str:
        locale.setlocale(locale.LC_ALL, 'es_ES')
        fn = self.fecha_de_nacimiento
        return f'{self.nombre} {self.apellidos} de {self.edad} anyos, nacido el {fn.strftime("%A")}\
 {fn.strftime("%d")} de {fn.strftime("%B")} de {fn.date().year}'

if __name__ == '__main__':
    p = PersonaM.parse('Ramirez Ayora, Juan, 30415004B,  29-06-2018 08:15')
    print(p)
    print(p.edad)
#    p = Persona.parse(' Ramirez Ayora, Juan, 30415004B,  29-06-2030 08:15')
    print(p)
#    p = Persona.parse('      , Juan, 30415004B,  29-06-2018 08:15')
    print(p)
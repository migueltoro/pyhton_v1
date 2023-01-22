'''
Created on 8 nov 2022

@author: belen
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, date
from us.lsi.tools.Preconditions import check_argument
import locale
from us.lsi.centro.Direccion import Direccion
from dateutil.relativedelta import relativedelta



locale.setlocale(locale.LC_ALL, 'es_ES')
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
        nw:datetime = datetime.now()
        return relativedelta(nw,self.fecha_de_nacimiento).years
   
    @property
    def dia_semana_nacimiento(self)->str: 
        return self.fecha_de_nacimiento.strftime("%A")
    
    @property
    def mes_cumple(self)->str: 
        return self.fecha_de_nacimiento.strftime("%B")
    
    @property
    def siguiente_cumple(self)->date:
        today_year:int = date.today().year
        return date(today_year+1, self.fecha_de_nacimiento.month, self.fecha_de_nacimiento.day)
        
    @property
    def dia_semana_siguiente_cumple(self)->str: 
        return self.siguiente_cumple.strftime("%A")
        
         
    def __str__(self)->str:
        return f'{self.nombre} {self.apellidos} de {self.edad} anyos, nacido el {self.dia_semana_nacimiento} {self.fecha_de_nacimiento.day} de {self.mes_cumple} de {self.fecha_de_nacimiento.year}'


if __name__ == '__main__':
    p:Persona = Persona.parse('Casares Amador,Ramiro,00895902Y,2003-06-14 10:02,+34721510926,Ronda de Samanta Cobos 392;Málaga;29316')
    print(p)
    print(f'- La fecha de nacimiento de {p.nombre} es {p.fecha_de_nacimiento}')
    print(f'- La edad de {p.nombre} es {p.edad}')
    print(f'- Su próximo cumpleaños será un {p.dia_semana_siguiente_cumple}')


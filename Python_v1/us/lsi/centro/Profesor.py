'''
Created on 8 nov 2022

@author: belen
'''
from __future__ import annotations
from dataclasses import dataclass
from us.lsi.centro.Persona import Persona
from enum import Enum, auto

class Titulo(Enum):
    Diplomado = auto()
    Master = auto()
    Doctor = auto()
    
@dataclass(frozen=True)
class Profesor(Persona):
    titulo:Titulo 
    
    @staticmethod
    def of_persona(p:Persona,titulo:Titulo)->Profesor: 
        return Profesor(p.apellidos,p.nombre,p.dni,p.fecha_de_nacimiento,p.telefono,p.direccion,titulo) 
    
    @staticmethod
    def parse_profesor(text:str)->Profesor: 
        ls:list[str] = text.split(',')
        titulo:Titulo= Titulo[ls[-1].strip()]
        p:Persona = Persona.parse_list(ls[0:-1])
        return Profesor.of_persona(p,titulo)

    
    def __str__(self)->str:
        return super().__str__() + f' con titulo {self.titulo.name}'

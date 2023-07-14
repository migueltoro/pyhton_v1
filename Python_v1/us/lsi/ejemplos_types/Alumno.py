'''
Created on 4 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from us.lsi.ejemplos_types.Persona import Persona

@dataclass(frozen=True)
class Alumno(Persona):
    nota:float
    
    @staticmethod
    def of_persona(p:Persona,nota:float)->Alumno: 
        return Alumno(p.apellidos,p.nombre,p.dni,p.fecha_de_nacimiento,p.telefono,p.direccion,nota) 
        
    @staticmethod
    def parse_alumno(text:str)->Alumno: 
        ls:list[str] = text.split(',')
        nota:float= float(ls[-1])
        p:Persona = Persona.parse_list(ls[0:-1])
        return Alumno.of_persona(p,nota)
    
    @staticmethod
    def parse_list_alumno(ls:list[str])->Alumno: 
        nota:float= float(ls[-1])
        p:Persona = Persona.parse_list(ls[0:-1])
        return Alumno.of_persona(p,nota)
    
    def __str__(self)->str:
        return super().__str__() + f' con nota de entrada {self.nota}'


if __name__ == '__main__':
    pass
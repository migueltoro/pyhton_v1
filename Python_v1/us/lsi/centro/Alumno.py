'''
Created on 8 nov 2022

@author: belen
'''

from __future__ import annotations
from dataclasses import dataclass
from us.lsi.centro.Persona import Persona
from us.lsi.tools import Preconditions

@dataclass(frozen=True)
class Alumno(Persona):
    nota:float
    
    @staticmethod
    def of_persona(p:Persona,nota:float)->Alumno: 
        Preconditions.check_argument(0<=nota<=14, 'La nota debe estar comprendida entre 0 y 14')
        return Alumno(p.apellidos,p.nombre,p.dni,p.fecha_de_nacimiento,p.telefono,p.direccion,nota) 
        
    @staticmethod
    def parse_alumno(text:str)->Alumno: 
        ls:list[str] = text.split(',')
        nota:float= float(ls[-1])
        p: Persona = Persona.parse_list(ls[0:-1])
        return Alumno.of_persona(p,nota)

    
    def __str__(self)->str:
        return super().__str__() + f' con nota de entrada {self.nota}'
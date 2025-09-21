from __future__ import annotations
from dataclasses import dataclass
from us.lsi.ejemplos_types.Persona import Persona

@dataclass(frozen=True)
class Alumno(Persona):
    nota:float
    
    @staticmethod
    def of_persona(p:Persona,nota:float)->Alumno: ...  
    @staticmethod
    def parse_alumno(text:str)->Alumno: ...
    @staticmethod
    def parse_list_alumno(ls:list[str])->Alumno: ...
    def __str__(self)->str: ...
        
    
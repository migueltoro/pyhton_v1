'''
Created on 28 oct 2023

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import TypeVar, Any
from datetime import datetime, date

R = TypeVar('R')

@dataclass(order=True, frozen=True)
class Persona:
    nombre:str
    apellido:str
    edad:int
    altura:float
    fecha:date
    
    @staticmethod
    def parse(text: list[str]) -> Persona:
        return Persona(text[0],text[1],int(text[2]),float(text[3]),datetime.strptime(text[4],'%d/%m/%Y').date())
    
    @staticmethod
    def val(text:list[str],prop:str) -> Any:
        return asdict(Persona.parse(text))[prop]
    
if __name__ == '__main__':
    pass
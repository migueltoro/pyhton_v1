'''
Created on 8 nov 2022

@author: belen
'''
from __future__ import annotations
from dataclasses import dataclass



@dataclass(frozen=True)
class Asignatura:
    ida:int
    nombre:str
    creditos:int
    num_grupos:int
    
    @staticmethod
    def parse(text:str)->Asignatura:
        partes = text.split(',')
        a = Asignatura(int(partes[0].strip()),partes[1].strip().capitalize(),int(partes[2].strip()),int(partes[3].strip()))
        return a
        
    def __str__(self)->str:
        return f'{self.nombre},{self.creditos},{self.num_grupos}'



'''
Created on 4 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
    
@dataclass(frozen=True)
class Matricula:
    dni:str
    ida:int
    idg:int
    
    @staticmethod
    def of(dni:str,ida:int,idg:int)->Matricula:
        return Matricula(dni,ida,idg)
    
    @staticmethod
    def parse(text:str)->Matricula:
        partes = text.split(',')
        return Matricula(partes[0],int(partes[1]),int(partes[2]))


    def __str__(self)->str:
        return f'{self.dni},{self.ida},{self.idg}'
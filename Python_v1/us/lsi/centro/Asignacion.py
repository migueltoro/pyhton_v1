'''
Created on 11 nov 2022

@author: belen
'''
from __future__ import annotations
from dataclasses import dataclass
    
@dataclass(frozen=True)
class Asignacion:
    dni:str
    ida:int
    idg:int
    
    @staticmethod
    def of(dni:str,ida:int,idg:int)->Asignacion:
        return Asignacion(dni,ida,idg)
    
    @staticmethod
    def parse(text:str)->Asignacion:
        partes = text.split(',')
        return Asignacion(partes[0],int(partes[1]),int(partes[2]))
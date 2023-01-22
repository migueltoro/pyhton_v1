'''
Created on 8 nov 2022

@author: belen
'''
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Direccion:
    calle: str
    ciudad:str
    zip_code: int
    
    @staticmethod
    def parse(text:str)->Direccion:
        partes = text.split(';')
        return Direccion(partes[0],partes[1],int(partes[2]))


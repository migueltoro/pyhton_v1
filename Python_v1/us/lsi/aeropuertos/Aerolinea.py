'''
Created on 19 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Aerolinea:
    codigo: str
    nombre: str
    
    @staticmethod 
    def of(codigo:str, nombre:str) -> Aerolinea:
        return Aerolinea(codigo,nombre)
    
    @staticmethod 
    def parse(text:str) -> Aerolinea:
        campos: list[str] = text.split(",")
        codigo: str = campos[0].strip()
        nombre: str = campos[1].strip()
        return Aerolinea.of(codigo,nombre)
    
    def __str__(self):
        return f'({self.codigo},{self.nombre})'

if __name__ == '__main__':
    pass
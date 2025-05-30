'''
Created on 25 ago 2024

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Ciudad:
    nombre:str
    habitantes:int
    
    @staticmethod 
    def of(nombre:str,habitantes:int)-> Ciudad:
        return Ciudad(nombre,habitantes)
        
    @staticmethod   
    def parse(linea: str) -> Ciudad:
        nombre,habitantes = linea.split(',')
        return Ciudad(nombre,int(habitantes))
    
    def __str__(self):
        return f'({self.nombre},{self.habitantes:d})'

if __name__ == '__main__':
    pass
    
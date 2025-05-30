'''
Created on 25 ago 2024

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass



@dataclass(frozen=True)
class Carretera:
    id:int
    nombre:str
    km:float
    __xx_num:int = 0
    
    @staticmethod 
    def of(nombre:str,km:float)-> Carretera:
        Carretera.__xx_num += 1
        return Carretera(Carretera.__xx_num,nombre,km)
    
    def __str__(self):
        return f'({self.nombre},{self.km:0.2f})'


if __name__ == '__main__':
    pass
'''
Created on 25 jun 2023

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Grupo:
    ida:int
    idg:int
    
    @staticmethod
    def of(ida:int,idg:int)->Grupo:
        return Grupo(ida,idg)
    
    

if __name__ == '__main__':
    pass
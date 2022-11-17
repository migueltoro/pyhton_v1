'''
Created on 3 nov 2022

@author: migueltoro
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
    
    def __str__(self):
        return f'{self.calle};{self.ciudad};{self.zip_code}'

if __name__ == '__main__':
    print(Direccion.parse('Pasadizo de Lorenza Dueñas 44 Apt. 02;Huelva;40664'))
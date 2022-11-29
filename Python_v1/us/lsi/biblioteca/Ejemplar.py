# -*- coding: utf-8 -*-
'''
Created on 9 ago 2022

@author: mateosg
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime

@dataclass(frozen=True,order=True)
class Ejemplar:
    isbn: str
    codigo: int
    fecha_adquisicion: date
    
    @staticmethod
    def of(isbn:str, codigo: int, fecha_adquisicion:date) -> Ejemplar:
        return Ejemplar(isbn,codigo,fecha_adquisicion)
    
    '''
    978-0-04-228215-2,0,2019-01-29
    '''
    @staticmethod
    def of_file(text:str)->Ejemplar:
        partes:list[str] = text.split(',')
        isbn:str = partes[0]
        codigo:int = int(partes[1])
        fecha_adquision:date = datetime.strptime(partes[2],"%Y-%m-%d").date()
        return Ejemplar.of(isbn,codigo,fecha_adquision)
        
    
if __name__ == '__main__':
    pass
    
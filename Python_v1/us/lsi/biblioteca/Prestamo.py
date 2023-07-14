# -*- coding: utf-8 -*-
'''
Created on 9 ago 2022

@author: mateosg
'''
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from datetime import date, timedelta, datetime
from typing import ClassVar


class Tipo_prestamo(Enum):
    DIARIO=auto()
    SEMANAL=auto()
    MENSUAL=auto()

@dataclass(frozen=True,order=True)
class Prestamo:
    codigo: int
    isbn:str
    codigo_ejemplar:int
    dni:str
    fecha_prestamo:date
    tipo: Tipo_prestamo
    __np:ClassVar[int] = 0
    
    @property
    def fecha_entrega(self:Prestamo) -> date:
        match self.tipo:
            case Tipo_prestamo.DIARIO:
                return self.fecha_prestamo + timedelta(days=1)
            case Tipo_prestamo.SEMANAL:
                return self.fecha_prestamo + timedelta(weeks=1)
            case _:
                return self.fecha_prestamo + timedelta(days=30)
            
    @staticmethod
    def of(isbn:str,codigo_ejemplar:int,dni:str,fecha_prestamo:date,tipo:Tipo_prestamo) -> Prestamo:    
        codigo = Prestamo.__np
        Prestamo.__np = Prestamo.__np+1
        return Prestamo(codigo,isbn,codigo_ejemplar,dni,fecha_prestamo,tipo)   
    
    '''
    978-1-04-876475-8,1,52240178W,2020-02-03,MENSUAL
    ''' 
    
    @staticmethod
    def parse(text:str)->Prestamo:
        ls:list[str] = text.split(',')
        fecha:date = datetime.strptime(ls[3],"%Y-%m-%d").date()
        return Prestamo.of(ls[0],int(ls[1]),ls[2],fecha,Tipo_prestamo[ls[4]])       
    
if __name__ == '__main__':
    p = Prestamo.parse('978-1-04-876475-8,1,52240178W,2020-02-03,MENSUAL')
    print(p)
'''
Created on 23 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from us.lsi.ruta.Marca import Marca
from datetime import datetime,date
from enum import Enum, auto

class Type(Enum):
    Descendiente = auto()
    LLano = auto()
    Ascendiente = auto()
    
    def __str__(self):
        return str(self.name)

@dataclass(frozen=True,order=True)
class Intervalo:
    principio: Marca
    fin: Marca
    
    def __post_init__(self) -> None:
        assert self.principio <= self.fin,'Principio={0}, fin={1}'.format(self.principio,self.fin)
    
    @staticmethod
    def of(principio: Marca, fin:Marca) -> Intervalo:      
        return Intervalo(principio,fin)
    
    def __str__(self):
        return '({0},{1})'.format(self.principio,self.fin) 

    @property
    def desnivel(self) -> float:
        return self.fin.coordenadas.altitud-self.principio.coordenadas.altitud
    
    @property
    def longitud(self) -> float:
        return self.principio.coordenadas.distancia(self.fin.coordenadas)
    
    @property
    def tiempo(self) -> float:
        return (datetime.combine(date.min,self.fin.tiempo) - datetime.combine(date.min,self.principio.tiempo)).seconds/3600
    
    @property
    def velocidad(self) -> float:
        assert self.tiempo > 0, 'El tiempo debe ser mayor que cero y es {0}'.format(self.tiempo)
        return self.longitud/self.tiempo

    @property
    def type(self) -> Type:
        if self.desnivel == 0:
            return Type.LLano
        elif self.desnivel > 0:
            return Type.Ascendiente
        else:
            return Type.Descendiente

if __name__ == '__main__':
    linea1 = '00:00:00,36.74991256557405,-5.147951105609536,712.2000122070312'.split(',')
    m1 = Marca.parse(linea1)
    linea2 = '00:00:30,36.75008556805551,-5.148005923256278,712.7999877929688'.split(',')
    m2 = Marca.parse(linea2)
    it = Intervalo.of(m1,m2)
    print(it)
    print(it.desnivel)
    print(it.longitud)
    print(it.tiempo)
    print(it.velocidad)
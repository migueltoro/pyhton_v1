'''
Created on 23 jul. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from typing import TypeVar
from us.lsi.ruta.Marca import Marca
from us.lsi.tools import Preconditions
from us.lsi.tools.Dates import to_datetime

Intervalo = TypeVar('Intervalo')

@dataclass(frozen=True,order=True)
class Intervalo:
    principio: Marca
    fin: Marca
    
    @staticmethod
    def of(principio: Marca, fin:Marca) -> Intervalo:
        return Intervalo(principio,fin)
    
    def __str__(self):
        return '({0},{1})'.format(self.principio,self.fin) 

    @property
    def desnivel(self) -> float:
        return self.fin.coordenadas.altitude-self.principio.coordenadas.altitude
    
    @property
    def longitud(self) -> float:
        return self.principio.coordenadas.distance(self.fin.coordenadas)
    
    @property
    def tiempo(self) -> float:
        return ((to_datetime(self.fin.tiempo) - to_datetime(self.principio.tiempo)).seconds)/3600
    
    @property
    def velocidad(self) -> float:
        Preconditions.checkArgument(self.tiempo > 0, 'El tiempo debe ser mayor que cero y es {0:.2f}'.format(self.tiempo))
        return self.longitud/self.tiempo


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
'''
Created on 24 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from us.lsi.tools.Preconditions import checkArgument
from us.lsi.coordenadas.Coordenadas2D import Coordenadas2D


@dataclass(frozen=True,order=True)
class Estacion:
    numero: int
    name: str    
    slots: int
    empty_slots: int
    free_bikes: int
    ubicacion: Coordenadas2D

    
    @staticmethod   
    def parse(linea: list[str]) -> Estacion:
        name,slots,empty_slots,free_bikes,longitude,latitude = linea
        checkArgument('_' in name,'{0} no contiene _'.format(name))
        numero, name = name.split("_")
        numero = int(numero)
        slots = int(slots)
        empty_slots = int(empty_slots)
        free_bikes = int(free_bikes)
        ubicacion = Coordenadas2D(float(longitude),float(latitude))
        return Estacion.of(numero,name,slots,empty_slots,free_bikes,ubicacion)
    
    @staticmethod   
    def of(numero:int,name:str,slots:int,empty_slots:int,free_bikes:int,ubicacion:Coordenadas2D) -> Estacion:
        checkArgument(slots>=0,"Slots deben ser mayor o igual que cero y es {0:d}".format(slots))
        checkArgument(empty_slots>=0,"Empty_Slots deben ser mayor o igual que cero y es {0:d}".format(empty_slots));
        checkArgument(free_bikes>=0,"Free_Bikes deben ser mayor o igual que cero y es {0:d}".format(free_bikes));
        return Estacion(numero,name, slots, empty_slots,free_bikes,ubicacion)
    
    @property
    def nombre_compuesto(self) -> str:
        return '{0}_{1}'.format(self.numero,self.name)
    
    def __str__(self):
        return '{0:3d} {1:>35s} {2:2d} {3:2d} {4:2d} {5:>40s}'.format(self.numero,self.name,self.slots,self.empty_slots,self.free_bikes,str(self.ubicacion))

if __name__ == '__main__':
    e = Estacion.parse('149_CALLE ARROYO,20,11,9,37.397829929383,-5.97567172039552'.split(','))
    print(e)
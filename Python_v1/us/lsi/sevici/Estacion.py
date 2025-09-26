'''
Created on 24 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from us.lsi.coordenadas.Coordenadas2D import Coordenadas2D


@dataclass(frozen=True,order=True)
class Estacion:
    numero: int
    name: str    
    slots: int
    empty_slots: int
    free_bikes: int
    ubicacion: Coordenadas2D
    
    def __post_init__(self) -> None:
        assert self.numero >= 0, f'El numero de la estacion debe ser mayor o igual que cero y es {self.numero}'
        assert self.slots >= 0, f'Slots deben ser mayor o igual que cero y es {self.slots}'
        assert self.empty_slots >= 0, f'Empty_Slots deben ser mayor o igual que cero y es {self.empty_slots}'
        assert self.free_bikes >= 0, f'Free_Bikes deben ser mayor o igual que cero y es {self.free_bikes}'
        assert isinstance(self.ubicacion, Coordenadas2D), f'Ubicacion debe ser Coordenadas2D y es {type(self.ubicacion)}'

    @staticmethod   
    def parse(linea: list[str]) -> Estacion:
        name,slots,empty_slots,free_bikes,longitude,latitude = linea
        assert '_' in name,f'{name} no contiene _'
        numero, name = name.split("_")
        numero0 = int(numero)
        slots0 = int(slots)
        empty_slots0 = int(empty_slots)
        free_bikes0 = int(free_bikes)
        ubicacion = Coordenadas2D(float(longitude),float(latitude))
        return Estacion.of(numero0,name,slots0,empty_slots0,free_bikes0,ubicacion)
    
    @staticmethod   
    def of(numero:int,name:str,slots:int,empty_slots:int,free_bikes:int,ubicacion:Coordenadas2D) -> Estacion:
        return Estacion(numero,name, slots, empty_slots,free_bikes,ubicacion)
    
    @property
    def nombre_compuesto(self) -> str:
        return '{0}_{1}'.format(self.numero,self.name)
    
    def __str__(self)->str:
        return '{0:3d} {1:>35s} {2:2d} {3:2d} {4:2d} {5:>40s}'.format(self.numero,self.name,self.slots,self.empty_slots,self.free_bikes,str(self.ubicacion))

if __name__ == '__main__':
    e = Estacion.parse('149_CALLE ARROYO,20,11,9,37.397829929383,-5.97567172039552'.split(','))
    print(e)
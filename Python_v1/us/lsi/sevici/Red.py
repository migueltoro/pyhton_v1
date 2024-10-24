'''
Created on 24 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from typing import Optional
from us.lsi.sevici.Estacion import Estacion
from us.lsi.tools.File import encoding, absolute_path
from us.lsi.coordenadas.Coordenadas2D import Coordenadas2D
#from sortedcontainers import SortedSet # type: ignore
#from us.lsi.tools.GraphicsMaps import markers
from abc import ABC,abstractmethod
from enum import Enum, auto

class RedType(Enum):   
    Clasica = auto()
    Comprension = auto()   

class Red(ABC):
    
    redType:RedType = RedType.Comprension
    
    def __init__(self, e:list[Estacion],por_nombre_compuesto:dict[str,Estacion],
                 por_numero:dict[int,Estacion]):
        self._estaciones:list[Estacion] = e
        self._por_nombre_compuesto:dict[str,Estacion] = por_nombre_compuesto
        self._por_numero:dict[int,Estacion] = por_numero
    
    
    @abstractmethod
    def __str__(self) -> str:
        ...
    
    @property
    def estaciones(self)->list[Estacion]:
        return self._estaciones
    
    @property
    def por_nombre_compuesto(self)->dict[str,Estacion]:
        return self._por_nombre_compuesto
    
    @property
    def por_numero(self)->dict[int,Estacion]:
        return self._por_numero
    
    @property
    def numero_de_estaciones(self) -> int:
        return len(self._estaciones)
    
    def estacion_de_nombre_compuesto(self,name:str) -> Optional[Estacion]:
        return self._por_nombre_compuesto.get(name,None)
                         
    def estacion_de_numero(self, n:int) -> Optional[Estacion]: 
        return self._por_numero.get(n,None)
    
    def add(self,estacion:Estacion)->None:
        assert estacion.numero not in self.por_numero,'El numero {} de la estacion esta repetido'.format(estacion.numero)
        assert estacion.nombre_compuesto not in self.por_nombre_compuesto, 'El nombre compuesto {} de la estacion esta repetido'.format(estacion.nombre_compuesto)
        self._estaciones.append(estacion)
        self._estaciones.sort()
        self._por_nombre_compuesto[estacion.nombre_compuesto] = estacion
        self._por_numero[estacion.numero] = estacion
    
    def remove_estacion(self,estacion:Estacion)->None:
        self._estaciones.remove(estacion)
        self._estaciones.sort()
        del self._por_nombre_compuesto[estacion.nombre_compuesto]
        del self._por_numero[estacion.numero]
    
    @abstractmethod
    def estaciones_cercanas_a(self, c: Coordenadas2D, distancia:float) -> list[Estacion]:
        ...
    
    @abstractmethod
    def estaciones_con_bicis_disponibles(self, k:int=1) -> set[Estacion]:
        ...
    
    @abstractmethod
    def ubicaciones_con_bicis_disponibles(self, k:int=1) -> set[Coordenadas2D]:
        ...
    
    @abstractmethod   
    def estacion_con_mas_bicis_disponibles(self) -> Estacion:
        ...
    
    @abstractmethod
    def estaciones_por_bicis_disponibles(self) -> dict[int,list[Estacion]]:
        ...
    
    @abstractmethod
    def numero_de_estaciones_por_bicis_disponibles(self) ->  dict[int,int]:
        ... 
    
if __name__ == '__main__':
    print(encoding(absolute_path("datos/estaciones.csv")))
    numero,name = '242_PLAZA NUEVA'.split('_')
    
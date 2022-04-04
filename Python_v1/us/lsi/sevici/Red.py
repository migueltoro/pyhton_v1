'''
Created on 24 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.sevici.Estacion import Estacion
from us.lsi.tools.File import encoding, lineas_de_csv, absolute_path
from us.lsi.coordenadas.Coordenadas2D import Coordenadas2D
from sortedcontainers import SortedSet
from us.lsi.tools.Iterable import grouping_list, str_iterable,groups_size
from us.lsi.tools.Preconditions import checkArgument
from us.lsi.tools.Dict import str_dictionary
from us.lsi.tools.GraphicsMaps import markers


class Red:
    
    def __init__(self, e:list[Estacion],por_nombre_compuesto:dict[str,Estacion]=None,por_numero:dict[int,Estacion]=None):
        self._estaciones:list[Estacion] = e
        self._por_nombre_compuesto:dict[str,Estacion] = por_nombre_compuesto
        self._por_numero:dict[int,Estacion] = por_numero
    
    @staticmethod
    def of(e:list[Estacion],por_nombre_compuesto:dict[str,Estacion]=None,por_numero:dict[int,Estacion]=None) -> Red:
        return Red(e,por_nombre_compuesto,por_numero)
    
    @staticmethod
    def data_of_file(fichero: str) -> Red:
        estaciones = [Estacion.parse(x) for x in lineas_de_csv(fichero, delimiter =",",encoding='cp1252')[1:]]
        checkArgument(len(estaciones) == len({e.numero for e in estaciones}),'Hay numeros de estacion repetidos')
        pnc = {e.nombre_compuesto:e for e in estaciones}
        pn = {e.numero:e for e in estaciones}
        estaciones.sort()
        return Red.of(estaciones,pnc,pn) 
    
    def __str__(self) -> str:
        return str_iterable(self._estaciones,sep='\n',prefix='Estaciones\n',suffix='\n---------------------')
    
    @property
    def estaciones(self)->list[Estacion]:
        return self._estaciones
    
    @property
    def por_nombre_compuesto(self)->dict[str,Estacion]:
        return self._por_nombre_compuesto
    
    @property
    def por_numero(self)->dict[int,Estacion]:
        return self._por_numero
    
    def __add__(self,estacion:Estacion)->None:
        checkArgument(estacion.numero not in self.por_numero,'El numero {} de la estacion esta repetido'.format(estacion.numero))
        checkArgument(estacion.nombre_compuesto not in self.por_nombre_compuesto, 'El nombre compuesto {} de la estacion esta repetido'.format(estacion.nombre_compuesto))
        self._estaciones.append(estacion)
        pnc = {e.nombre_compuesto:e for e in self._estaciones}
        pn = {e.numero:e for e in self._estaciones}
        self._estaciones.sort()
        self._por_nombre_compuesto = pnc
        self._por_numero = pn
    
    def remove(self,estacion:Estacion)->None:
        self._estaciones.remove(estacion)
        pnc = {e.nombre_compuesto:e for e in self._estaciones}
        pn = {e.numero:e for e in self._estaciones}
        self._estaciones.sort()
        self._por_nombre_compuesto = pnc
        self._por_numero = pn
    
    def estaciones_cercanas_a(self, c: Coordenadas2D, distancia:float) -> list[Estacion]:
        return sorted(e for e in self.estaciones if e.ubicacion.distancia(c) <= distancia)
   
    @property
    def numero_de_estaciones(self) -> int:
        return len(self._estaciones)
    
    def estacion_de_nombre_compuesto(self,name:str) -> Estacion | None:
        return self.por_nombre_compuesto.get(name,None)
                 
    def estacion_de_numero(self, n:int) -> Estacion | None: 
        return self.por_numero.get(n,None)
 
    def estaciones_con_bicis_disponibles(self, k:int=1) -> set[Estacion]:
            return {e for e in self.estaciones if e.free_bikes >= k}
    
    def ubicaciones_con_bicis_disponibles(self, k:int=1) -> set[Coordenadas2D]:
            return {e.ubicacion for e in self.estaciones if e.free_bikes >= k}
        
    @property
    def estacion_con_mas_bicis_disponibles(self) -> Estacion:
        return max(self.estaciones, key = lambda e:e.free_bikes)
    
    @property
    def estaciones_por_bicis_disponibles(self) -> dict[int,list[Estacion]]:
        return grouping_list(self.estaciones, lambda e: e.free_bikes)
   
    @property
    def numero_de_estaciones_por_bicis_disponibles(self) ->  dict[int,int]:
        return groups_size(self.estaciones, lambda e: e.free_bikes)  
    


if __name__ == '__main__':
    print(encoding(absolute_path("/resources/estaciones.csv")))
    numero,name = '242_PLAZA NUEVA'.split('_')
#    print(numero)
#    print(name)
    r = Red.data_of_file(absolute_path("/resources/estaciones.csv"))
#    r.__add__(Estacion.parse('361_ESTACA DE VARES,17,12,5,37.38369648551305,-5.914819934855601'.split(',')))
#    print(r)
 #   print(r.estacion_de_numero(6).ubicacion.distancia_a())
#    print(str_dictionary(r.numero_de_estaciones_por_bicis_disponibles,sep='\n'))
    
    
    
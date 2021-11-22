'''
Created on 24 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from us.lsi.sevici.Estacion import Estacion
from us.lsi.tools import File
from us.lsi.coordenadas.Coordenadas2D import Coordenadas2D
from sortedcontainers import SortedSet
from us.lsi.tools.Iterable import grouping_list, str_iterable,frequencies

@dataclass(frozen=True)
class Red:
    estaciones: list[Estacion]
    name:str = 'Sevici'
    href:str = None
    country:str = 'ES'
    city:str = 'Sevilla'
    ubicacion:Coordenadas2D = Coordenadas2D.of(37.388096,-5.982330)
    por_nombre_compuesto:dict[str,Estacion] = None
    por_numero:dict[int,Estacion] = None
    
    
    @staticmethod
    def data_of_file(fichero: str) -> Red:
        estaciones = [Estacion.parse(x) for x in File.lineas_de_csv(fichero, delimiter =",",encoding='cp1252')[1:]]
        pnc = {e.nombre_compuesto:e for e in estaciones}
        pn = {e.numero:e for e in estaciones}
        estaciones.sort()
        return Red(estaciones,por_nombre_compuesto=pnc,por_numero=pn) 
    
    def __str__(self) -> str:
        return 'Nombre = {0:s}\nEstaciones\n{1:s}'.format(self.name,'\n'.join(str(e) for e in self.estaciones))
    
    def estaciones_cercanas_a(self, c: Coordenadas2D, distancia:float) -> SortedSet:
        sorted_set = SortedSet()
        for e in self.estaciones:
            if e.ubicacion.distancia(c) <= distancia:
                sorted_set.add(e) 
        return sorted_set
   
    @property
    def numero_de_estaciones(self) -> int:
        return len(self.estaciones)
    
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
        return frequencies(self.estaciones, lambda e: e.free_bikes)  


if __name__ == '__main__':
    File.encoding("../../../resources/estaciones.csv")
    numero,name = '242_PLAZA NUEVA'.split('_')
#    print(numero)
#    print(name)
    r = Red.data_of_file("../../../resources/estaciones.csv")
#    print(r)
    print(r.estacion_con_mas_bicis_disponibles)
    print(r.estacion_de_numero(86))
    print(r.estacion_de_nombre_compuesto('86_CAMINO DE LOS DESCUBRIMIENTOS'))
    print(str_iterable(r.numero_de_estaciones_por_bicis_disponibles.items()))
    print(str_iterable(r.estaciones_con_bicis_disponibles(k=2)))
    
    
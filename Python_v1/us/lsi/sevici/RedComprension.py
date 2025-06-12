'''
Created on 24 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.sevici.Estacion import Estacion
from us.lsi.tools.File import encoding, lineas_de_csv, absolute_path
from us.lsi.coordenadas.Coordenadas2D import Coordenadas2D
#from sortedcontainers import SortedSet # type: ignore
from us.lsi.tools.Iterable import grouping_list, str_iter,groups_size
from us.lsi.tools.Dict import str_dict
#from us.lsi.tools.GraphicsMaps import markers
from us.lsi.sevici.Red import Red

class RedComprension(Red):
    
    def __init__(self, e:list[Estacion],por_nombre_compuesto:dict[str,Estacion],
                 por_numero:dict[int,Estacion]):
        super().__init__(e,por_nombre_compuesto,por_numero)
        
    @staticmethod
    def of(estaciones:list[Estacion]) -> Red:
        assert len(estaciones) == len({e.numero for e in estaciones}),'Hay numeros de estacion repetidos'
        pnc:dict[str,Estacion] = {e.nombre_compuesto:e for e in estaciones}
        pn:dict[int,Estacion] = {e.numero:e for e in estaciones}
        estaciones.sort()
        return RedComprension(estaciones,pnc,pn)
    
    @staticmethod
    def parse(fichero: str) -> Red:
        lineas:list[list[str]] = lineas_de_csv(fichero, delimiter =",",encoding='utf-8')
        estaciones:list[Estacion] = [Estacion.parse(x) for x in lineas[1:]]
        return RedComprension.of(estaciones)
    
    def __str__(self) -> str:
        return str_iter(self.estaciones,sep='\n',prefix='Estaciones\n',suffix='\n---------------------') 
    
    def estaciones_cercanas_a(self, c: Coordenadas2D, distancia:float) -> list[Estacion]:
        return sorted(e for e in self.estaciones if e.ubicacion.distancia(c) <= distancia)
 
    def estaciones_con_bicis_disponibles(self, k:int=1) -> set[Estacion]:
            return {e for e in self.estaciones if e.free_bikes >= k}
    
    def ubicaciones_con_bicis_disponibles(self, k:int=1) -> set[Coordenadas2D]:
            return {e.ubicacion for e in self.estaciones if e.free_bikes >= k}
        
    
    def estacion_con_mas_bicis_disponibles(self) -> Estacion:
        return max(self.estaciones, key = lambda e:e.free_bikes)
    
    
    def estaciones_por_bicis_disponibles(self) -> dict[int,list[Estacion]]:
        return grouping_list(self.estaciones, lambda e: e.free_bikes)
   
    
    def numero_de_estaciones_por_bicis_disponibles(self) ->  dict[int,int]:
        return groups_size(self.estaciones, lambda e: e.free_bikes)  
    


if __name__ == '__main__':
    print(encoding(absolute_path("datos/estaciones.csv")))
    numero,name = '242_PLAZA NUEVA'.split('_')
#    print(numero)
#    print(name)
    r = RedComprension.parse(absolute_path("datos/estaciones.csv"))
#    r.__add__(Estacion.parse('361_ESTACA DE VARES,17,12,5,37.38369648551305,-5.914819934855601'.split(',')))
#    print(r)
#   print(r.estacion_de_numero(6).ubicacion.distancia_a())
    print(str_dict(r.numero_de_estaciones_por_bicis_disponibles(),sep='\n'))
    
    
    
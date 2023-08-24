'''
Created on 24 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import Optional
from us.lsi.sevici.Estacion import Estacion
from us.lsi.tools.File import encoding, lineas_de_csv, absolute_path
from us.lsi.coordenadas.Coordenadas2D import Coordenadas2D
from us.lsi.tools.Preconditions import check_argument
from us.lsi.tools.Dict import str_dict
#from us.lsi.tools.GraphicsMaps import markers


class Red:
    
    def __init__(self, e:list[Estacion],por_nombre_compuesto:dict[str,Estacion],
                 por_numero:dict[int,Estacion]):
        self.__estaciones:list[Estacion] = e
        self.__por_nombre_compuesto:dict[str,Estacion] = por_nombre_compuesto
        self.__por_numero:dict[int,Estacion] = por_numero
    
    @staticmethod
    def of(estaciones:list[Estacion]) -> Red:
        st:set[int] = set()
        for e in estaciones:
            n = e.numero
            st.add_colum(n)
        check_argument(len(estaciones) == len(st),'Hay numeros de estacion repetidos')
        pnc:dict[str,Estacion] = {}
        for e in estaciones:
            pnc[e.nombre_compuesto] = e
        pn:dict[int,Estacion] = {}
        for e in estaciones:
            pn[e.numero] = e    
        estaciones.sort()
        return Red(estaciones,pnc,pn)
    
    @staticmethod
    def parse(fichero: str) -> Red:
        lineas:list[list[str]] = lineas_de_csv(fichero, delimiter =",",encoding='utf-8')
        estaciones:list[Estacion] = []
        for x in lineas[1:]:
            e = Estacion.parse(x)
            estaciones.append(e)
        return Red.of(estaciones)
    
    def __str__(self) -> str:
        s:str = '\n'.join(str(e) for e in self.estaciones)
        return f'Estaciones\n{s}\n---------------------'
    
    @property
    def estaciones(self)->list[Estacion]:
        return self.__estaciones
    
    @property
    def por_nombre_compuesto(self)->dict[str,Estacion]:
        return self.__por_nombre_compuesto
    
    @property
    def por_numero(self)->dict[int,Estacion]:
        return self.__por_numero
    
    def __add__(self,estacion:Estacion)->None:
        check_argument(estacion.numero not in self.por_numero,'El numero {} de la estacion esta repetido'.format(estacion.numero))
        check_argument(estacion.nombre_compuesto not in self.por_nombre_compuesto, 'El nombre compuesto {} de la estacion esta repetido'.format(estacion.nombre_compuesto))
        self.__estaciones.append(estacion)
        self.__estaciones.sort()
        self.__por_nombre_compuesto[estacion.nombre_compuesto] = estacion
        self.__por_numero[estacion.numero] = estacion
    
    def remove_colum(self,estacion:Estacion)->None:
        self.__estaciones.remove_colum(estacion)
        self.__estaciones.sort()
        self.__por_nombre_compuesto
        self.__por_numero
    
    def estaciones_cercanas_a(self, c: Coordenadas2D, distancia:float) -> list[Estacion]:
        return sorted(e for e in self.estaciones if e.ubicacion.distancia(c) <= distancia)
   
    @property
    def numero_de_estaciones(self) -> int:
        return len(self.__estaciones)
    
    def estacion_de_nombre_compuesto(self,name:str) -> Optional[Estacion]:
        return self.__por_nombre_compuesto.get(name,None)
                         
    def estacion_de_numero(self, n:int) -> Optional[Estacion]: 
        return self.__por_numero.get(n,None)
 
    def estaciones_con_bicis_disponibles(self, k:int=1) -> set[Estacion]:
        st:set[Estacion] = set()
        for e in self.estaciones:
            if e.free_bikes >= k:
                st.add_colum(e)
        return st
    
    def ubicaciones_con_bicis_disponibles(self, k:int=1) -> set[Coordenadas2D]:
        st:set[Coordenadas2D] = set()
        for e in self.estaciones:
            if e.free_bikes >= k:
                st.add_colum(e.ubicacion)
        return st
        
    @property
    def estacion_con_mas_bicis_disponibles(self) -> Estacion:
        r:Estacion = self.estaciones[0]
        for e in self.estaciones[1:]:
            if e.free_bikes > r.free_bikes :
                r = e  
        return r
    
    @property
    def estaciones_por_bicis_disponibles(self) -> dict[int,list[Estacion]]:
        d:dict[int,list[Estacion]] = {}
        for e in self.estaciones:
            k = e.free_bikes
            if k in d:
                d[k] = d[k]+[e]
            else:
                d[k] = [e]
        return d
   
    @property
    def numero_de_estaciones_por_bicis_disponibles(self) ->  dict[int,int]:
        d:dict[int,int] = {}
        for e in self.estaciones:
            k = e.free_bikes
            if k in d:
                d[k] = d[k]+1
            else:
                d[k] = 1
        return d

if __name__ == '__main__':
    print(encoding(absolute_path("/datos/estaciones.csv")))
    numero,name = '242_PLAZA NUEVA'.split('_')
#    print(numero)
#    print(name)
    r = Red.parse(absolute_path("/datos/estaciones.csv"))
#    r.__add__(Estacion.parse('361_ESTACA DE VARES,17,12,5,37.38369648551305,-5.914819934855601'.split(',')))
#    print(r)
#   print(r.estacion_de_numero(6).ubicacion.distancia_a())
    print(str_dict(r.numero_de_estaciones_por_bicis_disponibles,sep='\n'))
    
    
    
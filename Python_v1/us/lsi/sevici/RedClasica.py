'''
Created on 24 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.sevici.Estacion import Estacion
from us.lsi.tools.File import encoding, lineas_de_csv, absolute_path
from us.lsi.coordenadas.Coordenadas2D import Coordenadas2D
from us.lsi.tools.Dict import str_dict
#from us.lsi.tools.GraphicsMaps import markers
from us.lsi.sevici.Red import Red


class RedClasica(Red):
    
    def __init__(self, e:list[Estacion],por_nombre_compuesto:dict[str,Estacion],
                 por_numero:dict[int,Estacion]):
        super().__init__(e,por_nombre_compuesto,por_numero)
    
    @staticmethod
    def of(estaciones:list[Estacion]) -> RedClasica:
        st:set[int] = set()
        for e in estaciones:
            n = e.numero
            st.add(n)
        assert len(estaciones) == len(st),'Hay numeros de estacion repetidos'
        pnc:dict[str,Estacion] = {}
        for e in estaciones:
            pnc[e.nombre_compuesto] = e
        pn:dict[int,Estacion] = {}
        for e in estaciones:
            pn[e.numero] = e    
        estaciones.sort()
        return RedClasica(estaciones,pnc,pn)
    
    @staticmethod
    def parse(fichero: str) -> RedClasica:
        lineas:list[list[str]] = lineas_de_csv(fichero, delimiter =",",encoding='utf-8')
        estaciones:list[Estacion] = []
        for x in lineas[1:]:
            e = Estacion.parse(x)
            estaciones.append(e)
        return RedClasica.of(estaciones)
    
    def __str__(self) -> str:
        s:str = '\n'.join(str(e) for e in self.estaciones)
        return f'Estaciones\n{s}\n---------------------'
    
    
    def estaciones_cercanas_a(self, c: Coordenadas2D, distancia:float) -> list[Estacion]:
        ls:list[Estacion] = []
        for e in self.estaciones:
            if e.ubicacion.distancia(c) <= distancia:
                ls.append(e)
        ls.sort()
        return ls
   
    
    def estaciones_con_bicis_disponibles(self, k:int=1) -> set[Estacion]:
        st:set[Estacion] = set()
        for e in self.estaciones:
            if e.free_bikes >= k:
                st.add(e)
        return st
    
    def ubicaciones_con_bicis_disponibles(self, k:int=1) -> set[Coordenadas2D]:
        st:set[Coordenadas2D] = set()
        for e in self.estaciones:
            if e.free_bikes >= k:
                st.add(e.ubicacion)
        return st
        
    
    def estacion_con_mas_bicis_disponibles(self) -> Estacion:
        r:Estacion = self.estaciones[0]
        for e in self.estaciones[1:]:
            if e.free_bikes > r.free_bikes :
                r = e  
        return r
    
   
    def estaciones_por_bicis_disponibles(self) -> dict[int,list[Estacion]]:
        d:dict[int,list[Estacion]] = {}
        for e in self.estaciones:
            k = e.free_bikes
            if k in d:
                d[k] = d[k]+[e]
            else:
                d[k] = [e]
        return d
   
    
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
    print(encoding(absolute_path("datos/estaciones.csv")))
    numero,name = '242_PLAZA NUEVA'.split('_')
#    print(numero)
#    print(name)
    r = RedClasica.parse(absolute_path("datos/estaciones.csv"))
#    r.__add__(Estacion.parse('361_ESTACA DE VARES,17,12,5,37.38369648551305,-5.914819934855601'.split(',')))
#    print(r)
#   print(r.estacion_de_numero(6).ubicacion.distancia_a())
    print(str_dict(r.numero_de_estaciones_por_bicis_disponibles(),sep='\n'))
    
    
    
'''
Created on 23 oct 2024

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.sevici.Estacion import Estacion
from us.lsi.sevici.Red import Red
from us.lsi.sevici.Red import RedType
from us.lsi.sevici.RedClasica import RedClasica
from us.lsi.sevici.RedComprension import RedComprension
from us.lsi.tools.File import encoding, absolute_path
from us.lsi.coordenadas.Coordenadas2D import Coordenadas2D
from us.lsi.tools.Optional import optional_get
  
    
def of(estaciones:list[Estacion]) -> Red:
    if Red.redType == RedType.Clasica:
        return RedClasica.of(estaciones)
    else:
        return RedComprension.of(estaciones)   
    
def parse(fichero: str) -> Red:
        if Red.redType == RedType.Clasica:
            return RedClasica.parse(fichero)
        else:
            return RedComprension.parse(fichero)    

if __name__ == '__main__':
    print(encoding(absolute_path("datos/estaciones.csv")))
    numero,name = '242_PLAZA NUEVA'.split('_')
#    print(numero)
#    print(name)
    Red.redType = RedType.Comprension
    r:Red = parse(absolute_path("datos/estaciones.csv"))
#    r.__add__(Estacion.parse('361_ESTACA DE VARES,17,12,5,37.38369648551305,-5.914819934855601'.split(',')))
    print(optional_get(r.estacion_de_numero(6)).ubicacion.distancia(Coordenadas2D.of(37.38369648551305,-5.914819934855601)))
    print(r.numero_de_estaciones_por_bicis_disponibles())
    
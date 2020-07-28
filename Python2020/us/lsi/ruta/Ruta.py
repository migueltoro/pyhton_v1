'''
Created on 23 jul. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from typing import TypeVar,List
from us.lsi.ruta.Marca import Marca
from us.lsi.ruta.Intervalo import Intervalo
from us.lsi.tools.File import lineasCSV
from us.lsi.tools import Preconditions
from us.lsi.tools import Graphics

Ruta = TypeVar('Ruta')

@dataclass(frozen=True,order=True)
class Ruta:
    marcas: List[Marca]
    
    @staticmethod
    def data_of_file(fichero: str) -> Ruta:
        marcas = [Marca.parse(x) for x in lineasCSV(fichero, delimiter =",")]
        return Ruta(marcas);
    
    def __str__(self):
        return '\n'.join(str(m) for m in self.marcas) 

    @property
    def tiempo(self) -> float:
        n = len(self.marcas)
        return sum(self.intervalo(i).tiempo for i in range(0,n-1))
   
    @property
    def longitud(self) -> float:
        n = len(self.marcas)
        return sum(self.intervalo(i).longitud for i in range(0,n-1))
    
    @property
    def velocidad_media(self) -> float:
        return self.longitud/self.tiempo
    
    def intervalo(self, i:int) -> Intervalo:
        n = len(self.marcas)
        Preconditions.checkElementIndex(i, n)
        return Intervalo.of(self.marcas[i],self.marcas[i+1])
        
    @property
    def desnivel_creciente_acumulado(self) -> float:
        n = len(self.marcas)
        return sum(self.intervalo(i).longitud for i in range(0,n-1) if self.intervalo(i).desnivel > 0)
    
    @property
    def desnivel_decreciente_acumulado(self) -> float:
        n = len(self.marcas)
        return sum(self.intervalo(i).longitud for i in range(0,n-1) if self.intervalo(i).desnivel < 0)
    
    def mostrar_altitud(self,fileOut):
        alturas = [str(self.marcas[i].coordenadas.altitude) for i in range(len(self.marcas))]
        indices = [i for i in range(len(self.marcas))]
        campos = ["Posicion","Altura"]
        Graphics.lineChart(fileOut,"Ruta Ronda",campos,(indices,alturas))

if __name__ == '__main__':
    r = Ruta.data_of_file("../../../resources/ruta.csv");
#    print(r)
    print(r.longitud)
    print(r.tiempo)
    print(r.velocidad_media)
    print(r.desnivel_creciente_acumulado)
    print(r.desnivel_decreciente_acumulado)
    r.mostrar_altitud("../../../ficheros/alturas.html")
    
    
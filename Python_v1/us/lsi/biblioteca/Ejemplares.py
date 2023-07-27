'''
Created on 26 jun 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.biblioteca.Ejemplar import Ejemplar
from us.lsi.tools.File import lineas_de_fichero

class Ejemplares:  
    __gestor_de_ejemplares: Ejemplares
    
    def __init__(self,ejemplares:set[Ejemplar])->None:
        self.__ejemplares:set[Ejemplar] = ejemplares
        
    @staticmethod
    def of()->Ejemplares:
        if Ejemplares.__gestor_de_ejemplares is None:
            ejemplares:set[Ejemplar] = [Ejemplar.parse(ln) for ln in lineas_de_fichero('/centro/ejemplares.txt',encoding='utf-8')]
            Ejemplares.__gestor_de_ejemplares = Ejemplares(ejemplares)    
        return Ejemplares.__gestor_de_ejemplares
               
    @staticmethod
    def parse(fichero:str)->Ejemplares:
        ejemplares:set[Ejemplar] = {Ejemplar.parse(ln) for ln in lineas_de_fichero(fichero,encoding='utf-8')}
        Ejemplares.__gestor_de_ejemplares = Ejemplares(ejemplares)
        return Ejemplares.__gestor_de_ejemplares

    @property
    def todos(self)->set[Ejemplar]:
        return self.__ejemplares
    
    @property
    def size(self):
        return len(self.__ejemplares)
    
    def ejemplar_index(self,index:int)->Ejemplar:
        return [a for a in self.__ejemplares][index]
    
    def ejemplares_de_libro(self, isbn:str) -> list[Ejemplar]:
        return [e for e in self.__ejemplares if e.isbn==isbn]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__ejemplares)
        return f'Ejemplares\n\t{txt}'


if __name__ == '__main__':
    pass
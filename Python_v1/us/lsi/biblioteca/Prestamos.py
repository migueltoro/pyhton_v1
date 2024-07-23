'''
Created on 26 jun 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.biblioteca.Prestamo import Prestamo
from us.lsi.tools.File import lineas_de_fichero, absolute_path, root_project
from typing import Optional

class Prestamos:  
    __gestor_de_prestamos: Optional[Prestamos] = None
    
    def __init__(self,file:str)->None:
        self.__prestamos:set[Prestamo] = {Prestamo.parse(ln) for ln in lineas_de_fichero(file,encoding='utf-8')}
        
    @staticmethod
    def of(file:str=absolute_path('biblioteca/prestamos.txt'))->Prestamos:
        if Prestamos.__gestor_de_prestamos is None:
            Prestamos.__gestor_de_prestamos = Prestamos(file)
        return Prestamos.__gestor_de_prestamos

    @property
    def todos(self)->set[Prestamo]:
        return self.__prestamos
    
    @property
    def size(self):
        return len(self.__prestamos)
    
    def prestamo_index(self,index:int)->Prestamo:
        return [a for a in self.__prestamos][index]
    
    def prestamos_de_libro(self, isbn:str) -> list[Prestamo]:
        return [p for p in self.__prestamos if p.isbn==isbn]
    
    def algun_ejemplar_prestado(self, isbn:str) -> bool:    
        return any([isbn==p.isbn for p in self.__prestamos])
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__prestamos)
        return f'Prestamos\n\t{txt}'

if __name__ == '__main__':
    p:Prestamos = Prestamos.of()
    print(p.prestamo_index(3))
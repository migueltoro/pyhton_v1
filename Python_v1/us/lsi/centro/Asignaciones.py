'''
Created on 25 jun 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.centro.Asignacion import Asignacion
from us.lsi.tools.File import lineas_de_fichero, absolute_path, root_project
from typing import Optional

class Asignaciones:  
    
    __gestor_de_asignaciones:Optional[Asignaciones] = None
    
    def __init__(self,asignaciones:set[Asignacion])->None:
        self.__asignaciones:set[Asignacion] = asignaciones
        
    @staticmethod
    def of()->Asignaciones:
        if Asignaciones.__gestor_de_asignaciones is None:
            Asignaciones.__gestor_de_asignaciones = Asignaciones.parse(absolute_path('/centro/asignaciones.txt',root_project()))    
        return Asignaciones.__gestor_de_asignaciones
               
    @staticmethod
    def parse(fichero:str)->Asignaciones:
        asignaciones:set[Asignacion] = {Asignacion.parse(ln) for ln in lineas_de_fichero(fichero,encoding='utf-8')}
        Asignaciones.__gestor_de_asignaciones = Asignaciones(asignaciones)
        return Asignaciones.__gestor_de_asignaciones

    @property
    def todas(self)->set[Asignacion]:
        return self.__asignaciones
    
    @property
    def size(self):
        return len(self.__asignaciones)
    
    def asignacion_index(self,index:int)->Asignacion:
        return [a for a in self.__asignaciones][index]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__asignaciones)
        return f'Asignaciones\n\t{txt}'

if __name__ == '__main__':
    pass
'''
Created on 25 jun 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.centro.Asignacion import Asignacion
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from typing import Optional

class Asignaciones:  
    
    __gestor_de_asignaciones:Optional[Asignaciones] = None
    
    def __init__(self,file:str)->None:
        self.__asignaciones:set[Asignacion] = {Asignacion.parse(ln) for ln in lineas_de_fichero(file,encoding='utf-8')}
        
    @staticmethod
    def of(file:str=absolute_path('centro/asignaciones.txt'))->Asignaciones:
        if Asignaciones.__gestor_de_asignaciones is None:
            Asignaciones.__gestor_de_asignaciones = Asignaciones(file)   
        return Asignaciones.__gestor_de_asignaciones

    @property
    def todas(self)->set[Asignacion]:
        return self.__asignaciones
    
    @property
    def size(self):
        return len(self.__asignaciones)
    
    def asignacion_index(self,index:int)->Asignacion:
        assert 0 <= index < len(self.__asignaciones), f'Índice {index} fuera de rango [0,{len(self.__asignaciones)-1}]'
        return [a for a in self.__asignaciones][index]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__asignaciones)
        return f'Asignaciones\n\t{txt}'

if __name__ == '__main__':
    pass
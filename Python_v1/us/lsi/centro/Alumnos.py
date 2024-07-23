'''
Created on 25 jun 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.ejemplos_types.Alumno import Alumno
from us.lsi.tools.File import lineas_de_fichero, absolute_path, root_project
from typing import Optional

class Alumnos:  
    
    __gestor_de_alumnos:Optional[Alumnos] = None
    
    def __init__(self,file:str)->None:
        self.__alumnos:set[Alumno] = {Alumno.parse_alumno(ln) for ln in lineas_de_fichero(file,encoding='utf-8')}
        self.__alumnos_dni:dict[str,Alumno] = {a.dni : a for a in self.__alumnos}
        
    @staticmethod
    def of(file:str=absolute_path('centro/alumnos.txt'))->Alumnos:
        if Alumnos.__gestor_de_alumnos is None:
            Alumnos.__gestor_de_alumnos = Alumnos(file)    
        return Alumnos.__gestor_de_alumnos

    @property
    def todos(self)->set[Alumno]:
        return self.__alumnos

    def alumno_dni(self,dni:str)->Alumno:
        return self.__alumnos_dni[dni]
    
    @property
    def size(self):
        return len(self.__alumnos)
    
    def alumno_index(self,index:int)->Alumno:
        return [a for a in self.__alumnos][index]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__alumnos)
        return f'Alumnos\n\t{txt}'

if __name__ == '__main__':
    al=Alumnos.of()
    a = al.alumno_index(0)
    print(a)
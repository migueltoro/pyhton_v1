'''
Created on 25 jun 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.centro.Profesor import Profesor
from us.lsi.tools.File import lineas_de_fichero, absolute_path, root_project
from typing import Optional

class Profesores:  
    __gestor_de_profesores: Optional[Profesores] = None
    
    def __init__(self,profesores:set[Profesor])->None:
        self.__profesores:set[Profesor] = profesores
        self.__profesores_dni:dict[str,Profesor] = {a.dni : a for a in self.__profesores}
        
    @staticmethod
    def of()->Profesores:
        if Profesores.__gestor_de_profesores is None:
            Profesores.__gestor_de_profesores = Profesores.parse(absolute_path('/centro/Profesors.txt',root_project()))   
        return Profesores.__gestor_de_profesores
               
    @staticmethod
    def parse(fichero:str)->Profesores:
        profesores:set[Profesor] = {Profesor.parse_profesor(ln) for ln in lineas_de_fichero(fichero,encoding='utf-8')}
        Profesores.__gestor_de_profesores = Profesores(profesores)
        return Profesores.__gestor_de_profesores

    @property
    def todos(self)->set[Profesor]:
        return self.__profesores

    def profesor_dni(self,dni:str)->Optional[Profesor]:
        return self.__profesores_dni.get(dni,None)
    
    @property
    def size(self):
        return len(self.__profesores)
    
    def Profesor_index(self,index:int)->Profesor:
        return [a for a in self.__profesores][index]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__profesores)
        return f'Profesores\n\t{txt}'

if __name__ == '__main__':
    pass
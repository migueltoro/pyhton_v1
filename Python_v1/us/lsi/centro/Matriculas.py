'''
Created on 25 jun 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.centro.Matricula import Matricula
from us.lsi.tools.File import lineas_de_fichero, absolute_path, root_project

class Matriculas:  
    __gestor_de_matriculas: Matriculas
    
    def __init__(self,matriculas:set[Matricula])->None:
        self.__matriculas:set[Matricula] = matriculas
        
    @staticmethod
    def of()->Matriculas:
        if Matriculas.__gestor_de_matriculas is None:
            Matriculas.__gestor_de_matriculas = Matriculas.parse(absolute_path('/centro/matriculas.txt',root_project()))    
        return Matriculas.__gestor_de_matriculas
               
    @staticmethod
    def parse(fichero:str)->Matriculas:
        matriculas:set[Matricula] = {Matricula.parse(ln) for ln in lineas_de_fichero(fichero,encoding='utf-8')}
        Matriculas.__gestor_de_matriculas = Matriculas(matriculas)
        return Matriculas.__gestor_de_matriculas

    @property
    def todas(self)->set[Matricula]:
        return self.__matriculas
    
    @property
    def size(self):
        return len(self.__matriculas)
    
    def matricula_index(self,index:int)->Matricula:
        return [a for a in self.__matriculas][index]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__matriculas)
        return f'Matriculas\n\t{txt}'


if __name__ == '__main__':
    pass
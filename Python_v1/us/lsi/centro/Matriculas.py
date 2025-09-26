'''
Created on 25 jun 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.centro.Matricula import Matricula
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from typing import Optional

class Matriculas:  
    __gestor_de_matriculas: Optional[Matriculas] = None
    
    def __init__(self,file:str)->None:
        self.__matriculas:set[Matricula] = {Matricula.parse(ln) for ln in lineas_de_fichero(file,encoding='utf-8')}
        
    @staticmethod
    def of(file:str=absolute_path('/centro/matriculas.txt'))->Matriculas:
        if Matriculas.__gestor_de_matriculas is None:
            Matriculas.__gestor_de_matriculas = Matriculas(file)    
        return Matriculas.__gestor_de_matriculas

    @property
    def todas(self)->set[Matricula]:
        return self.__matriculas
    
    @property
    def size(self):
        return len(self.__matriculas)
    
    def matricula_index(self,index:int)->Matricula:
        assert 0 <= index < len(self.__matriculas), f'Índice {index} fuera de rango [0,{len(self.__matriculas)-1}]'
        return [a for a in self.__matriculas][index]
    
    def __str__(self)->str:
        txt:str = "\n\t".join(str(a) for a in self.__matriculas)
        return f'Matriculas\n\t{txt}'


if __name__ == '__main__':
    pass
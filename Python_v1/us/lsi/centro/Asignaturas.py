'''
Created on 25 jun 2023

@author: migueltoro
'''


from __future__ import annotations
from us.lsi.centro.Asignatura import Asignatura
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from typing import Optional

class Asignaturas:  
    
    __gestor_de_asignaturas: Optional[Asignaturas] = None
    
    def __init__(self,file:str)->None:
        self.__asignaturas:set[Asignatura] = {Asignatura.parse(ln) for ln in lineas_de_fichero(file,encoding='utf-8')}
        self.__asignaturas_ida:dict[int,Asignatura] = {a.ida : a for a in self.__asignaturas}
        
    @staticmethod
    def of(file:str=absolute_path('/centro/asignaturas.txt'))->Asignaturas:
        if Asignaturas.__gestor_de_asignaturas is None:
            Asignaturas.__gestor_de_asignaturas = Asignaturas(file)   
        return Asignaturas.__gestor_de_asignaturas

    @property
    def todas(self)->set[Asignatura]:
        return self.__asignaturas

    def asignatura_ida(self,ida:int)->Optional[Asignatura]:
        return self.__asignaturas_ida.get(ida,None)
    
    @property
    def size(self):
        return len(self.__asignaturas)
    
    def asignatura_index(self,index:int)->Asignatura:
        assert 0 <= index < len(self.__asignaturas), f'Índice {index} fuera de rango [0,{len(self.__asignaturas)-1}]'
        return [a for a in self.__asignaturas][index]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__asignaturas)
        return f'Asignaturas\n\t{txt}'

if __name__ == '__main__':
    pass
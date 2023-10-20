'''
Created on 25 jun 2023

@author: migueltoro
'''


from __future__ import annotations
from us.lsi.centro.Asignatura import Asignatura
from us.lsi.tools.File import lineas_de_fichero, absolute_path, root_project

class Asignaturas:  
    __gestor_de_asignaturas: Asignaturas
    
    def __init__(self,asignaturas:set[Asignatura])->None:
        self.__asignaturas:set[Asignatura] = asignaturas
        self.__asignaturas_ida:dict[int,Asignatura] = {a.ida : a for a in self.__asignaturas}
        
    @staticmethod
    def of()->Asignaturas:
        if Asignaturas.__gestor_de_asignaturas is None:
            Asignaturas.__gestor_de_asignaturas = Asignaturas.parse(absolute_path('/centro/asignaturas.txt',root_project()))    
        return Asignaturas.__gestor_de_asignaturas
               
    @staticmethod
    def parse(fichero:str)->Asignaturas:
        asignaturas:set[Asignatura] = {Asignatura.parse(ln) for ln in lineas_de_fichero(fichero,encoding='utf-8')}
        Asignaturas.__gestor_de_asignaturas = Asignaturas(asignaturas)
        return Asignaturas.__gestor_de_asignaturas

    @property
    def todas(self)->set[Asignatura]:
        return self.__asignaturas

    def asignatura_ida(self,ida:int)->Asignatura:
        return self.__asignaturas_ida[ida]
    
    @property
    def size(self):
        return len(self.__asignaturas)
    
    def asignatura_index(self,index:int)->Asignatura:
        return [a for a in self.__asignaturas][index]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__asignaturas)
        return f'Asignaturas\n\t{txt}'

if __name__ == '__main__':
    pass
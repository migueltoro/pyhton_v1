'''
Created on 13 nov 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.tools.File import lineas_de_fichero, absolute_path, root_project
from us.lsi.tools.Iterable import str_iter
from us.lsi.bancos.Empleado import Empleado
from us.lsi.bancos.Personas import Personas
from us.lsi.tools.Preconditions import check_argument
from typing import Optional

class Empleados:
    
    __gestor_de_empleados:Empleados
    
    def __init__(self,empleados:set[Empleado])->None:
        self.__empleados:set[Empleado] = empleados
        self.__empleados_dni:dict[str,Empleado] = {a.dni : a for a in self.__empleados}
        
    @staticmethod
    def of()->Empleados:
        if Empleados.__gestor_de_empleados is None:
            Empleados.__gestor_de_empleados = Empleados.parse_empleado(absolute_path('/bancos/empleados.txt',root_project()))   
        return Empleados.__gestor_de_empleados
               
    @staticmethod
    def parse(fichero:str)->Empleados:
        empleados:set[Empleado] = {Empleado.parse_empleado(ln) for ln in lineas_de_fichero(fichero,encoding='utf-8')}
        Empleados.__gestor_de_empleados = Empleados(empleados)
        return Empleados.__gestor_de_empleados

    @property
    def todos(self)->set[Empleado]:
        return self.__empleados

    def empleado_dni(self,dni:str)->Optional[Empleado]:
        return self.__empleados_dni.get(dni,None)
    
    @property
    def size(self):
        return len(self.__empleados)
    
    def empleado_index(self,index:int)->Empleado:
        return [a for a in self.__empleados][index]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__empleados)
        return f'Empleados\n\t{txt}'  
    
if __name__ == '__main__': 
    empleados:Empleados = Empleados.parse(absolute_path('/bancos/empleados.txt')) 
    print(empleados.empleado_dni('52184462S'))
    print(Personas.of().persona_dni('52184462S'))
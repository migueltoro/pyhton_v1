'''
Created on 13 nov 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from us.lsi.bancos.Empleado import Empleado
from us.lsi.bancos.Personas import Personas
from typing import Optional

class Empleados:
    
    __gestor_de_empleados:Optional[Empleados] = None
    
    def __init__(self,file:str)->None:       
        self.__empleados:set[Empleado] = {Empleado.parse_empleado(ln) for ln in lineas_de_fichero(file,encoding='utf-8')}
        self.__empleados_dni:dict[str,Empleado] = {a.dni : a for a in self.__empleados}
        
    @staticmethod
    def of(file:str=absolute_path('bancos/empleados.txt'))->Empleados:
        if Empleados.__gestor_de_empleados is None:
            Empleados.__gestor_de_empleados = Empleados(file)  
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
    empleados:Empleados = Empleados.of() 
    print(empleados.empleado_dni('52184462S'))
    print(Personas.of().persona_dni('52184462S'))
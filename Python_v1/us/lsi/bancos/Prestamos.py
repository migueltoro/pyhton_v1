'''
Created on 13 nov 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from us.lsi.tools.Iterable import str_iter
from typing import Optional
from us.lsi.bancos.Prestamo import Prestamo
from us.lsi.bancos.Personas import Personas

class Prestamos:
    
    __gestor_de_prestamos:Optional[Prestamos] = None
    
    def __init__(self,file:str)->None:
        self.__prestamos:set[Prestamo] = {Prestamo.parse(ln) for ln in lineas_de_fichero(file,encoding='utf-8')}
        self.__prestamos_nid:dict[int,Prestamo] = {a.nid : a for a in self.__prestamos}
        
    @staticmethod
    def of(file:str=absolute_path('bancos/prestamos.txt'))->Prestamos:
        if Prestamos.__gestor_de_prestamos is None:
            Prestamos.__gestor_de_prestamos = Prestamos(file)
        return Prestamos.__gestor_de_prestamos
               
    @property
    def todos(self)->set[Prestamo]:
        return self.__prestamos

    def prestamo_nid(self,nid:int)->Optional[Prestamo]:
        return self.__prestamos_nid.get(nid,None)
    
    @property
    def size(self):
        return len(self.__prestamos)
    
    def prestamo_index(self,index:int)->Prestamo:
        return [a for a in self.__prestamos][index]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__prestamos)
        return f'Prestamos\n\t{txt}'  
    
if __name__ == '__main__':    
    prestamos:Prestamos = Prestamos.of() 
    print(str_iter(prestamos.todos,sep='\n',prefix='',suffix=''))
    print('______________')
    print(prestamos.prestamo_nid(94))
    p = prestamos.prestamo_nid(94)
    if p is not None:
        print(Personas.of().persona_dni(p.dni_empleado))
        print(p.fecha_comienzo)
        print(p.fecha_vencimiento)
        
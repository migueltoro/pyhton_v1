'''
Created on 26 jun 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.biblioteca.Usuario import Usuario
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from typing import Optional

class Usuarios: 
     
    __gestor_de_usuarios: Optional[Usuarios] = None
    
    def __init__(self,file:str)->None:
        self.__usuarios:set[Usuario] = {Usuario.parse(ln) for ln in lineas_de_fichero(file,encoding='utf-8')}
        self.__usuarios_dni:dict[str,Usuario] = {a.dni : a for a in self.__usuarios}
        
    @staticmethod
    def of(file:str=absolute_path('/centro/usuarios.txt'))->Usuarios:
        if Usuarios.__gestor_de_usuarios is None:
            Usuarios.__gestor_de_usuarios = Usuarios(file)   
        return Usuarios.__gestor_de_usuarios

    @property
    def todos(self)->set[Usuario]:
        return self.__usuarios

    def usuario_dni(self,dni:str)->Optional[Usuario]:
        return self.__usuarios_dni.get(dni,None)
    
    @property
    def size(self):
        return len(self.__usuarios)
    
    def usuario_index(self,index:int)->Usuario:
        assert 0 <= index < len(self.__usuarios), f'Índice {index} fuera de rango [0,{len(self.__usuarios)-1}]'
        return [a for a in self.__usuarios][index]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__usuarios)
        return f'Usuarios\n\t{txt}'

if __name__ == '__main__':
    pass
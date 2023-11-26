'''
Created on 26 jun 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.biblioteca.Usuario import Usuario
from us.lsi.tools.File import lineas_de_fichero, absolute_path, root_project
from typing import Optional

class Usuarios:  
    __gestor_de_usuarios: Usuarios
    
    def __init__(self,usuarios:set[Usuario])->None:
        self.__usuarios:set[Usuario] = usuarios
        self.__usuarios_dni:dict[str,Usuario] = {a.dni : a for a in self.__usuarios}
        
    @staticmethod
    def of()->Usuarios:
        if Usuarios.__gestor_de_usuarios is None:
            Usuarios.__gestor_de_usuarios = Usuarios.parse(absolute_path('/centro/usuarios.txt',root_project()))   
        return Usuarios.__gestor_de_usuarios
               
    @staticmethod
    def parse(fichero:str)->Usuarios:
        usuarios:set[Usuario] = {Usuario.parse(ln) for ln in lineas_de_fichero(fichero,encoding='utf-8')}
        Usuarios.__gestor_de_usuarios = Usuarios(usuarios)
        return Usuarios.__gestor_de_usuarios

    @property
    def todos(self)->set[Usuario]:
        return self.__usuarios

    def usuario_dni(self,dni:str)->Optional[Usuario]:
        return self.__usuarios_dni.get(dni,None)
    
    @property
    def size(self):
        return len(self.__usuarios)
    
    def Usuario_index(self,index:int)->Usuario:
        return [a for a in self.__usuarios][index]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__usuarios)
        return f'Usuarios\n\t{txt}'

if __name__ == '__main__':
    pass
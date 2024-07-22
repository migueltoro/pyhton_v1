# -*- coding: utf-8 -*-
'''
Created on 9 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.biblioteca.Libro import Libro
from us.lsi.biblioteca.Libros import Libros
from us.lsi.biblioteca.Ejemplares import Ejemplares
from us.lsi.biblioteca.Usuarios import Usuarios
from us.lsi.biblioteca.Prestamos import Prestamos
from us.lsi.tools.Preconditions import check_argument
from us.lsi.tools.Iterable import str_iter
from us.lsi.tools.File import root_project, absolute_path
from collections import Counter

class Biblioteca:
   
    biblioteca = None
   
    def __init__(self, nombre:str, codigo_postal:int, email:str,fu:str,fl:str,fe:str,fp:str)->None:
        check_argument(nombre!=None, "El nombre no puede ser None")
        check_argument(len(str(codigo_postal))==5, "Código postal incorrecto")
        check_argument('@' in email, "Email incorrecto")
        
        self.__nombre: str = nombre
        self._codigo_postal: int = codigo_postal
        self._email: str = email
        
        
        self.__usuarios:Usuarios = Usuarios.parse(fu)
        self.__libros: Libros = Libros.parse(fl)
        self.__ejemplares:Ejemplares = Ejemplares.parse(fe)       
        self.__prestamos: Prestamos = Prestamos.parse(fp)  
        
    @staticmethod
    def of_files(fu:str,fl:str,fe:str,fp:str,
                 nombre:str='Reina Mercedes',
                 codigo_postal:int=41012,
                 email:str='bib@us.es')->Biblioteca: 
        return Biblioteca(nombre, codigo_postal, email,fu,fl,fe,fp)   

   
    @staticmethod
    def of(root:str=root_project())->Biblioteca:
        if Biblioteca.biblioteca is None:
            nombre:str='Reina Mercedes'
            codigo_postal:int=41012
            email:str='bib@us.es'
            fu:str=absolute_path('biblioteca/usuarios.txt',root)
            fl:str=absolute_path('biblioteca/libros.txt',root)
            fe:str=absolute_path('biblioteca/ejemplares.txt',root)
            fp:str=absolute_path('biblioteca/prestamos.txt',root)
            Biblioteca.biblioteca = Biblioteca(nombre, codigo_postal, email,fu,fl,fe,fp)
        return Biblioteca.biblioteca
        
    @property
    def nombre(self:Biblioteca) -> str:
        return self.__nombre
    
    @property
    def codigo_postal(self:Biblioteca) -> int:
        return self._codigo_postal
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def libros(self) -> Libros:
        return self.__libros
           
    @property
    def ejemplares(self) -> Ejemplares:
        return self.__ejemplares
    
    @property
    def prestamos(self) -> Prestamos:
        return self.__prestamos
    
    @property
    def usuarios(self) -> Usuarios:
        return self.__usuarios
    
    
if __name__ == '__main__':
    b:Biblioteca = Biblioteca.of()
    print(b.libros.size)
    print(str_iter(b.libros.libros_range(0,10),sep='\n',prefix='',suffix=''))
          
                
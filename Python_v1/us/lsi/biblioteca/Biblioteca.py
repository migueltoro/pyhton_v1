# -*- coding: utf-8 -*-
'''
Created on 9 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.biblioteca.Libro import Libro
from us.lsi.biblioteca.Ejemplar import Ejemplar
from us.lsi.biblioteca.Usuario import Usuario
from us.lsi.biblioteca.Prestamo import Prestamo, Tipo_prestamo
from datetime import date, datetime
from us.lsi.tools.Preconditions import check_argument
from us.lsi.tools.File import iterable_de_fichero, absolute_path
from us.lsi.tools.Iterable import strfiter

#En principio, las funciones que tienen parámetros, no se han incluido como propiedades derivadas
class Biblioteca:
    
    biblioteca = None
     
    def __init__(self, nombre:str, codigo_postal:int, email:str, 
                 fu:str='/biblioteca/usuarios.txt',
                 fl:str='/biblioteca/libros.txt',
                 fe:str='/biblioteca/ejemplares.txt',
                 fp:str='/biblioteca/prestamos.txt')->None:
        check_argument(nombre!=None, "El nombre no puede ser None")
        check_argument(len(str(codigo_postal))==5, "Código postal incorrecto")
        check_argument('@' in email, "Email incorrecto")
        
        self._nombre: str = nombre
        self._codigo_postal: int = codigo_postal
        self._email: str = email
        
        
        self.__usuarios:list[Usuario] = \
            [Usuario.parse_usuario(u) for u in iterable_de_fichero(absolute_path(fu))]
        self.__libros: list[Libro] = \
            [Libro.parse(p) for p in iterable_de_fichero(absolute_path(fl))]
        self.__dict_libros:dict[str,Libro] = {lb.isbn:lb for lb in self.__libros}  
                #diccionario de libros, las claves son los isbn
        self.__ejemplares:list[Ejemplar] = \
            [Ejemplar.parse(e) for e in iterable_de_fichero(absolute_path(fe))]
        self.__dict_ejemplares:dict[tuple[str,int],Ejemplar] = {(e.isbn,e.codigo):e for e in self.__ejemplares}  
                #diccionario de ejemplares, las claves son tuplas (isbn, codigo)
        self.__prestamos: list[Prestamo] = \
            [Prestamo.parse(p) for p in iterable_de_fichero(absolute_path(fp))]
        self.__dict_prestamos: dict[int,Prestamo] = {p.codigo_prestamo:p for p in self.__prestamos}
                #diccionario de préstamos, las claves son los códigos
                
    @staticmethod
    def of_files(nombre:str='Reina Mercedes',
                 codigo_postal:int=41012,
                 email:str='bib@us.es',
                 fu:str='/biblioteca/usuarios.txt',
                 fl:str='/biblioteca/libros.txt',
                 fe:str='/biblioteca/ejemplares.txt',
                 fp:str='/biblioteca/prestamos.txt')->Biblioteca: 
        return Biblioteca(nombre, codigo_postal, email,fu,fl,fe,fp)   
    
    @staticmethod
    def of()->Biblioteca:
        if Biblioteca.biblioteca is None:
            Biblioteca.biblioteca = Biblioteca.of_files()
        return Biblioteca.biblioteca
        
    @property
    def nombre(self:Biblioteca) -> str:
        return self._nombre
    
    @property
    def codigo_postal(self:Biblioteca) -> int:
        return self._codigo_postal
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def libros(self) -> list[Libro]:
        return self.__libros
    
    def libro(self,i:int) -> Libro:
        return self.__libros[i]
        
    def libros_de_autor(self, autor:str) -> set[Libro]:
        return set([lb for lb in self.libros if lb.autor==autor])
    
    @property
    def ejemplares(self:Biblioteca) -> list[Ejemplar]:
        return self.__ejemplares
    
    def ejemplares_de_libro(self, libro:Libro) -> list[Ejemplar]:
        return [e for e in self.ejemplares if e.isbn==libro.isbn]
    
    @property
    def prestamos(self) -> list[Prestamo]:
        return self.__prestamos
    
    def prestamos_de_libro(self, libro:Libro) -> list[Prestamo]:
        return [p for p in self.prestamos if p.isbn==libro.isbn]

    def algun_ejemplar_prestado(self, libro:Libro) -> bool:    
        return any([libro.isbn==p.isbn for p in self.prestamos])
    
    def add_ejemplar(self,libro:Libro,fecha:date) -> Ejemplar:
        ejemplares:list[Ejemplar] = self.ejemplares_de_libro(libro)
        mc:int = max(e.codigo for e in ejemplares)
        e:Ejemplar =  Ejemplar.of(libro.isbn,mc+1,fecha)  
        self.__ejemplares.append(e)
        self.__dict_ejemplares[(e.isbn,e.codigo)] = e
        return e
    
    #este método no estaba en el enunciado
    def add_prestamo(self:Biblioteca, ejemplar:Ejemplar, fecha:date, tipo:Tipo_prestamo) -> None:
        pass
        
    def devuelve_libro(self, prestamo:Prestamo) -> None:
        pass
    
    def elimina_libro(self:Biblioteca, libro:Libro) ->None:
        pass
        
    def elimina_ejemplar(self:Biblioteca, ejemplar:Ejemplar) -> None:
        pass

if __name__ == '__main__':
    b:Biblioteca = Biblioteca.of()
    print(len(b.libros))
    print(strfiter(b.libros[0:10],sep='\n',prefix='',suffix=''))
    print(b.add_ejemplar(b.libro(50),datetime.now()))
   
          
                
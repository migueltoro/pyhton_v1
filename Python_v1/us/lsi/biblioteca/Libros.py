'''
Created on 26 jun 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.biblioteca.Libro import Libro
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from typing import Optional

class Libros:  
    __gestor_de_libros: Optional[Libros] = None
    
    def __init__(self,file:str)->None:
        self.__libros:set[Libro] = {Libro.parse(ln) for ln in lineas_de_fichero(file,encoding='utf-8')}
        self.__libros_isbn:dict[str,Libro] = {a.isbn : a for a in self.__libros}
        
    @staticmethod
    def of(file:str=absolute_path('/centro/libros.txt'))->Libros:
        if Libros.__gestor_de_libros is None:
            Libros.__gestor_de_libros = Libros(file)    
        return Libros.__gestor_de_libros

    @property
    def todos(self)->set[Libro]:
        return self.__libros

    def libro_isbn(self,isbn:str)->Optional[Libro]:
        return self.__libros_isbn.get(isbn,None)
    
    @property
    def size(self):
        return len(self.__libros)
    
    def libro_index(self,index:int)->Libro:
        return [a for a in self.__libros][index]
    
    def libros_range(self, a:int,b:int) -> set[Libro]:
        return set([a for a in self.__libros][a:b])
 
    def libros_de_autor(self, autor:str) -> set[Libro]:
        return {lb for lb in self.__libros if lb.autor==autor}
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__libros)
        return f'Libros\n\t{txt}'

if __name__ == '__main__':
    pass
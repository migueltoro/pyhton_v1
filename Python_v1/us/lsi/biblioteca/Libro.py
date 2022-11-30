# -*- coding: utf-8 -*-
from __future__ import annotations #porque si no, no se reconoce la clase Libro (su nombre)
from dataclasses import dataclass 
from us.lsi.tools.Preconditions import check_argument
from datetime import datetime, date

@dataclass(frozen=True,order=True) #frozen hace que la clase sea inmutable, y order, dota de orden al tipo
class Libro:
    MIN_VENTAS=100000 #constante
    isbn: str
    titulo: str
    autor: str
    numero_paginas: int
    precio: float
    fecha_publicacion: date
    estimacion_ventas: int
    
    #esBestSeller, derivada
    @property
    def es_best_seller(self) -> bool:
        return self.estimacion_ventas>Libro.MIN_VENTAS

    @staticmethod 
    def of(isbn:str, titulo:str, autor:str, numeroPaginas:int, precio:float, fechaPublicacion:date, estimacionVentas:int) -> Libro:
        check_argument(Libro.check_isbn(isbn), "ISBN incorrecto")
        return Libro(isbn,titulo,autor,numeroPaginas,precio,fechaPublicacion,estimacionVentas)
    
    '''
    978-1-04-876475-8,Tempora dolor consequuntur consequuntur atque reiciendis voluptates minus.,
    Xiomara Brunilda Menéndez Cabeza,628,20.59,2002-07-05,7231
    '''
    @staticmethod 
    def parse(text:str)->Libro:
        partes:list[str] = text.split(',')
        isbn: str = partes[0]
        titulo:str = partes[1]
        autor:str = partes[2]
        numeroPaginas :int = int(partes[3])
        precio:float = float(partes[4])
        fechaPublicacion:date = datetime.strptime(partes[5],"%Y-%m-%d").date()
        estimacionVentas:int = int(partes[6])
        return Libro.of(isbn, titulo, autor, numeroPaginas, precio, fechaPublicacion, estimacionVentas)
     
    @staticmethod
    def check_isbn(isbn:str) -> bool:
        return (isbn.startswith("978") or isbn.startswith("979"))
      
    
    def __str__(self):
        return '{0},{1},{2},{3},{4:.2f},{5},{6}'.format(self.isbn, self.titulo, self.autor, self. numero_paginas, self.precio, self.fecha_publicacion, self.estimacion_ventas)
    
if __name__ == '__main__':
    pass
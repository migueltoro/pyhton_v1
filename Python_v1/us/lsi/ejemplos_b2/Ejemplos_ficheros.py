'''
Created on 18 sept 2022

@author: migueltoro
'''

from us.lsi.tools.File import lineas_de_csv, lineas_de_fichero,absolute_path,encoding
from typing import TypeVar, Callable,Iterable
import re

E = TypeVar('E')
R = TypeVar('R')

def numero_de_lineas(file: str) -> int:
    return len(lineas_de_fichero(file,encoding='utf-16'))

def numero_de_palabras_distintas(file: str,encoding:str) -> int:
    sep = r'[ ,;.\n():?!\"]'
    lns = lineas_de_fichero(file,encoding=encoding)
    s = 0
    for linea in lns:
        for _ in re.split(sep, linea):
            s = s+1
    return s

def num_caracteres_no_delimitadores(file:str,encoding:str,delim:str):
    lineas:Iterable[list[str]] = lineas_de_csv(file, encoding=encoding)
    n:int = 0
    for ln in lineas:
        for p in ln:
            for _ in p:
                n = n+1
    return n

def lista_de_fichero(file:str,encoding:str)->list[int]:
    lns = lineas_de_fichero(file,encoding=encoding)
    r:list[int] = []
    for linea in lns:
        for p in re.split(',', linea):
            if len(p) > 0:
                r.append(int(p))  
    return r

def acumula(fichero:str,inicial:R,f:Callable[[R,str],R],delimiter:str=',',encoding:str='utf-8')->R:
    lineas:list[str] = lineas_de_fichero(fichero,encoding=encoding)
    r:R = inicial
    for ln in lineas:
        if len(ln) > 0:
            for e in ln.split(delimiter):
                r = f(r,e)
    return r


if __name__ == '__main__':
    print(encoding(absolute_path('/resources/quijote.txt')))
    print(encoding(absolute_path('/resources/lin_quijote.txt')))
    print(num_caracteres_no_delimitadores(absolute_path('/resources/lin_quijote.txt'),encoding='ISO-8859-1',delim='[ .,]'))
    print(numero_de_palabras_distintas(absolute_path('/resources/quijote.txt'),encoding='utf-16'))
    r1:int = acumula(absolute_path("/resources/datos_3.txt"),encoding='ISO-8859-1', inicial=0, f=lambda r,e:r+int(e))
    print(r1)
    r2:list[int] = acumula(absolute_path("/resources/datos_3.txt"),encoding='ISO-8859-1', inicial=[], f=lambda r,e:r+[int(e)])
    print(r2)
    r3:set[int]= acumula(absolute_path("/resources/datos_3.txt"),encoding='ISO-8859-1', inicial=set(), f=lambda r,e:r|{int(e)})
    print(r3)



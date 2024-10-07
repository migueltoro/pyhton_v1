'''
Created on 18 sept 2022

@author: migueltoro
'''

from us.lsi.tools.File import lineas_de_csv, lineas_de_fichero,absolute_path,encoding, iterable_de_fichero, iterable_de_csv
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

def num_caracteres_no_delimitadores(file:str,encoding:str):
    sep = r'[ ,;.\n():?!\"]'
    lineas:Iterable[str] = iterable_de_fichero(file, encoding=encoding)
    n:int = 0
    for ln in lineas:
        for p in re.split(sep,ln):
            for _ in p:
                n = n+1
    return n

def lista_de_fichero(file:str,encoding:str,delim:str)->list[int]:
    lns:list[list[str]] = lineas_de_csv(file,encoding=encoding,delimiter=delim)
    r:list[int] = []
    for linea in lns:
        for p in linea:
            if len(p) > 0:
                r.append(int(p))  
    return r

def suma_elementos_fichero_if(file:str,encoding:str,pd:Callable[[int],bool])->int:
    lns:list[str] = lineas_de_fichero(file,encoding=encoding)
    r:int = 0
    for linea in lns:
        for p in re.split(',', linea):
            if len(p) > 0:
                e = int(p)
                if pd(e):
                    r = r + e 
    return r

def test1():
    print(encoding(absolute_path('resources/quijote.txt')))
    print(encoding(absolute_path('resources/lin_quijote.txt')))
    print(lista_de_fichero(absolute_path('datos/datos_2.txt'),encoding='utf-8',delim=","))
    
def test2():
    print(num_caracteres_no_delimitadores(absolute_path('resources/quijote.txt'),encoding='utf-16'))
    print(numero_de_palabras_distintas(absolute_path('resources/quijote.txt'),encoding='utf-16'))

if __name__ == '__main__':
    test2()
    
    
   
    
    
    



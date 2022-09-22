'''
Created on 16 sept 2022

@author: migueltoro
'''

from us.lsi.tools.File import lineas_de_fichero, absolute_path
import re
from typing import Callable

def lista_de_fichero(file:str,encoding:str)->list[int]:
    lns = lineas_de_fichero(file,encoding=encoding)
    r:list[int] = []
    for linea in lns:
        for p in re.split(',', linea):
            if len(p) > 0:
                r.append(int(p))  
    return r

def suma_elementos_fichero(file:str,encoding:str)->int:
    lns = lineas_de_fichero(file,encoding=encoding)
    r:int = 0
    for linea in lns:
        for p in re.split(',', linea):
            if len(p) > 0:
                r = r + int(p) 
    return r

def suma_elementos_fichero_if(file:str,encoding:str,pd:Callable[[int],bool])->int:
    lns = lineas_de_fichero(file,encoding=encoding)
    r:int = 0
    for linea in lns:
        for p in re.split(',', linea):
            if len(p) > 0:
                e = int(p)
                if pd(e):
                    r = r + e 
    return r

if __name__ == '__main__':
    
    ls: list[str] = lineas_de_fichero(absolute_path('/resources/datos_2.txt'),encoding='utf-8')
    print(ls)  
    print(lista_de_fichero(absolute_path('/resources/datos_2.txt'),encoding='utf-8'))
    print(suma_elementos_fichero(absolute_path('/resources/datos_2.txt'),encoding='utf-8'))
    print(suma_elementos_fichero_if(absolute_path('/resources/datos_2.txt'),encoding='utf-8',pd=lambda e: e%3==0))
    print(re.split(',', ",antonio,pepe"))
    
'''
Created on 16 sept 2022

@author: migueltoro
'''

from us.lsi.tools.File import lineas_de_fichero, absolute_path, encoding
import re

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

def lista_de_fichero(file:str,encoding:str)->list[int]:
    lns = lineas_de_fichero(file,encoding=encoding)
    r:list[int] = []
    for linea in lns:
        for p in re.split(',', linea):
            if len(p) > 0:
                r.append(int(p))  
    return r

if __name__ == '__main__':
    print(encoding(absolute_path('/resources/quijote.txt')))
    ls: list[str] = lineas_de_fichero(absolute_path('/resources/datos_2.txt'),encoding='utf-8')
    print(ls)  
    print(lista_de_fichero(absolute_path('/resources/datos_2.txt'),encoding='utf-8'))
    print(numero_de_palabras_distintas(absolute_path('/resources/quijote.txt'),encoding='utf-16'))
'''
Created on 16 sept 2022

@author: migueltoro
'''

from us.lsi.tools.File import lineas_de_fichero, absolute_path
import re

def numero_de_lineas(file: str) -> int:
    return len(lineas_de_fichero(file,encoding='utf-16'))

def numero_de_palabras_distintas(file: str) -> int:
    sep = r'[ ,;.\n():?!\"]'
    lns = lineas_de_fichero(file,encoding='utf-16')
    s = 0
    for linea in lns:
        for _ in re.split(sep, linea):
            s = s+1
    return s

if __name__ == '__main__':
    ls: list[str] = lineas_de_fichero(absolute_path('/resources/datos_2.txt'),encoding='utf-8')
    r:list[int] = []
    for linea in ls:
        for p in re.split(',', linea):
            if len(p) > 0:
                r.append(int(p))    
    print(r)
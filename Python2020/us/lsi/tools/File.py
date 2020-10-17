'''
Created on 15 jul. 2020

@author: migueltoro
'''

from typing import List, Iterator
import csv

def partes_de_linea(linea:str, delimiter:str=",")-> List[str]:
    partes = linea.split(delimiter)
    return partes

def lineas_iterator(file:str,encoding:str='utf-8') -> Iterator[str]:
    with open(file, "r", encoding=encoding) as f:
        for linea in f:
            yield linea
    
def lineas_de_fichero(file:str,encoding:str='utf-8') -> List[str]:
    with open(file, "r", encoding=encoding) as f:
        lineas_de_fichero =  [linea for linea in f]
        return lineas_de_fichero
    
def lineas_de_csv(file:str, delimiter:str=",")-> List[List[str]]:
    with open(file) as f:
        lector = csv.reader(f, delimiter = delimiter)
        lineas_de_fichero =  [linea for linea in lector]
        return lineas_de_fichero

def texto_de_fichero(file:str,encoding:str='utf-8') -> str:
    with open(file, "r", encoding=encoding) as f:
        texto = f.read()
        return texto
    
def write(file:str,texto:str) -> None:
    with open(file, "w", encoding='utf-8') as f:
        f.write(texto)

if __name__ == '__main__':
    f = lineas_iterator('../../../resources/palabras_huecas.txt')
    for x in f:
        print(x)
    
   
        
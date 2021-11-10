'''
Created on 15 jul. 2020

@author: migueltoro
'''


from typing import Iterable
import csv
import chardet

def partes_de_linea(linea:str, delimiter:str=",")-> list[str]:
    partes = linea.split(delimiter)
    return partes

def lineas_iterable(file:str,encoding:str='utf-8') -> Iterable[str]:
    with open(file, "r", encoding=encoding) as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield line.strip()
    
def lineas_de_fichero(file:str,encoding='utf-8') -> list[str]:
    with open(file,encoding=encoding) as f:
        lineas_de_fichero =  [linea.rstrip('\n') for linea in f]
        return lineas_de_fichero
    
def lineas_de_csv(file:str, delimiter:str=",", encoding='utf-8')-> list[list[str]]:
    with open(file,encoding= encoding) as f:
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

def write_iterable(file:str,iterable:Iterable[str]) -> None:
    with open(file, "w", encoding='utf-8') as f:
        for ln in iterable:
            f.write(ln)

def print_encoding(file:str)->str:
    with open(file,"rb") as f:
        data = f.read()
        enc = chardet.detect(data)
        return enc['encoding']

if __name__ == '__main__':
#    f = lineas_iterator('../../../resources/palabras_huecas.txt')
#    for x in f:
#        print(x)
    
    f = lineas_de_csv('../../../resources/estaciones.csv')
    for x in f:
        print(x)
   
        
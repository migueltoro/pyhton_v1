'''
Created on 15 jul. 2020

@author: migueltoro
'''


from typing import Iterable
import csv
import chardet
from us.lsi.tools.Preconditions import check_argument
import os
import sys

def root_project():
    return sys.path[1]

def absolute_path(file:str)->str:
    return root_project()+file

def dir_path()->str:
    return os.getcwd()

def existe_fichero(filePath:str)->bool:
    return os.path.isfile(filePath)
    
def partes_de_linea(linea:str, delimiter:str=",")-> list[str]:
    partes = linea.split(delimiter)
    return partes

def lineas_iterable(file:str,encoding:str='utf-8') -> Iterable[str]:
    check_argument(existe_fichero(file),'El fichero {} no existe'.format(file))
    with open(file, "r", encoding=encoding) as f:
        for line in f:
            yield line.strip()
    
def lineas_de_fichero(file:str,encoding:str='utf-8') -> list[str]:
    check_argument(existe_fichero(file),f'El fichero {file} no existe')
    with open(file,encoding=encoding) as f:
        lineas_de_fichero =  [linea.rstrip('\n') for linea in f]
        return lineas_de_fichero
       
def lineas_de_csv(file:str, delimiter:str=",", encoding:str='utf-8')-> Iterable[list[str]]:
    check_argument(existe_fichero(file),'El fichero {} no existe'.format(file))
    with open(file,encoding= encoding) as f:
        lector = csv.reader(f, delimiter = delimiter)
        lineas_de_fichero =  [linea for linea in lector]
        return lineas_de_fichero

def iterable_de_csv(file:str, delimiter:str=",", encoding:str='utf-8')-> Iterable[list[str]]:
    check_argument(existe_fichero(file),'El fichero {} no existe'.format(file))
    with open(file,encoding= encoding) as f:
        lector = csv.reader(f, delimiter = delimiter)
        for line in lector:
            yield line

def iterable_de_csv_partes(file:str, delimiter:str=",", encoding='utf-8')-> Iterable[str]:
    check_argument(existe_fichero(file),'El fichero {} no existe'.format(file))
    with open(file,encoding= encoding) as f:
        lector = csv.reader(f, delimiter = delimiter)
        for line in lector:
                for p in line:
                    yield p           

def read(file:str,encoding:str='utf-8') -> str:
    check_argument(existe_fichero(file),'El fichero {} no existe'.format(file))
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

def encoding(file:str)->str:
    check_argument(existe_fichero(file),'El fichero {} no existe'.format(file))
    with open(file,"rb") as f:
        data = f.read()
        enc = chardet.detect(data)
        return enc['encoding']

if __name__ == '__main__':
#    f = lineas_iterator('../../../resources/palabras_huecas.txt')
#    for x in f:
#        print(x)
    
    print(os.getcwd())
    print(existe_fichero("../../../resources/datos_2.txt"))
   
        
'''
Created on 15 jul. 2020

@author: migueltoro
'''


from typing import Iterable, Optional
import csv
import chardet
from us.lsi.tools.Preconditions import check_argument
import os
import sys

def root_project():
    return sys.path[1]

def absolute_path(file:str,project:str=root_project())->str:
    return project+file

def dir_path()->str:
    return os.getcwd()

def existe_fichero(filePath:str)->bool:
    return os.path.isfile(filePath)
    
def partes_de_linea(linea:str, delimiter:str=",")-> list[str]:
    partes = linea.split(delimiter)
    return partes

def iterable_de_fichero(file:str,encoding:str='utf-8') -> Iterable[str]:
    check_argument(existe_fichero(file),'El fichero {} no existe'.format(file))
    with open(file, "r", encoding=encoding) as f:
        for linea in f:
            yield linea.strip()
    
def lineas_de_fichero(file:str,encoding:str='utf-8') -> list[str]:
    check_argument(existe_fichero(file),f'El fichero {file} no existe')
    with open(file,"r",encoding=encoding) as f:
        return  [linea.strip() for linea in f]
       
def lineas_de_csv(file:str, delimiter:str=",", encoding:str='utf-8')-> list[list[str]]:
    check_argument(existe_fichero(file),f'El fichero {file} no existe')
    with open(file,"r",encoding= encoding) as f:
        lector = csv.reader(f, delimiter = delimiter)
        return  [linea for linea in lector]
    
def dict_de_csv(file:str, delimiter:str=",", encoding:str='utf-8')->dict[str,list[str]]:
    check_argument(existe_fichero(file),f'El fichero {file} no existe')
    with open(file,"r",encoding=encoding) as f:
        lector = csv.DictReader(f, delimiter = delimiter)
        r:dict[str,list[str]] = {}
        for row in lector:
            for k,v in row.items():
                r[k] = r.get(k, [])+[v]
        return r

def iterable_de_csv(file:str, delimiter:str=",", encoding:str='utf-8')-> Iterable[list[str]]:
    check_argument(existe_fichero(file),f'El fichero {file} no existe')
    with open(file,"r",encoding= encoding) as f:
        lector = csv.reader(f, delimiter = delimiter)
        for linea in lector:
            yield linea

def iterable_de_csv_partes(file:str, delimiter:str=",", encoding='utf-8')-> Iterable[str]:
    check_argument(existe_fichero(file),f'El fichero {file} no existe')
    with open(file,"r",encoding= encoding) as f:
        lector = csv.reader(f, delimiter = delimiter)
        for linea in lector:
            for p in linea:
                yield p      

def read(file:str,encoding:str='utf-8') -> str:
    check_argument(existe_fichero(file),'El fichero {} no existe'.format(file))
    with open(file,"r", encoding=encoding) as f:
        texto = f.read()
        return texto
    
def write(file:str,texto:str) -> None:
    with open(file,"w", encoding='utf-8') as f:
        f.write(texto)

def write_iterable(file:str,iterable:Iterable[str], encoding='utf-8') -> None:
    with open(file,"w", encoding=encoding) as f:
        for ln in iterable:
            f.write(ln+'\n')

def encoding(file:str)->Optional[str]:
    check_argument(existe_fichero(file),'El fichero {0} no existe'.format(file))
    with open(file,"rb") as f:
        data = f.read()
        enc = chardet.detect(data)
        return enc['encoding']

if __name__ == '__main__':
#    f = lineas_iterator('../../../resources/palabras_huecas.txt')
#    for x in f:
#        print(x)
    
    print(os.getcwd())
    print(existe_fichero(absolute_path("/datos/datos_2.txt")))
    print(root_project())
#    print(sys.path)
    print(dict_de_csv(absolute_path("/datos/pp2.csv")))   
    print(lineas_de_csv(absolute_path("/datos/pp2.csv")))   
    
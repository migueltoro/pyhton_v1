'''
Created on 15 jul. 2020

@author: migueltoro
'''

from typing import List
import csv

def text(file:str,encoding:str='utf-8') -> str:
    with open(file, "r", encoding=encoding) as f:
        text = f.read()
        f.close()
        return text
    
def lineas(file:str,encoding:str='utf-8') -> List[str]:
    with open(file, "r", encoding=encoding) as f:
        lineas =  [linea for linea in f]
        f.close()
        return lineas
    
def lineasCSV(file:str, delimiter:str=",")-> List[str]:
    with open(file) as f:
        lector = csv.reader(f, delimiter = delimiter)
        lineas =  [linea for linea in lector]
        f.close()
        return lineas

    
def write(file:str,text:str) -> None:
    with open(file, "w", encoding='utf-8') as f:
        f.write(text)
        f.close()

if __name__ == '__main__':
    pass
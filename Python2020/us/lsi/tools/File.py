'''
Created on 15 jul. 2020

@author: migueltoro
'''

import csv

def text(file,encoding='utf-8'):
    with open(file, "r", encoding=encoding) as f:
        text = f.read()
        f.close()
        return text
    
def lineas(file,encoding='utf-8'):
    with open(file, "r", encoding=encoding) as f:
        lineas =  [linea for linea in f]
        f.close()
        return lineas
    
def lineasCSV(file, delimiter = ","):
    with open(file) as f:
        lector = csv.reader(f, delimiter = delimiter)
        lineas =  [linea for linea in lector]
        f.close()
        return lineas

    
def write(file,text):
    with open(file, "w", encoding='utf-8') as f:
        f.write(text)
        f.close()

if __name__ == '__main__':
    pass
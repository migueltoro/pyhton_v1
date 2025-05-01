'''
Created on 24 nov 2021

@author: migueltoro
'''

from us.lsi.tools.Iterable import str_iter
from us.lsi.tools.File import lineas_de_fichero,absolute_path
import sys
import calendar
from sortedcontainers.sorteddict import SortedDict # type: ignore
import random

d = {0:'a',3:'b',2:'c'}
print(list(d.values()))
r2 = "La respuesta es correcta"

def pp(file:str)->float:
    ls: list[str] = lineas_de_fichero(file)
    ls2: list[str] = ls [1:]
    n:int = 0
    s:float = 0.
    for e in ls2:
        s = s + float(e.split(',')[1])
        n = n+1
    m = s/n
    return m

def pp2(file:str)->float:
    ls: list[str] = lineas_de_fichero(file)
    ls2: list[str] = ls [1:]
    n:int = 0
    s:float = 0.
    for e in ls2:
        _,v,_ = e.split(',')
        s = s + float(v)
        n = n+1
    m = s/n
    return m

numeros = [7, 3, 5, 1, 3, 1, 7]


if __name__ == '__main__':
    print(str_iter(sys.path,sep='\n'))
    print(list(calendar.day_name))
    print(d)
    r = sorted(d.items(),reverse=True)
    random.shuffle(r)
    print(r)    
    print(SortedDict(r))
    print(len(r2))
    print(r2[23])
    num = 29
    print(num % 3 == 0 or 20 <= num <= 30)
    print(4+1.)
    print(pp(absolute_path('datos/pp.txt')))
    print(pp2(absolute_path('datos/pp.txt')))
    print(numeros[8-2])
    print()
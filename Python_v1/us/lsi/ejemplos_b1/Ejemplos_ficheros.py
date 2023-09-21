'''
Created on 16 sept 2022

@author: migueltoro
'''

from us.lsi.tools.File import lineas_de_fichero, absolute_path, iterable_de_fichero
from typing import Callable, Iterable

def lista_de_fichero_0(file:str)->list[str]:
    with open(file,encoding='UTF-8') as f:
        r:list[str] = []
        for linea in f:
            r.append(linea)  
    return r

def lista_de_fichero_1(file:str)->list[str]:
    with open(file,encoding='UTF-8') as f:
        return list(f)

def lista_de_fichero_2(file:str)->list[int]:
    with open(file,encoding='UTF-8') as f:
        r:list[int] = []
        for linea in f:
            for p in linea.split(','):
                p = p.strip()
                if len(p) > 0:
                    r.append(int(p))  
    return r

def lista_de_fichero_3(file:str,encoding:str)->list[int]:
    lns:list[str] = lineas_de_fichero(file,encoding=encoding)
    r:list[int] = []
    for linea in lns:
        for p in linea.split(','):
            if len(p) > 0:
                r.append(int(p))  
    return r

def lista_de_fichero_4(file:str,encoding:str)->list[int]:
    lns:list[str] = lineas_de_fichero(file,encoding=encoding)
    r:list[int] = []
    for linea in lns:
        for p in linea.split(','):
            if len(p) > 0:
                r.append(int(p))  
    return r

def lista_de_fichero_5(file:str,encoding:str)->list[int]:
    lns:Iterable[str] = iterable_de_fichero(file,encoding=encoding)
    r:list[int] = []
    for linea in lns:
        for p in linea.split(','):
            if len(p) > 0:
                r.append(int(p))  
    return r

def lista_de_fichero_6(file:str,encoding:str,f:Callable[[int],int])->list[int]:
    lns:Iterable[str] = iterable_de_fichero(file,encoding=encoding)
    r:list[int] = []
    for linea in lns:
        for p in linea.split(','):
            if len(p) > 0:
                r.append(f(int(p)))
    return r

def suma_elementos_fichero(file:str,encoding:str)->int:
    lns = lineas_de_fichero(file,encoding=encoding)
    r:int = 0
    for linea in lns:
        for p in linea.split(','):
            if len(p) > 0:
                r = r + int(p) 
    return r

def suma_elementos_fichero_if(file:str,encoding:str,pd:Callable[[int],bool])->int:
    lns = lineas_de_fichero(file,encoding=encoding)
    r:int = 0
    for linea in lns:
        for p in linea.split(','):
            if len(p) > 0:
                e = int(p)
                if pd(e):
                    r = r + e 
    return r

def cuadrado(x:int)->int:
    return x*x

if __name__ == '__main__':
    print(",antonio,pepe".split(','))
    print(absolute_path('/resources/datos_2.txt'))
    f:Callable[[int],int] = lambda x: x*x
    print(f(3))
   
    print(lista_de_fichero_0(absolute_path('/datos/datos.txt')))
    print(lista_de_fichero_1(absolute_path('/datos/datos.txt')))
    ls: list[str] = lineas_de_fichero('../../../datos/datos.txt',encoding='utf-8')
    print(ls) 
#    print(lista_de_fichero_1(absolute_path('/datos/datos_2.txt'),encoding='utf-8'))
    print(lista_de_fichero_5(absolute_path('/datos/datos_2.txt'),encoding='utf-8'))
    print(lista_de_fichero_6(absolute_path('/datos/datos_2.txt'),encoding='utf-8',f=lambda x:int(x)**3))
    print(suma_elementos_fichero(absolute_path('/datos/datos_2.txt'),encoding='utf-8'))
    print(suma_elementos_fichero(absolute_path('/datos/datos_2.txt'),encoding='utf-8'))
    print(suma_elementos_fichero_if(absolute_path('/datos/datos_2.txt'),encoding='utf-8',pd=lambda e: e%3==0))    
    
    
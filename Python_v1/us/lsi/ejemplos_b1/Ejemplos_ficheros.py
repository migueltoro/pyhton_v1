'''
Created on 16 sept 2022

@author: migueltoro
'''


from us.lsi.tools.File import lineas_de_fichero, absolute_path, iterable_de_fichero, iterable_de_csv
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


def suma_elementos_fichero_if_2(file:str,encoding:str,pd:Callable[[int],bool])->int:
    lns:Iterable[list[str]] = iterable_de_csv(file,delimiter=',',encoding=encoding)
    r:int = 0
    for linea in lns:
        for p in linea:
            if len(p) > 0:
                e = int(p)
                if pd(e):
                    r = r + e 
    return r

def cuadrado(x:int)->int:
    return x*x

def lee_de_fichero(file:str,encoding:str)->str:
    with open(file,'r',encoding=encoding) as f:
        return f.read()

def escribe_en_fichero(file:str,encoding:str,ls:Iterable[str])->None:
    with open(file,'w',encoding=encoding) as f:
        r:str = '\n'.join(ls)
        f.write(r)
            
def escribe_en_fichero_csv(file:str,sep:str,encoding:str,ls:Iterable[list[str]])->None:
    with open(file,'w',encoding=encoding) as f:
        for linea in ls:
            r:str = sep.join(linea)
            f.write(r+'\n')

def test1():
    print(",antonio,pepe".split(','))
    print(absolute_path('resources/datos_2.txt'))
    f:Callable[[int],int] = lambda x: x*x
    print(f(4))
    print(cuadrado(4))
    
def test2():
    print(lista_de_fichero_0(absolute_path('datos/datos.txt')))
    print(lista_de_fichero_1(absolute_path('datos/datos.txt')))
    print(lista_de_fichero_2(absolute_path('datos/datos.txt')))
    ls1: list[str] = lineas_de_fichero(absolute_path('datos/datos.txt'),encoding='utf-8')
    print(ls1) 
    ls2: list[str] = lineas_de_fichero(absolute_path('datos/datos.txt'),encoding='utf-8')
    print(ls2) 
    
def test3():
    print('_____________')
    print(lista_de_fichero_5(absolute_path('datos/datos_2.txt'),encoding='utf-8'))
    print('_____________')
    print(lista_de_fichero_6(absolute_path('datos/datos_2.txt'),encoding='utf-8',f=lambda x:int(x)**3))
    
def test4():
    print(suma_elementos_fichero(absolute_path('datos/datos_2.txt'),encoding='utf-8'))
    print(suma_elementos_fichero_if(absolute_path('datos/datos_2.txt'),encoding='utf-8',pd=lambda e: e%3==0)) 
    print(suma_elementos_fichero_if_2(absolute_path('datos/datos_2.txt'),encoding='utf-8',pd=lambda e: e%3==0)) 


def test5():
    ''' Equivalencia entre for y while '''
   
    print('________________________')  
    s1:int=0
    for e in range(10,30,5):
        s1 = s1 + e
        print(s1)
    print('________________________')    
    s2:int=0
    i:int = 10
    while i < 30:
            s2 = s2 + i
            i = i + 5
            print(s2) 

def test6():
    print(lee_de_fichero(absolute_path('datos/datos.txt'),encoding='utf-8'))
    lns:Iterable[list[str]] = iterable_de_csv(absolute_path('datos/datos_2.txt'),delimiter=',',encoding='utf-8')
    escribe_en_fichero(absolute_path('datos/datos_4.txt'), 'utf-8', [str(x) for x in range(10,30,5)])
    escribe_en_fichero_csv(absolute_path('datos/datos_5.txt'), ';', 'utf-8', lns)
             
if __name__ == '__main__':
    test6()  
    
      
    
    
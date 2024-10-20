'''
Created on 18 sept 2022

@author: migueltoro
'''

from typing import Iterable
from us.lsi.tools.Iterable import distinct, flat_map, iterate
from us.lsi.tools.File import lineas_de_csv,absolute_path, iterable_de_fichero, encoding
from itertools import accumulate
from operator import mul
import re

def test0():
    print(encoding(absolute_path('/resources/lin_quijote.txt')))
    
'''
Comparación entre la forma clásica , explícita y por comprensión de definir colecciones

'''
    
def test1():
    # Forma clásica
    for x in range(3, 70):
        if x % 3 == 0:
            t = x**2
            print(t)
    # Forma por comprensión   
    r:Iterable[int] = (x**2 for x in range(3, 70) if x % 3 == 0)
    print('________________________________________')
    print(r)
    for e in r:
        print(e)
    
    # Forma por explícita
   
    r2: Iterable[int] = (3,56,78,67,45) # En realidad es una tupla que como sabemos es iterable
    print('________________________________________')
    print(r2)
    for e in r2:
        print(e)
        
    
    
def test2():
    # Forma clásica
    sr: list[int] = []
    for x in range(3, 70):
        if x % 3 == 0:
            t = x**2
            sr.append(t)

    # Forma por comprensión 
    s:list[int] = [x**2 for x in range(3, 70) if x % 3 == 0]
    print(s)
    print(sr)
    
    # Forma por explícita
    s2: list[int] = [3,56,78,67,45]
    print(s2)
        
def test3():
    # Forma clásica
    sts: set[int] = set()
    for x in range(3, 70):
        if x % 3 == 0:
            t = x**2
            sts.add(t)
    
    # Forma por comprensión     
    st:set[int] = {x**2 for x in range(3, 70) if x % 3 == 0}
    print(sts)
    print(st)
    # Forma por explícita
    st2: set[int] = {3,56,78,67,45}
    print(st2)
    
def test4():
    # Forma clásica
    dtr: dict[int,int] = {}
    for x in range(3, 70):
        if x % 3 == 0:
            t1 = x**2
            t2 = x**3
            dtr[t1] = t2

    # Forma por comprensión 
    dt:dict[int,int] = {x**2:x**3 for x in range(3, 70) if x % 3 == 0}
    print(dtr)
    print(dt)
    # Forma por explícita
    dt2: dict[int,int] = {3:56,78:67,45:45}
    print(dt2)
    
'''
Usos 
'''

    
def test5():
    nombres:list[str] = ["Miguel", "Ana", "Jose Maria", "Guillermo", "Maria", "Luisa"]
    ranking:dict[str,int] = {nombre: nombres.index(nombre) for nombre in nombres}
    print(f'ranking = {ranking}')
    
'''
Funciones para trasnformar iterables
'''    

def test6():  
    texto:str = "este es un pequeño texto para probar la siguiente definicion por comprension"
    iniciales = {p[0] for p in texto.split()}
    palabras = {p for p in texto.split()}
    palabras_por_iniciales = {c: [p for p in palabras if p[0]==c] for c in iniciales}
    print(f'palabras_por_iniciales = {palabras_por_iniciales}')
    
def test7():
    fichero:str= absolute_path("datos/datos_3.txt")
    it3:Iterable[list[str]] = lineas_de_csv(fichero)
    it4:Iterable[str] = flat_map(it3)
    it5:Iterable[int] = map(lambda e:int(e),it4)
    it6:Iterable[int] = distinct(it5)
    r0:list[int] = sorted(it6,key=lambda x:x)
    print(f'sorted = {r0}')
    
def test8():
    r7:Iterable[str] = flat_map(iterable_de_fichero(absolute_path("datos/datos_3.txt")),key=lambda ln: re.split(',',ln))
    print(list(r7))
    print('________________')
    r8:Iterable[str] = flat_map(lineas_de_csv(absolute_path('resources/lin_quijote.txt'), encoding='ISO-8859-1',delimiter=' '))
    r9:Iterable[str] = filter(lambda x: len(x)>0,r8)
    print(list(r9))
    
def test9():
    cadena:str = "lunes,martes,miercoles,jueves,viernes,sabado,domingo"
    it7:Iterable[tuple[int,str]] = enumerate(cadena)
    it8:Iterable[tuple[int,str]] = filter(lambda e:e[0]%2==0,it7)
    it9:Iterable[str] = map(lambda e: e[1],it8)
    print(list(it9))
    
def test10():
    a:int = 0
    b:int = 200
    c:int = 5
    d:int = 4
    it1:Iterable[int] = map(lambda x:x**2,range(a,b,c))
    it2:Iterable[int] = filter(lambda x:x%d==0, it1)
    print(list(it2))
    
def test11():
    versions:list[int] = [14, 3, 6]
    r5:Iterable[int] = accumulate(versions,mul)
    print(list(r5))
    
def test12():
    r6:Iterable[int] = iterate(3,lambda x:x*7,lambda x: x<1000)
    print(f'Iterate = {list(r6)}')
    
def test13():
    languages:list[str] = ['Java', 'Python', 'JavaScript']
    versions:list[int] = [14, 3, 6]   
    r1:Iterable[tuple[str,int]] = zip(languages, versions)
    print(list(r1))
    dias:list[str] = ["lunes", "martes", "miercoles", "jueves","viernes", "sabado", "domingo"]
    r2:Iterable[tuple[int,str]] = enumerate(dias)
    r3:list[tuple[int,str]] = list(r2)
    print(list(r3))
    r4:dict[int,str]  = dict(r3)
    print(r4)
    

if __name__ == '__main__':
    test1()
    
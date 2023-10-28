'''
Created on 18 sept 2022

@author: migueltoro
'''

from typing import Iterable
from us.lsi.tools.Iterable import distinct, flat_map, iterate
from us.lsi.tools.File import lineas_de_csv,absolute_path, iterable_de_fichero
from itertools import accumulate
from operator import mul
import re

for x in range(3, 70):
    if x % 3 == 0:
        t = x**2
        pass

r:Iterable[int] = (x**2 for x in range(3, 70) if x % 3 == 0)

sr: list[int] = []
for x in range(3, 70):
    if x % 3 == 0:
        t = x**2
        sr.append(t)

s:list[int] = [x**2 for x in range(3, 70) if x % 3 == 0]

sts: set[int] = set()
for x in range(3, 70):
    if x % 3 == 0:
        t = x**2
        sts.add(t)
        
st:set[int] = {x**2 for x in range(3, 70) if x % 3 == 0}


dtr: dict[int,int] = {}
for x in range(3, 70):
    if x % 3 == 0:
        t1 = x**2
        t2 = x**3
        dtr[t1] = t2

dt:dict[int,int] = {x**2:x**3 for x in range(3, 70) if x % 3 == 0}

nombres:list[str] = ["Miguel", "Ana", "Jose Maria", "Guillermo", "Maria", "Luisa"]
ranking:dict[str,int] = {nombre: nombres.index(nombre) for nombre in nombres}

texto:str = "este es un pequeño texto para probar la siguiente definicion por comprension"
iniciales = {p[0] for p in texto.split()}
palabras = {p for p in texto.split()}
palabras_por_iniciales = {c: [p for p in palabras if p[0]==c] for c in iniciales}

a:int = 0
b:int = 200
c:int = 5
d:int = 4
it1:Iterable[int] = map(lambda x:x**2,range(a,b,c))
it2:Iterable[int] = filter(lambda x:x%d==0, it1)

fichero:str= absolute_path("/datos/datos_3.txt")
it3:Iterable[list[str]] = lineas_de_csv(fichero)
it4:Iterable[str] = flat_map(it3,key=lambda x:x)
it5:Iterable[int] = map(lambda e:int(e),it4)
it6:Iterable[int] = distinct(it5)
r0:list[int] = sorted(it6,key=lambda x:x)


cadena:str = "lunes,martes,miercoles,jueves,viernes,sabado,domingo"
it7:Iterable[tuple[int,str]] = enumerate(cadena)
it8:Iterable[tuple[int,str]] = filter(lambda e:e[0]%2==0,it7)
it9:Iterable[str] = map(lambda e: e[1],it8)

r7:Iterable[str] = flat_map(iterable_de_fichero(absolute_path("/datos/datos_3.txt"),
                        encoding='ISO-8859-1'),key=lambda ln: re.split(',',ln))
r8:Iterable[str] = flat_map(
                lineas_de_csv(absolute_path('/resources/lin_quijote.txt'),encoding='ISO-8859-1',delimiter=' '))
r9:Iterable[str] = filter(lambda x: len(x)>0,r8)

texto2:str = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"

languages:list[str] = ['Java', 'Python', 'JavaScript']
versions:list[int] = [14, 3, 6]
dias:list[str] = ["lunes", "martes", "miercoles", "jueves","viernes", "sabado", "domingo"]
          
r1:Iterable[tuple[str,int]] = zip(languages, versions)
r2:enumerate[str] = enumerate(dias)
r3:list[tuple[int,str]] = list(r2)
r4:dict[int,str]  = dict(r3)
r5:Iterable[int] = accumulate(versions,mul)
r6:Iterable[int] = iterate(3,lambda x:x+7,lambda x: x<100)

if __name__ == '__main__':
    print(s)
    print(ranking)
    print(palabras_por_iniciales)
    print(r0)
    print(list(r9))
    print(list(r5))
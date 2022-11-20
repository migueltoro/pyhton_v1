'''
Created on 18 sept 2022

@author: migueltoro
'''

from typing import Iterable
from us.lsi.tools.File import absolute_path, iterable_de_fichero, lineas_de_csv
from us.lsi.tools.Iterable import flat_map, distinct, iterate, all_pairs
from itertools import accumulate
from operator import mul
import re



def ej1(a:int,b:int,c:int,d:int)->Iterable[int]:
    it1:Iterable[int] = map(lambda x:x**2,range(a,b,c))
    it2:Iterable[int] = filter(lambda x:x%d==0, it1)
    return it2

def ej2(fichero:str)->Iterable[int]:
    it1:Iterable[list[str]] = lineas_de_csv(fichero)
    it2:Iterable[str] = flat_map(it1,key=lambda x:x)
    it3:Iterable[int] = map(lambda e:int(e),it2)
    it4:Iterable[int] = distinct(it3)
    return it4

def ej3(cadena:str):
    it1:Iterable[tuple[int,str]] = enumerate(cadena)
    it2:Iterable[tuple[int,str]] = filter(lambda e:e[0]%2==0,it1)
    it3:Iterable[str] = map(lambda e: e[1],it2)
    return it3

languages:list[str] = ['Java', 'Python', 'JavaScript']
versions:list[int] = [14, 3, 6]
dias:list[str] = ["lunes", "martes", "miercoles", "jueves","viernes", "sabado", "domingo"]
          
r1:Iterable[tuple[str,int]] = zip(languages, versions)
r2:enumerate[str] = enumerate(dias)
r3:list[tuple[int,str]] = list(r2)
r4:dict[int,str]  = dict(r3)
r5:Iterable[int] = accumulate(versions,mul)
r6:Iterable[int] = iterate(3,lambda x:x+7,lambda x: x<100)


dias2:Iterable[str] = flat_map(dias)
r7:Iterable[str] = flat_map(iterable_de_fichero(absolute_path("/resources/datos_3.txt"),
                        encoding='ISO-8859-1'),key=lambda ln: re.split(',',ln))
r8:Iterable[str] = flat_map(
                lineas_de_csv(absolute_path('/resources/lin_quijote.txt'),encoding='ISO-8859-1',delimiter=' '))

texto:str = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"

r9:Iterable[str] = filter(lambda x: len(x)>0,r8)

if __name__ == '__main__': 
    print(list(ej1(2,45,3,4)))
    print(list(ej2(absolute_path("/resources/datos_3.txt"))))
    print(list(ej3("lunes,martes,miercoles,jueves,viernes,sabado,domingo")))
    print(list(all_pairs(3,3)))
    print(list(dias2))
    print(list(r1))
    print(list(r3))
    print(r4[5])
    print(list(r5))
    print(list(r6))
    print(list(r7))
    print(list(r9))
    
    

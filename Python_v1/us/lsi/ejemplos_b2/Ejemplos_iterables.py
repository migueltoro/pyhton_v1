'''
Created on 18 sept 2022

@author: migueltoro
'''

from typing import Iterable, Any
from us.lsi.tools.File import lineas_de_csv, absolute_path
from us.lsi.tools.Iterable import flat_map, distinct, index_if
from functools import reduce

def ej1(a:int,b:int,c:int,d:int)->Iterable[int]:
    it1:Iterable[int] = map(lambda x:x**2,range(a,b,c))
    it2:Iterable[int] = filter(lambda x:x%d==0, it1)
    return it2

def ej2(fichero:str)->Iterable[int]:
    it1:Iterable[list[str]] = lineas_de_csv(fichero)
    it2:Iterable[str] = flat_map(it1)
    it3:Iterable[int] = map(lambda e:int(e),it2)
    it4:Iterable[int] = distinct(it3)
    return it4

def ej3(cadena:str):
    it1:Iterable[tuple[int,str]] = enumerate(cadena)
    it2:Iterable[tuple[int,str]] = filter(lambda e:e[0]%2==0,it1)
    it3:Iterable[str] = map(lambda e: e[1],it2)
    return it3

def hacia_atras(ls:list[Any])-> Iterable[Any]:
    i = len(ls)-1
    while i>=0:
        yield ls[i]
        i = i-1


dias:list[str] = ["lunes", "martes", "miercoles", "jueves","viernes", "sabado", "domingo"]
texto:str = "En un lugar de la Mancha de cuyo nombre no quiero \ acordarme"

if __name__ == '__main__':
    print(sorted(dias, key=len))
    print(reduce(lambda x,y: x*y,range(2,30,5)))
    print(list(hacia_atras(dias)))
    print(list(ej3("lunes,martes,miercoles,jueves,viernes,sabado,domingo")))
    print(list(ej1(2,45,3,4)))
    print(list(ej2(absolute_path("/resources/datos_3.txt"))))
    print("Primera aparicion de la letra a:",index_if(texto,lambda e:e=="a"))

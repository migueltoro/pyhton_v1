'''
Created on 17 nov 2021

@author: migueltoro
'''
from us.lsi.tools.File import lineas_de_fichero, lineas_de_csv, encoding
from us.lsi.tools.Iterable import flat_map
from typing import Iterable, TypeVar, Callable
from us.lsi.tools.Preconditions import checkArgument
import re
import random
from collections import Counter
from us.lsi.tools.File import absolute_path
from calendar import day_name

E = TypeVar('E')
R = TypeVar('R')

def acumula(fichero:str,delimiter:str=',',encoding:str='utf-8',inicial:R='',f:Callable[[R,E],R]=lambda r,e:r+e)->R:
    lineas = lineas_de_csv(fichero,delimiter=delimiter,encoding=encoding)
    r:R = inicial
    for ln in lineas:
        if len(ln) > 0:
            for e in ln:
                r = f(r,e)
    return r

def mcd(a:int, b:int)->int:
    checkArgument(a>=0 and b>0,'El coeficiente a debe ser \
         mayor o igual que cero y b mayor que cero \
        y son: a = {0}, b = {1}'.format(a,b))
    while b > 0:
        a, b = b, a%b
    return a

def suma_aritmetica(a:int,b:int,c:int)->int:
    s = 0
    for e in range(a,b,c):
        s = s + e
    return s

if __name__ == '__main__':
    r = acumula(absolute_path("/resources/datos_2.txt"),encoding='ISO-8859-1',inicial=set(),f=lambda r,e:r|{int(e)})
    print(r)
    print('../../../resources/datos_2.txt'.split('/'))
    print(re.split('[ ,]','En un lugar de la Mancha, de cuyo nombre no quiero acordarme'))
    print(mcd(135,45))
    print(range(23,45))
    print("La suma de la pregresion aritmetica de {0} a {1} \
con razon {2} es {3}" \
    .format(2,500,7,suma_aritmetica(2,500,7)))
    r = [random.randint(0,100) for _ in range(50)]
    print(sorted(Counter(r).items(),reverse = True))
    it = lineas_de_csv("../../../resources/datos_2.txt",encoding='ISO-8859-1')
    print(Counter(flat_map(it)).most_common(5))
    

    
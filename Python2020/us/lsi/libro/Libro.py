'''
Created on 25 jul. 2020

@author: migueltoro
'''

from typing import Set,OrderedDict,Iterator
from us.lsi.tools.File import lineas
from us.lsi.tools.Functions import identity
from us.lsi.tools.Iterable import size,flat_map,average,find_first,grouping,distinct,str_iterable,grouping_list
from us.lsi.tools.Collections import invert_dict
import re

sep = r'[ ,;.\n():?!\"]'

def palabras_huecas() -> Set[str]:
    lns = lineas("../../../resources/palabras_huecas.txt")
    return {p for p in lns}

def palabras_no_huecas(file: str) -> Iterator[str]:
    lns = lineas(file,encoding='utf-16')
    pls = flat_map(lns,lambda x: re.split(sep, x))
    palabras = (p for p in pls if p not in palabras_huecas() if len(p) > 0)
    return palabras

def palabras_no_huecas_distintas(file: str) -> Iterator[str]:
    return distinct(palabras_no_huecas(file))

def numero_de_lineas(file: str) -> int:
    return len(lineas(file))

def numero_de_palabras_no_huecas(file:str) -> int:
    return size(palabras_no_huecas(file)) 

def numero_de_palabras_distintas_no_huecas(file:str) -> int:    
    return size(palabras_no_huecas_distintas(file))            

def longitud_media_de_lineas(file:str) -> float:
    return average(len(ln) for ln in lineas(file))

def numero_de_lineas_vacias(file:str) -> int:
    return size(ln for ln in lineas(file) if len(ln) == 0)

def linea_mas_larga(file:str) -> str:
    return max(lineas(file), key= lambda x:len(x))

def primera_linea_con_palabra(file:str,palabra:str) -> str:
    return find_first(lineas(file),predicate=lambda ln:palabra in ln).get()

def linea_numero(file:str,n:int) -> str:
    return find_first(enumerate(lineas(file)),predicate=lambda p:p[0] == n).get()[1]

def frecuencias_de_palabras(file:str) -> OrderedDict[str,int]:
    d = grouping(palabras_no_huecas(file),fkey=identity,op=lambda x,y:x+1,a0=0)
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))

def palabras_por_frecuencias(file:str) -> OrderedDict[int,Set[str]]:
    d = invert_dict(frecuencias_de_palabras(file))
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))
 
def palabra_en_lineas(file:str) -> OrderedDict[str,Set[int]]:
    lns = lineas(file,encoding='utf-16')
    palabras = ((i,p) for i,linea in enumerate(lns) for p in re.split(sep,linea) if len(p) >0) 
    d = grouping_list(palabras,fkey=lambda e: e[1], fvalue=lambda e: e[0])
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))

if __name__ == '__main__':
#    print(numero_de_palabras_distintas_no_huecas("../../../resources/quijote.txt"))
#    print(str_iterable(palabras_por_frecuencias("../../../resources/quijote.txt").items(),sep='\n',pf='',sf=''))
    print(str_iterable(palabra_en_lineas("../../../resources/quijote.txt").items(),sep='\n',pf='',sf=''))
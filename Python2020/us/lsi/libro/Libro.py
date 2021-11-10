'''
Created on 25 jul. 2020

@author: migueltoro
'''

from typing import OrderedDict,Iterable
from us.lsi.tools.File import lineas_de_fichero
from us.lsi.tools.Functions import identity
from us.lsi.tools.Iterable import flat_map,average,find_first,distinct,str_iterable,grouping_list,\
    frequencies
from us.lsi.tools.Collections import invert_dict
import re

sep = r'[ ,;.\n():?!\"]'

def palabras_huecas() -> set[str]:
    lns = lineas_de_fichero("../../../resources/palabras_huecas.txt")
    return {p for p in lns}

def palabras_no_huecas(file: str) -> Iterable[str]:
    lns = lineas_de_fichero(file,encoding='utf-16')
    pls = flat_map(lns,lambda x: re.split(sep, x))
    palabras = (p for p in pls if p not in palabras_huecas() if len(p) > 0)
    return palabras

def palabras_no_huecas_distintas(file: str) -> Iterable[str]:
    return distinct(palabras_no_huecas(file))

def numero_de_lineas(file: str) -> int:
    return len(lineas_de_fichero(file))

def numero_de_palabras_no_huecas(file:str) -> int:
    return palabras_no_huecas(file).count() 

def numero_de_palabras_distintas_no_huecas(file:str) -> int:    
    return palabras_no_huecas_distintas(file).count()            

def longitud_media_de_lineas(file:str) -> float:
    return average(len(ln) for ln in lineas_de_fichero(file))

def numero_de_lineas_vacias(file:str) -> int:
    return (ln for ln in lineas_de_fichero(file) if len(ln) == 0).count()

def linea_mas_larga(file:str) -> str:
    return max(lineas_de_fichero(file), key= lambda x:len(x))

def primera_linea_con_palabra(file:str,palabra:str) -> str:
    return find_first(lineas_de_fichero(file),predicate=lambda ln:palabra in ln).get()

def linea_numero(file:str,n:int) -> str:
    return find_first(enumerate(lineas_de_fichero(file)),predicate=lambda p:p[0] == n).get()[1]

def frecuencias_de_palabras(file:str) -> OrderedDict[str,int]:
    d = frequencies(palabras_no_huecas(file),fkey=identity)
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))

def palabras_por_frecuencias(file:str) -> OrderedDict[int,set[str]]:
    d = invert_dict(frecuencias_de_palabras(file))
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))
 
def palabra_en_lineas(file:str) -> OrderedDict[str,set[int]]:
    lns = lineas_de_fichero(file,encoding='utf-16')
    palabras = ((i,p) for i,linea in enumerate(lns) for p in re.split(sep,linea) if len(p) >0) 
    d = grouping_list(palabras,fkey=lambda e: e[1], fvalue=lambda e: e[0])
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))
    

if __name__ == '__main__':
#    print(numero_de_palabras_distintas_no_huecas("../../../resources/quijote.txt"))
#    print(str_iterable(palabras_por_frecuencias("../../../resources/quijote.txt").items(),sep='\n',pf='',sf=''))
    print(str_iterable(palabra_en_lineas("../../../resources/quijote.txt").items(),sep='\n',prefix='',suffix=''))
'''
Created on 25 jul. 2020

@author: migueltoro
'''

from typing import OrderedDict,Iterable
from us.lsi.tools.File import lineas_de_fichero, encoding
from us.lsi.tools.Dict import str_dictionary, invert_dict_set
from us.lsi.tools.Functions import identity
from us.lsi.tools.Iterable import flat_map,average,first,distinct,str_iterable,grouping_set,groups_size, count
from collections import Counter
import re
from us.lsi.tools.Dict import str_dictionary

sep = r'[ ,;.\n():?!\"]'

def palabras_huecas() -> set[str]:
    lns = lineas_de_fichero("../../../resources/palabras_huecas.txt")
    return {p for p in lns}

def palabras_no_huecas(file: str) -> Iterable[str]:
    huecas = palabras_huecas()
    lns = lineas_de_fichero(file,encoding='utf-16')
    pls = flat_map(lns,lambda x: re.split(sep, x))
    palabras = (p for p in pls if p not in huecas if len(p) > 0)
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
    return count(ln for ln in lineas_de_fichero(file,encoding='utf-16') if len(ln) == 0)

def linea_mas_larga(file:str) -> str:
    return max(lineas_de_fichero(file), key= lambda x:len(x))

def primera_linea_con_palabra(file:str,palabra:str) -> str:
    return first(lineas_de_fichero(file),predicate=lambda ln:palabra in ln).get()

def linea_numero(file:str,n:int) -> str:
    return first(enumerate(lineas_de_fichero(file)),predicate=lambda p:p[0] == n).get()[1]

def frecuencias_de_palabras(file:str) -> OrderedDict[str,int]:
    d = groups_size(palabras_no_huecas(file))
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))

def palabras_por_frecuencias(file:str) -> OrderedDict[int,set[str]]:
    d = invert_dict_set(frecuencias_de_palabras(file))
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))
 
def palabra_en_lineas(file:str) -> OrderedDict[str,set[int]]:
    lns = lineas_de_fichero(file,encoding='utf-16')
    palabras = ((i,p) for i,linea in enumerate(lns) for p in re.split(sep,linea) if len(p) >0) 
    d = grouping_set(palabras,fkey=lambda e: e[1], fvalue=lambda e: e[0])
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))

def palabras_frecuentes(file:str, k:int)->str:
    return Counter(palabras_no_huecas(file)).most_common(k)
      

if __name__ == '__main__':
    print(encoding("../../../resources/quijote.txt"))
#    print(str_iterable(palabras_no_huecas("../../../resources/quijote.txt"),sep='\n'))
#    print(str_dictionary(palabras_por_frecuencias("../../../resources/quijote.txt"),sep='\n'))
#    print(numero_de_palabras_distintas_no_huecas("../../../resources/quijote.txt"))
#    print(str_iterable(palabras_por_frecuencias("../../../resources/quijote.txt").items(),sep='\n',pf='',sf=''))
    print(str_iterable(palabra_en_lineas("../../../resources/quijote.txt").items(),sep='\n',prefix='',suffix=''))
#    print(palabras_frecuentes("../../../resources/quijote.txt"))
    print(palabras_frecuentes("../../../resources/quijote.txt", 10))
    
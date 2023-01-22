'''
Created on 25 jul. 2020

@author: migueltoro
'''

from typing import OrderedDict,Iterable,Optional
from us.lsi.tools.File import lineas_de_fichero, encoding, absolute_path, iterable_de_fichero
from us.lsi.tools.Dict import strfdict, invert_dict_set
from us.lsi.tools.Iterable import flat_map,first,distinct,strfiter,grouping_set,groups_size,count_if
from collections import Counter
import re
from statistics import mean

sep = r'[ ,;.\n():?!\"]'

def palabras_huecas() -> set[str]:
    lns:list[str] = lineas_de_fichero(absolute_path("/resources/palabras_huecas.txt"))
    return {p for p in lns}

def lineas_de_libro(file: str) -> Iterable[str]:
    return iterable_de_fichero(file,encoding='utf-16')

def palabras_no_huecas(file: str) -> Iterable[str]:
    huecas:set[str] = palabras_huecas()
    lns:Iterable[str] = lineas_de_libro(file)
    pls:Iterable[str] = flat_map(lns,lambda x: re.split(sep, x))
    palabras:Iterable[str] = (p for p in pls if p not in huecas and len(p) > 0)
    return palabras

def palabras_no_huecas_distintas(file: str) -> Iterable[str]:
    return distinct(palabras_no_huecas(file))

def palabras_lineas(file:str) -> Iterable[tuple[int,str]]:
    lns:Iterable[str] = lineas_de_libro(file)
    pl:Iterable[tuple[int,str]] = ((i,p) for i,linea in enumerate(lns) for p in re.split(sep,linea) if len(p) > 0) 
    return pl

def numero_de_lineas(file: str) -> int:
    return count_if(lineas_de_libro(file))

def numero_de_palabras_no_huecas(file:str) -> int:
    return count_if(palabras_no_huecas(file)) 

def numero_de_palabras_distintas_no_huecas(file:str) -> int:    
    return count_if(palabras_no_huecas_distintas(file))           

def longitud_media_de_lineas(file:str) -> float:
    return mean(len(ln) for ln in lineas_de_fichero(file))

def numero_de_lineas_vacias(file:str) -> int:
    return count_if(ln for ln in lineas_de_libro(file) if len(ln) == 0)

def linea_mas_larga(file:str) -> str:
    return max(lineas_de_libro(file), key= lambda x:len(x))

def primera_linea_con_palabra(file:str,palabra:str) -> Optional[str]:
    return first(lineas_de_libro(file),p=lambda ln:palabra in ln)

def linea_numero(file:str,n:int) -> Optional[str]:
    r:Optional[tuple[int,str]] = first(enumerate(lineas_de_libro(file)),p=lambda p:p[0] == n)
    return r[1] if r else None

def frecuencias_de_palabras(file:str) -> OrderedDict[str,int]:
    d: dict[str,int] = groups_size(palabras_no_huecas(file))
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))

def palabras_por_frecuencias(file:str) -> OrderedDict[int,set[str]]:
    d:dict[int,set[str]] = invert_dict_set(dict(frecuencias_de_palabras(file)))
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))
 
def palabra_en_lineas(file:str) -> OrderedDict[str,set[int]]:
    palabras:Iterable[tuple[int,str]] = palabras_lineas(file)
    d:dict[str,set[int]] = grouping_set(palabras,key=lambda e: e[1], value=lambda e: e[0])
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))

def palabras_frecuentes(file:str, k:int)->list[str]:
    return [p for p,_ in Counter(palabras_no_huecas(file)).most_common(k)]

    
if __name__ == '__main__':
    print(encoding(absolute_path("/resources/quijote.txt")))
    print(strfiter(palabras_no_huecas(absolute_path("/resources/quijote.txt")),sep='\n'))
    print(strfdict(palabras_por_frecuencias(absolute_path("/resources/quijote.txt")),sep='\n'))
    print(numero_de_palabras_distintas_no_huecas(absolute_path("/resources/quijote.txt")))
    print(strfiter(palabras_por_frecuencias(absolute_path("/resources/quijote.txt")).items(),sep='\n',prefix='',suffix=''))
    print(strfiter(palabra_en_lineas(absolute_path("/resources/quijote.txt")).items(),sep='\n',prefix='',suffix=''))
    print(palabras_frecuentes(absolute_path("/resources/quijote.txt"), 10))
    
'''
Created on 7 dic 2022

@author: migueltoro
'''


from collections import Counter
import re
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from typing import OrderedDict,Optional

sep = r'[ ,;.\n():?!\"]'

def palabras_huecas() -> set[str]:
    lns:list[str] = lineas_de_fichero(absolute_path("/resources/palabras_huecas.txt"))
    r:set[str] = set()
    for p in lns:
        r.add(p) 
    return r

def numero_de_lineas(file: str) -> int:
    lns:list[str] = lineas_de_fichero(file)
    r:int = 0
    for _ in lns:
        r = r +1
    return r

def numero_de_lineas_vacias(file:str) -> int:
    lns:list[str] = lineas_de_fichero(file)
    r:int = 0
    for ln in lns:
        if len(ln)==0:
            r = r +1
    return r

def longitud_media_de_lineas(file:str) -> float:
    lns:list[str] = lineas_de_fichero(file)
    n:int = 0
    s:int = 0
    for ln in lns:
        n = n+1
        s = s + len(ln)
    return s/n

def linea_mas_larga(file:str) -> str:
    lns:list[str] = lineas_de_fichero(file)
    n:int = len(lns[0])
    ml:str = lns[0]
    for ln in lns[1:]:
        if len(ln) > n:
            n = len(ln)
            ml = ln
    return ml

def linea_numero(file:str,n:int) -> Optional[str]:
    lns:list[str] = lineas_de_fichero(file)
    if n>=0 and n <len(lns):
        return lns[n]
    else:
        return None
    

def numero_de_palabras_no_huecas(file:str) -> int:
    ph:set[str] = palabras_huecas()
    lns:list[str] = lineas_de_fichero(file)
    r: int = 0
    for ln in lns:
        for p in re.split(sep,ln):
            if not p in ph:
                r = r + 1
    return r

def numero_de_palabras_distintas_no_huecas(file:str) -> int: 
    ph:set[str] = palabras_huecas()
    lns:list[str] = lineas_de_fichero(file)
    pa:set[str] = set()
    r: int = 0
    for ln in lns:
        for p in re.split(sep,ln):
            if not p in ph:
                if not p in pa:
                    r = r + 1
                    pa.add(p)
    return r   

def primera_linea_con_palabra(file:str,palabra:str) -> Optional[str]:
    lns:list[str] = lineas_de_fichero(file)
    r: Optional[str] = None
    for ln in lns:
            if palabra in ln:
                r = ln
                break
    return r  

def frecuencias_de_palabras(file:str) -> OrderedDict[str,int]:
    ph:set[str] = palabras_huecas()
    lns:list[str] = lineas_de_fichero(file)
    d:dict[str,int]
    for ln in lns:
        for p in re.split(sep,ln):
            if not p in ph:
                if p in d.keys():
                    d[p] = d[p]+1
                else:
                    d[p] = 1          
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))

def palabras_por_frecuencias(file:str) -> OrderedDict[int,set[str]]:
    d: dict[str,int] = frecuencias_de_palabras(file)
    r: dict[int,set[str]] = {}
    for p in d.keys():
        key = d[p]
        if key in r:
            r[key].add(p)
        else:
            r[key] = {p}
    return OrderedDict(sorted(r.items(), key=lambda t: t[0]))  

def palabra_en_lineas(file:str) -> OrderedDict[str,set[int]]: 
    ph:set[str] = palabras_huecas()
    lns:list[str] = lineas_de_fichero(file)
    nl: int = 0
    d: dict[str,set[int]] = {}
    for ln in lns:
        for p in re.split(sep,ln):
            if not p in ph:
                if p in d.keys():
                    d[p].add(nl)
                else:
                    d[p] = {nl}              
        nl = nl + 1            
    return OrderedDict(sorted(d.items(), key=lambda t: t[0]))

def palabras_frecuentes(file:str, k:int)->list[str]:
    return [p for p,_ in Counter(frecuencias_de_palabras(file)).most_common(k)]


if __name__ == '__main__':
    pass
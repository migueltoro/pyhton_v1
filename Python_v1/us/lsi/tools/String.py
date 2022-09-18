'''
Created on 24 jul. 2020

@author: migueltoro
'''

import re
from typing import TypeVar, Callable

E = TypeVar('E')
K = TypeVar('K')

def transform(inText:str,reglas:dict[str,str]) -> str:
    outText = inText;
    for e,s in reglas.items():
        outText = re.sub(r'\{'+e+'\}',s,outText)
    return outText

def to_unicode(r:str) -> str:
    return str(r).encode('cp850', errors='replace').decode('cp850')

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)   

def str_split(text:str,sep:str=',') -> list[str]:
    return re.split(sep,text)

def strplist(text:str,value:Callable[[str],E])->list[E]:
    txt:list[str] = re.split('[,\[\]]',text)
    return [value(e) for e in txt if e]

def strpset(text:str,value:Callable[[str],E])->set[E]:
    txt:list[str] = re.split('[,\{\}]',text)
    return {value(e) for e in txt if e}

def strpdict(text:str,key:Callable[[str],K],value:Callable[[str],E])->dict[K,E]:
    txt:list[str] = re.split('[,\{\}]',text)
    txt2:list[list[str]] = [re.split(':',e) for e in txt if e]
    return {key(k):value(v) for k,v in txt2}

if __name__ == '__main__':
    e0 = r'[ ,;.\n():?!\"]'.encode('utf-8')
    print(e0)
    e1 = 'Juan Antonio,Pepe fue&mail'
    print(str_split(e1,sep='[ ,&]'))
    print(e1.split(' ,&'))
    print(strplist('[3.4,5.6,7.8]',float))
    print(strpset('{3.4,5.6,7.8,5.6}',float))
    print(strpdict('{2:3.4,4:5.6,6:7.8,10:5.6}',int,float))
'''
Created on 24 jul. 2020

@author: migueltoro
'''

import re
from typing import TypeVar


Objeto2D = TypeVar('Objeto2D')

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

if __name__ == '__main__':
    e0 = r'[ ,;.\n():?!\"]'.encode('utf-8')
    print(e0)
    e1 = 'Juan Antonio,Pepe fue&mail'
    print(str_split(e1,sep='[ ,&]'))
    print(e1.split(' ,&'))
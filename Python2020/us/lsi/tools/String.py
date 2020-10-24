'''
Created on 24 jul. 2020

@author: migueltoro
'''

import re
from typing import TypeVar, Dict, List


Objeto2D = TypeVar('Objeto2D')

def transform(inText:str,reglas:Dict[str,str]) -> str:
    outText = inText;
    for e,s in reglas.items():
        outText = re.sub(r'\{'+e+'\}',s,outText)
    return outText;

def to_unicode(r:str) -> str:
    return str(r).encode('cp850', errors='replace').decode('cp850')

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)   

def split_str(text:str,sep:str=',') -> List[str]:
    return re.split(sep,text)

if __name__ == '__main__':
    e = r'[ ,;.\n():?!\"]'.encode('utf-8')
    print(e)
    e = 'Juan Antonio,Pepe fue&mail'
    print(split_str(e,sep='[ ,&]'))
    print(e.split(' ,&'))
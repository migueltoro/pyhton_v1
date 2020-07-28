'''
Created on 26 jul. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from typing import TypeVar, Tuple

UsuarioPalabra = TypeVar('UsuarioPalabra')

@dataclass(frozen=True,order=True,)
class UsuarioPalabra:
    usuario:str
    palabra:str
    
    @staticmethod   
    def of(usuario: str, palabra:str) -> UsuarioPalabra:
        return UsuarioPalabra(usuario,palabra)
    
    @staticmethod   
    def of_tuple(t: Tuple[str,str]) -> UsuarioPalabra:
        return UsuarioPalabra(t[0],t[1])
    
    def __str__(self):
        return "(%s,%s)" % (self.usuario,self.palabra)

if __name__ == '__main__':
    pass
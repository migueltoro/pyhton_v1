'''
Created on 23 ago 2024

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar
from us.lsi.tipos_agregados.Agregado_lineal import Agregado_lineal

E = TypeVar('E')


class Cola(Agregado_lineal[E]):
    
    @staticmethod
    def of()->Cola[E]:
        return Cola()
    
    def __init__(self)->None:
        super().__init__()
    
    def add(self,e:E)->None:
        self._elements.append(e)
        

if __name__ == '__main__':
    cl:Cola[int] = Cola.of()
    cl.add_all([23, 47, 1,2,-3,4,5])
    print(cl.remove_all())
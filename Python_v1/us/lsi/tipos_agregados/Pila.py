'''
Created on 23 ago 2024

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar
from us.lsi.tipos_agregados.Agregado_lineal import Agregado_lineal

E = TypeVar('E')


class Pila(Agregado_lineal[E]):
    
    @staticmethod
    def of()->Pila[E]:
        return Pila()
    
    def __init__(self)->None:
        super().__init__()
    
    def add(self,e:E)->None:
        self._elements.insert(0,e)
        

if __name__ == '__main__':
    cl:Pila = Pila.of()
    cl.add_all([23, 47, 1,2,-3,4,5])
    print(cl.remove_all())
   

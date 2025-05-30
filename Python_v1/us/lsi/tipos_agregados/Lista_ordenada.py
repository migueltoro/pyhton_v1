'''
Created on 27 ago 2024

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Callable, Generic
from us.lsi.tipos_agregados.Agregado_lineal import Agregado_lineal
from us.lsi.tools.Types import Comparable


E = TypeVar('E')
R = TypeVar('R', bound=Comparable)


class Lista_ordenada(Agregado_lineal[E],Generic[E,R]):
    
    @staticmethod
    def of(order:Callable[[E],R])->Lista_ordenada[E,R]:
        return Lista_ordenada(order)
    
    def __init__(self,order:Callable[[E],R])->None:
        super().__init__() 
        self.__order = order
       
    def __index_order(self,e:E)->int:
        '''
        Obtiene el índice del elemento que es menor o igual que e y tal que el siguiente elemento es mayor que e
        '''
        ln:int = len(self._elements)
        order_e:R = self.__order(e)
        
        if self.is_empty() or order_e < self.__order(self._elements[0]):
            return 0
        if self.__order(self._elements[ln-1]) <= order_e:
            return ln        
        for i in range(ln):
            if self.__order(self._elements[i]) <= order_e and self.__order(self._elements[i + 1]) > order_e:
                return i+1
        return -1
    
    def add(self,e:E)->None:
        i:int = self.__index_order(e)
        self._elements.insert(i,e)
     

if __name__ == '__main__':
    cl:Lista_ordenada[int,int] = Lista_ordenada.of(lambda x:-x)
    cl.add_all([23, 47, 1,2,-3,4,5])
    print(cl.remove_all())

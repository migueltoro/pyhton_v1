'''
Created on 10 sept 2024

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Generic
from us.lsi.tools.Types import Comparable
from abc import abstractmethod
from enum import Enum

E = TypeVar('E')
P = TypeVar('P', bound=Comparable)

class Implementacion(Enum):
    LISTA = 1
    MONTON = 2

class Cola_de_prioridad(Generic[E,P]):
    
    @staticmethod
    def of(imp:Implementacion=Implementacion.MONTON)->Cola_de_prioridad[E,P]:
        if imp == Implementacion.LISTA:
            return Cola_de_prioridad_lista_ordenada()
        else:
            return Cola_de_prioridad_monton()
    
    def __init__(self)->None:
        self._elements:list[E] = []
        
    def add_all(self,ls:list[tuple[E,P]])->None:
        for e in ls:
            self.add(e[0],e[1])
    
    def remove_all(self)->list[E]:
        ls:list[E] = []
        while not self.is_empty():
            ls.append(self.remove())
        return ls
    
    def size(self)->int:
        return len(self._elements)
    
    def is_empty(self)->bool:
        return len(self._elements) == 0
    
    def elements(self)->list[E]:
        return self._elements
    
    @abstractmethod
    def add(self,e:E,priority:P)->None:
        pass
    
    @abstractmethod   
    def decrease_priority(self,e:E,new_priority:P)->None:
        pass
    
    @abstractmethod
    def remove(self)->E:
        pass
    

class Cola_de_prioridad_lista_ordenada(Cola_de_prioridad[E,P]):
    
    def __init__(self)->None:
        super().__init__()
        self._priorities:list[P] = []
       
    def _index_order(self,priority:P)->int:
        '''
        Obtiene el índice del elemento que es menor o igual que e y tal que el siguiente elemento es mayor que e
        '''
        ln:int = len(self._elements)
        
        if self.is_empty() or priority < self._priorities[0]:
            return 0
        if self._priorities[ln-1] <= priority:
            return ln        
        for i in range(ln):
            if self._priorities[i] <= priority and self._priorities[i + 1] > priority:
                return i+1
        return -1
    
    def add(self,e:E,priority:P)->None:
        i:int = self._index_order(priority)
        self._elements.insert(i,e)
        self._priorities.insert(i,priority)
        
    def remove(self)->E:  
        assert len(self._elements) > 0, 'El agregado esta vacío'
        e:E = self._elements.pop(0)
        self._priorities.pop(0)
        return e 
         
    def decrease_priority(self,e:E,new_priority:P)->None:
        index:int = self._elements.index(e)
        if new_priority < self._priorities[index] :
            self.elements().pop(index)
            self._priorities.pop(index)
            self.add(e,new_priority)

       
class Datos(Generic[P]):
    
    def __init__(self,priority:P,index:int)->None:
        self.priority:P  = priority                    
        self.index:int = index
    
    @staticmethod
    def of(priority:P,index:int)->Datos[P]:
        return Datos(priority,index)
    
class Cola_de_prioridad_monton(Cola_de_prioridad[E,P]):
    
    def __init__(self)->None:
        super().__init__()
        self._map:dict[E,Datos[P]] = {} 
        
    def __swap(self,i:int,j:int):      
        self._elements[i],self._elements[j] = self._elements[j],self._elements[i]
        self._map[self._elements[i]].index = i
        self._map[self._elements[j]].index = j
                
    def __last(self)->int:
        return len(self._elements)-1 
    
    def __parent(self,i:int)->int:
        return (i-1)//2
    
    def __left(self,i:int)->int:
        r = 2*i + 1
        return r if r <= self.__last() else -1
    
    def __right(self,i:int)->int:
        r = 2*i + 2
        return r if r <= self.__last() else -1
    
    def __priority(self,index:int)->P:
        return self._map[self._elements[index]].priority
       
    def __index(self,e:E)->int:
        return self._map[e].index  
    
    def __choose(self,i:int)->int:
        left = self.__left(i)
        right = self.__right(i)
        r: int = -1
        if left == -1 and right == -1:
            r = -1
            return r
        if right == -1  and self.__priority(i) < self.__priority(left):
            r = -1
            return r
        if right == -1:
            r = left
            return r
        if self.__priority(i) < self.__priority(right) and self.__priority(i) < self.__priority(left):
            r = -1
            return r
        r = left if self.__priority(left) < self.__priority(right) else right
        return r
    
    def __up(self,i:int)->None: 
        while i > 0 and self.__priority(i) < self.__priority(self.__parent(i)):
            self.__swap(i,self.__parent(i))
            i = self.__parent(i)
            
    def __down(self, i:int)->None:
        while True:
            m:int = self.__choose(i)
            if m == -1:
                break
            self.__swap(i,m)
            i = m
        
    def add(self,e:E,priority:P)->None:
        index:int = len(self._elements)
        self._elements.append(e) 
        d: Datos[P] = Datos.of(priority,index)      
        self._map[e] = d
        self.__up(self.__last())
    
    def remove(self)->E:  
        assert len(self._elements) > 0, 'El agregado esta vacío'
        e = self._elements[0]
        self._map.pop(e)
        self._elements[0] = self._elements[self.__last()]
        self._elements.pop()
        self.__down(0)
        return e
     
    def decrease_priority(self,e:E,new_priority:P)->None:
        i:int = self.__index(e)
        if new_priority < self.__priority(i):
            self._map[e].priority = new_priority
            self.__up(i)
       

if __name__ == '__main__':
    
    cl:Cola_de_prioridad[int,int] = Cola_de_prioridad.of(Implementacion.MONTON)
    ls = [2,32,-4156,557,3,5,7,8,9,10,-11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    cl.add_all([(x,x) for x in ls])
    cl.decrease_priority(557, -5)
    print(cl.remove_all())
    cm:Cola_de_prioridad[int,int] = Cola_de_prioridad.of(Implementacion.LISTA)
    cm.add_all([(x,x) for x in ls])
    cm.decrease_priority(557, -5)
    print(cm.remove_all())
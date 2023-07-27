'''
Created on 10 oct 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Generic, Callable
from abc import abstractmethod

E = TypeVar("E")
R = TypeVar("R")

identity = lambda x:x

class Matriz(Generic[E]):
    
    def __init__(self,datos: list[list[E]])->None:
        self.datos: list[list[E]] = datos    
    
    
    @staticmethod
    def of(datos: list[list[E]])->Matriz[E]:
        pass
    
    
    @staticmethod
    def parse(file:str,t:Callable[[str],E]= identity,delimiter=' ',encoding='utf-8')->Matriz[E]:
        pass
    
    @abstractmethod
    def nf(self)->int:  
        pass
    
    @abstractmethod    
    def nc(self)->int:   
        pass 
    
    @abstractmethod
    def get(self,f:int,c:int)->E: 
        pass  
    
    @abstractmethod
    def submatriz(self,f1:int,c1:int,f2:int,c2:int)->Matriz[E]:    
        pass
    
    @abstractmethod
    def traspuesta(self)->Matriz[E]:
        pass
    
    @abstractmethod
    def map(self,t:Callable[[E],R])->Matriz[R]:
        pass
    
    @abstractmethod     
    def es_simetrica(self):
        pass
    
    @abstractmethod
    def __eq__(self,other:object)->bool:
        pass
    
    @abstractmethod      
    def __str__(self) -> str:
        pass

if __name__ == '__main__':
    pass
  
    
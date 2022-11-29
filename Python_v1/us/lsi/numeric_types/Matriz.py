'''
Created on 10 oct 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Generic, Callable, Iterable
from us.lsi.tools.Preconditions import check_argument
from us.lsi.tools.File import lineas_de_csv, absolute_path, encoding
from us.lsi.tools.Iterable import all_pairs

E = TypeVar("E")
R = TypeVar("R")

identity = lambda x:x

class Matriz(Generic[E]):
    
    def __init__(self,datos: list[list[E]])->None:
        self.datos: list[list[E]] = datos    
    
    @staticmethod
    def of(datos: list[list[E]])->Matriz[E]:
        check_argument(all(len(x)==len(datos[0]) for x in datos),f'La filas deben ser de igual tamanyo')
        return Matriz(datos)
    
    @staticmethod
    def of_file(file:str,t:Callable[[str],R]= identity,delimiter=' ',encoding='utf-8')->Matriz[R]:
        filas:list[list[str]] = lineas_de_csv(file,delimiter=delimiter,encoding=encoding)
        return Matriz.of(filas).map(t)
    
    @property
    def nf(self)->int:  
        return len(self.datos)
    
    @property
    def nc(self)->int:   
        return len(self.datos[0]) 
    
    def get(self,f:int,c:int)->E: 
        return self.datos[f][c]   
    
    def submatriz(self,f1:int,c1:int,f2:int,c2:int)->Matriz[E]:    
        filas: list[list[E]] = self.datos[f1:f2]  
        datos: list[list[E]] = [f[c1:c2] for f in filas]
        return Matriz.of(datos)
    
    @property
    def traspuesta(self)->Matriz[E]:
        datos:list[list[E]] = [[self.get(c,f) for c in range(self.nf)] for f in range(self.nc)]
        return Matriz.of(datos)
    
    def map(self,t:Callable[[E],R])->Matriz[R]:
        datos:list[list[R]] = [[t(self.get(f,c)) for c in range(self.nc)] for f in range(self.nf)]
        return Matriz.of(datos)
          
    @property
    def es_simetrica(self):
        indices:Iterable[tuple[int,int]] = (p for p in all_pairs(self.nf,self.nc) if p[0] > p[1])
        return all(self.get(f,c) == self.get(c,f) for f,c in indices)
    
    def __eq__(self,other:object)->bool:
        if not isinstance(other, Matriz):
            return False       
        return self.datos == other.datos
           
    def __str__(self) -> str:
        fs:Callable[[int],str] = lambda f:' '.join(f'{str(x):>5s}' for x in self.datos[f])
        return '\n'.join(fs(f) for f in range(self.nf))

if __name__ == '__main__':
    print(encoding(absolute_path('/resources/matriz1.txt')))
    m:Matriz[str]= Matriz.of_file(absolute_path('/resources/matriz1.txt'))
    print(m)
    print('_________________')
    print(m.traspuesta)
    print('_________________')
    print(m.get(2,3))
    print(m.nf)
    print(m.nc)
    print(m.submatriz(1, 1, 5, 4))
    print(m.es_simetrica)
    print('_________________')
    
     
    
    
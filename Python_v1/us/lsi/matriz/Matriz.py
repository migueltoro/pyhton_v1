'''
Created on 25 oct 2022

@author: belen
'''

from __future__ import annotations
from typing import TypeVar, Generic, Callable
from us.lsi.tools import Preconditions
from us.lsi.tools.File import lineas_de_csv, encoding, absolute_path
from us.lsi.tools.Iterable import all_pairs, Iterable

E = TypeVar("E")

class Matriz(Generic[E]):
    #===========================================================================
    # CONSTRUCTOR
    #===========================================================================
    def __init__(self, datos: list[list[E]]) -> None:
        self.datos: list[list[E]] = datos
    
    #===========================================================================
    # MÉTODOS DE FACTORÍA
    #===========================================================================
    @staticmethod
    def of(datos:list[list[E]]) -> Matriz[E]:
        Preconditions.check_argument(len(datos) > 0, 'El número de filas tiene que ser mayor que cero')
        Preconditions.check_argument(all(len(x)>0 for x in datos), 'El número de columnas tiene que ser mayor que cero')
        Preconditions.check_argument(all(len(x)==len(datos[0]) for x in datos), 'Todas las filas tienen que tener el mismo tamaño')
        return Matriz(datos)
    
    @staticmethod
    def of_file(fichero:str, t:Callable[[str],E]) -> Matriz[E]:
        datos_aux: list[list[str]] = list(lineas_de_csv(fichero,delimiter=' ',encoding=encoding(fichero)))
        datos: list[list[E]] = [[t(datos_aux[f][c]) for c in range(len(datos_aux[0]))] for f in range(len(datos_aux))]
        return Matriz.of(datos)
                                     
    #===========================================================================
    # PROPIEDADES DERIVADAS
    #===========================================================================
    @property
    def nf(self)->int:  
        return len(self.datos)
    
    @property
    def nc(self)->int:   
        return len(self.datos[0]) 
    
    def get(self,f:int,c:int)->E: 
        return self.datos[f][c] 
    
    @property
    def traspuesta(self)->Matriz[E]:
        datos: list[list[E]] = [[self.get(c, f) for c in range(self.nf)] for f in range(self.nc)]
        return Matriz.of(datos)
        
    @property
    def es_simetrica(self)->bool:
#        return self.nc == self.nf and self == self.traspuesta
        indices:Iterable[tuple[int,int]] = (p for p in all_pairs(self.nf,self.nc) if p[0] > p[1])
        return all(self.get(f,c) == self.get(c,f) for f,c in indices)
        
        

    
    #===========================================================================
    # REPRESENTACIÓN COMO CADENA
    #===========================================================================
    
    def __str__(self) -> str:
        fs:Callable[[int],str] = lambda f:' '.join(f'{str(e):>5s}' for e in self.datos[f])
        return '\n'.join(fs(f) for f in range(self.nf))
    

    #===========================================================================
    # CRITERIO DE IGUALDAD
    #===========================================================================
    def __eq__(self, other) -> bool:
#        return self.datos==(other.datos)
        indices:Iterable[tuple[int,int]] = (p for p in all_pairs(self.nf,self.nc))
        return all(self.get(f,c) == other.get(f,c) for f,c in indices)
    
        
if __name__ == '__main__':
    m3:Matriz[int] = Matriz.of_file(absolute_path('/resources/matriz4.txt'),lambda x:int(x))
    print(m3)
    print('___________')
    print(m3.traspuesta)
    
        
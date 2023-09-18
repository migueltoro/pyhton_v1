'''
Created on 24 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Callable
from us.lsi.tools import Preconditions
from us.lsi.tools.File import lineas_de_csv, absolute_path
from us.lsi.matriz.Matriz import Matriz
from us.lsi.tools.Functions import identity

E = TypeVar("E")
R = TypeVar("R")

class MatrizI(Matriz[E]):
    #===========================================================================
    # CONSTRUCTOR
    #===========================================================================
    def __init__(self, datos: list[list[E]]) -> None:
        super().__init__(datos)
    
    #===========================================================================
    # MÉTODOS DE FACTORÍA
    #===========================================================================
    @staticmethod
    def of(datos:list[list[E]]) -> MatrizI[E]:
        Preconditions.check_argument(len(datos) > 0, 'El número de filas tiene que ser mayor que cero')
        r1:bool = True
        for e in datos:
            if not len(e)>0:
                r1 = False
                break
        Preconditions.check_argument(r1, 'El número de columnas tiene que ser mayor que cero')
        r2:bool = True
        for e in datos:
            if not len(e)==len(datos[0]):
                r2 = False
                break
        Preconditions.check_argument(r2, 'Todas las filas tienen que tener el mismo tamaño')
        return MatrizI(datos)
    
    @staticmethod
    def parse(file:str,t:Callable[[str],E]= identity,delimiter=' ',encoding='utf-8') -> MatrizI[E]:
        datos_f: list[list[str]] = list(lineas_de_csv(file,delimiter=delimiter,encoding=encoding))
        dt:list[list[E]] = []
        for ln in datos_f:
            fila: list[E] = []
            for x in ln:
                e:E = t(x)
                fila.append(e)
            dt.append(fila)
        return MatrizI.of(dt)
                                     
    #===========================================================================
    # PROPIEDADES DERIVADAS
    #===========================================================================
    
    def nf(self)->int:  
        return len(self.datos)
    
    
    def nc(self)->int:   
        return len(self.datos[0]) 
    
    def get(self,f:int,c:int)->E: 
        return self.datos[f][c] 
    
    
    def traspuesta(self)->Matriz[E]:
        dt:list[list[E]] = []
        for f in range(self.nc()):
            fila: list[E] = []
            for c in range(self.nc()):
                fila.append(self.get(c,f))
            dt.append(fila)
        return Matriz.of(dt)
        
    def es_simetrica(self)->bool:
        return self == self.traspuesta
    
    def submatriz(self,f1:int,c1:int,f2:int,c2:int):    
        pass
    
    def map(self,t:Callable[[E],R]):
        pass 
    
    #===========================================================================
    # REPRESENTACIÓN COMO CADENA
    #===========================================================================
    
    def __str__(self) -> str:
        fs:Callable[[int],str] = lambda i:' '.join(f'{str(x):>5s}' for x in self.datos[i])
        return '\n'.join(fs(i) for i in range(self.nf()))
    
    #===========================================================================
    # CRITERIO DE IGUALDAD
    #===========================================================================
    def __eq__(self, other) -> bool:
##        return self.datos==other.datos
        r = self.nf() == other.nf() and self.nc() == other.nc()
        for f in range(self.nc()):
            for c in range(self.nc()):
                r = self.get(f,c) == other.get(f,c)
                if not r:
                    break
        return r
           
if __name__ == '__main__':
    m3:MatrizI[int] = MatrizI.parse(absolute_path('/datos/matriz4.txt'),lambda x:int(x))
    print(m3)
    print('___________')
    print(m3.traspuesta)     

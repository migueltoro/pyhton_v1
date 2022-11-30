'''
Created on 27 oct 2022

@author: migueltoro
'''
from __future__ import annotations
from typing import TypeVar, Callable, Iterable
from us.lsi.tools.Preconditions import check_argument
from us.lsi.tools.File import absolute_path
from us.lsi.tools.Iterable import all_pairs, first_index_if
from fractions import Fraction
from functools import reduce
from operator import mul
from us.lsi.numeric_types.Field import FieldElement,Field,FractionField
from us.lsi.numeric_types.Matriz import Matriz

S = TypeVar('S',bound=FieldElement)

identity = lambda x:x

class Matriz_field(Matriz[S]):
    
    def __init__(self,datos: list[list[S]], field:Field[S])->None:
        super().__init__(datos)
        self.field = field
    
    @staticmethod
    def of_datos(datos: list[list[S]],field:Field[S]):
        return Matriz_field(datos,field)
    
    @staticmethod
    def of_file_field(file:str,field:Field[S],delimiter=' ',encoding='utf-8')->Matriz_field[S]:
        m:Matriz[S]= Matriz.of_file(file,lambda x:field.parse(x),delimiter,encoding)
        return Matriz_field(m.datos,field)
    
    @staticmethod
    def matriz_unidad(nf:int,field:Field[S])->Matriz_field[S]:
        one:S = field.one()
        zero:S = field.zero()
        datos:list[list[S]] = [[one if c == f else zero for c in range(nf)] for f in range(nf)]
        m = Matriz_field(datos,field)
        return m
    
    @staticmethod
    def matriz_zero(nf:int,field:Field[S])->Matriz_field[S]:
        zero:S = field.zero()
        datos:list[list[S]] = [[zero for _ in range(nf)] for _ in range(nf)]
        return Matriz_field(datos,field)
    
    def __str__(self) -> str:
        fs:Callable[[int],str] = lambda f:' '.join(f'{self.field.str(x):s}' for x in self.datos[f])
        return '\n'.join(fs(f) for f in range(self.nf))
       
    def __cambia_filas(self,f1:int,f2:int)->None:
        self.datos[f1],self.datos[f2] = self.datos[f1],self.datos[f2]

    def __busca_primera_fila(self,c:int)->int:
        zero:S = self.field.zero()
        it:Iterable[S]=(self.datos[i][c] for i in range(c,len(self.datos)))
        return first_index_if(it, lambda e: e!=zero)
    
    def __multiplica_fila_por_factor(self,f:int,factor:S)->None:
        self.datos[f] = [e*factor for e in self.datos[f]]
        
    def __resta_fila_por_factor(self,f1:int,f2:int,factor:S)->None:
        self.datos[f1] = [e1-e2*factor for e1,e2 in zip(self.datos[f1],self.datos[f2])]
   
    def __add__(self,other:Matriz_field[S])->Matriz_field[S]:
        datos:list[list[S]] = [[self.get(f,c) + other.get(f,c) for c in range(self.nc)] for f in range(self.nf)]
        return Matriz_field.of_datos(datos,self.field)
    
    def __sub__(self,other:Matriz_field[S])->Matriz_field[S]:
        datos:list[list[S]] = [[self.get(f,c) - other.get(f,c) for c in range(self.nc)] for f in range(self.nf)]
        return Matriz_field.of_datos(datos,self.field)  

    def __mul__(self,other:Matriz_field[S])->Matriz_field[S]:
        check_argument(self.nc == other.nf, f'No se pueden multiplicar')
        zero:S = self.field.zero()
        ss:Callable[[int,int],S] = \
            lambda f,c:sum((self.get(f,k)*other.get(k,c) for k in range(self.nc)),zero)
        datos:list[list[S]] = [[ss(f,c) for c in range(other.nc)] for f in range(self.nf)]
        return Matriz_field.of_datos(datos,self.field)
    
    def __pow__(self,n:int)->Matriz_field[S]:
        return reduce(mul,(self for _ in range(n)),Matriz_field.matriz_unidad(self.nf,self.field))
    
    @property
    def es_antisimetrica(self):
        indices:Iterable[tuple[int,int]] = ((f,c) for f,c in all_pairs(self.nf,self.nc) if f >= c)
        return all(self.get(i,j) == self.field.zero() - self.get(j,i) for i,j in indices)
    
    @property
    def traza(self):
        return sum((self.get(i,i) for i in range(self.nf) if i<self.nf and i<self.nc),self.field.zero())
   
    @property
    def aumentada(self):
        one:S = self.field.one()
        zero:S = self.field.zero()
        ff:Callable[[int],list[S]] = lambda c: [one if i == c else zero for i in range(self.nc)]
        datos:list[list[S]] = [self.datos[f]+ff(f) for f in range(self.nf)]
        return Matriz_field.of_datos(datos,self.field)
   
    def __invert__(self)->Matriz_field:
        check_argument(self.nc == self.nf, f'Debe ser cuadrada')
        one:S = self.field.one()
        ma:Matriz_field = self.aumentada
        for fp in range(ma.nf):
            pf:int=ma.__busca_primera_fila(fp)
            if pf == -1:
                raise Exception('La matriz no se puede invertir')
            else:
                pf = pf+fp
                if pf != fp:
                    ma.__cambia_filas(fp,pf)
                if ma.datos[fp][fp] != one:
                    ma.__multiplica_fila_por_factor(fp, one/ma.datos[fp][fp])                                            
                for f in range(fp+1,ma.nf):
                    ma.__resta_fila_por_factor(f, fp, ma.datos[f][fp])                                 
        for fp in range(ma.nf-1,0,-1):                          
                for f in range(fp-1,-1,-1):
                    ma.__resta_fila_por_factor(f, fp, ma.datos[f][fp])                                                                      
        return Matriz_field.of_datos(ma.submatriz(0, self.nc, self.nf, ma.nc).datos,self.field)
    
    @property
    def determinante(self)->S:
        check_argument(self.nc == self.nf, f'Debe ser cuadrada')
        one:S = self.field.one()
        zero:S = self.field.zero()
        det: S = one
        ma:Matriz_field = self.aumentada
        for fp in range(ma.nf):
            pf:int=ma.__busca_primera_fila(fp)
            if pf == -1:
                return zero
            else:
                pf = pf+fp
                if pf != fp:
                    ma.__cambia_filas(fp,pf)
                if ma.datos[fp][fp] != Fraction(1):
                    det = det*ma.datos[fp][fp]
                    ma.__multiplica_fila_por_factor(fp, 1/ma.datos[fp][fp])                                                           
                for f in range(fp+1,ma.nf):
                    ma.__resta_fila_por_factor(f, fp, ma.datos[f][fp])                                 
        for fp in range(ma.nf-1,0,-1):                          
                for f in range(fp-1,-1,-1):
                    ma.__resta_fila_por_factor(f, fp, ma.datos[f][fp])                                                                      
        return det                                                                     
    
    def __truediv__(self,other:Matriz_field):
        return self*(~other)
    
    @property
    def solve(self)->Matriz_field:
        check_argument(self.nc == self.nf+1, f'Debe cumplirse que nc = nf +1 y tenemos nc={self.nc}, nf={self.nf}')
        m = Matriz_field.of_datos(self.submatriz(0, 0, self.nf, self.nc-1).datos,self.field)
        v = Matriz_field.of_datos(self.submatriz(0, self.nc-1, self.nf, self.nc).datos,self.field)
        mi = ~m
        return mi*v

if __name__ == '__main__':
    m2:Matriz_field[Fraction] = Matriz_field.of_file_field(absolute_path('/resources/matriz2.txt'),FractionField())
    print(m2)
    print(m2.es_antisimetrica)
    print('_________________')
    m3:Matriz_field[Fraction] = Matriz_field.of_file_field(absolute_path('/resources/matriz3.txt'),FractionField())
    print(m2+m3)
    print(m2-m3)
    print(m2*m3)
    print(m2**5)
    print(m3.traza)
    print('_________________')
    m4:Matriz_field[Fraction] = Matriz_field.of_file_field(absolute_path('/resources/matriz6.txt'),FractionField())
    print(m4.solve)
    print('_________________')
    print(m4)
    print('_________________')
    print(m4.traspuesta)
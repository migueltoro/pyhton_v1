'''
Created on 24 nov 2022

@author: migueltoro
'''

from __future__ import annotations

from fractions import Fraction
from us.lsi.matriz.MatrizI import MatrizI
from us.lsi.tools.File import absolute_path


class MatrizF(MatrizI[Fraction]):
    #===========================================================================
    # MÉTODOS DE FACTORÍA
    #===========================================================================
        
    @staticmethod
    def of(datos:list[list[Fraction]])->MatrizF:
        return MatrizF(datos)
    
    @staticmethod
    def of_file_fraction(file:str)->MatrizF:
        return MatrizF.of(MatrizI.parse(file, lambda x: Fraction(x)).datos)

    #===========================================================================
    # PROPIEDADES DERIVADAS
    #===========================================================================
    @property
    def es_antisimetrica(self)->bool:
        r:bool = True
        for f in range(self.nf()):
            for c in range(self.nc()):
                r = self.get(f, c) == -self.get(f, c)
                if not r:
                    r1 = False
                    break
        return r1
    
    #===========================================================================
    # OTROS MÉTODOS
    #===========================================================================
    def __add__(self,other:MatrizF)->MatrizF:
        assert self.nf() == other.nf() and self.nc() == other.nc(), f'No se pueden sumar'
        dt:list[list[Fraction]] = []
        for f in range(self.nf()):
            fila: list[Fraction] = []
            for c in range(self.nc()):
                fila.append(self.get(f,c) + other.get(f,c))
            dt.append(fila)
        return MatrizF.of(dt)
    
    def __sub__(self,other:MatrizF)->MatrizF:
        assert self.nf() == other.nf() and self.nc() == other.nc(), f'No se pueden restar'
        dt:list[list[Fraction]] = []
        for f in range(self.nf()):
            fila: list[Fraction] = []
            for c in range(self.nc()):
                fila.append(self.get(f,c) - other.get(f,c))
            dt.append(fila)
        return MatrizF.of(dt)
    
    def __mul__(self,other:MatrizF)->MatrizF:
        assert self.nc() == other.nf(), f'No se pueden multiplicar'
        dt:list[list[Fraction]] = []
        for f in range(self.nf()):
            fila: list[Fraction] = []
            for c in range(self.nc()):
                s:Fraction=Fraction(0)
                for k in range(self.nc()):
                    s = s + self.get(f,k)*other.get(k,c)
                fila.append(s)
            dt.append(fila)
        return MatrizF.of(dt)
    

if __name__ == '__main__':
    m2:MatrizF = MatrizF.of_file_fraction(absolute_path('datos/matriz2.txt'))
    print(m2)
    print(m2.es_antisimetrica)
    m3:MatrizF = MatrizF.of_file_fraction(absolute_path('datos/matriz4.txt'))
    print(m3)
    print('----------------')
    m5:MatrizF = MatrizF.of_file_fraction(absolute_path('datos/matriz7.txt'))
    print(m5)
    print('----------------')
    print(m3+m5)
    print('----------------')
    print(m3-m5)
    print('----------------')
    print(m3*m5)
    print('----------------')
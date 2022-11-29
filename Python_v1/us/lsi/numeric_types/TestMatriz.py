'''
Created on 10 oct 2022

@author: migueltoro
'''
from us.lsi.tools.File import absolute_path
from novedades.generic_types.Matriz_field import Matriz_field
from fractions import Fraction
from novedades.generic_types.Field import FractionField,Field

if __name__ == '__main__':
    f: Field[Fraction] = FractionField()
    m3:Matriz_field[Fraction] = Matriz_field.of_file_type(absolute_path('/ficheros/matriz4.txt'),f)
    print(m3)
    print('----------------')
    m5:Matriz_field[Fraction] = Matriz_field.matriz_unidad(3, f)
    print(m5)
    print('----------------')
    print(m3+m5)
    print('----------------')
    print(m3-m5)
    print('----------------')
    print(m3*m5)
    print('----------------')
    m4 = ~m3
    print(m4)
    print('----------------')
    print(m3*m4)
    print(m3.determinante)
    print(m4.determinante)
    
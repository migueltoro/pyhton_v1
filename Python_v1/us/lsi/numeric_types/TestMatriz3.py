'''
Created on 11 oct 2022

@author: migueltoro
'''

from us.lsi.tools.File import absolute_path
from us.lsi.numeric_types.Matriz_field import Matriz_field
from us.lsi.numeric_types.Field import FractionField,Field,FloatField,ComplexField
from fractions import Fraction

if __name__ == '__main__':
    f1: Field[Fraction] = FractionField()
    m3:Matriz_field[Fraction] = Matriz_field.of_file_field(absolute_path('/resources/matriz7.txt'),f1)
    print(m3)
    print('----------------')
    m4 = ~m3
    print(m4)
    print('----------------')
    print(m3.determinante)
    print(m4.determinante)
    print('----------------')
    f2: Field[float] = FloatField()
    m5:Matriz_field[float] = Matriz_field.of_file_field(absolute_path('/resources/matriz8.txt'),f2)
    print(m5)
    print('----------------')
    m6 = ~m5
    print(m6)
    print('----------------')
    print(m5.determinante)
    print(m6.determinante)
    f3: Field[complex] = ComplexField()
    m7:Matriz_field[complex] = Matriz_field.of_file_field(absolute_path('/resources/matriz9.txt'),f3)
    print(m7)
    print('----------------')
    m8 = ~m7
    print(m8)
    print('----------------')
    print(f3.str(m7.determinante))
    print(f3.str(m8.determinante))
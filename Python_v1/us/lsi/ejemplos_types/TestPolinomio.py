'''
Created on 17 ago 2022

@author: migueltoro
'''
from us.lsi.ejemplos_types.Polinomio import Polinomio
from fractions import Fraction
from numbers import Number

if __name__ == '__main__':
    p0: Polinomio = Polinomio.of(Fraction(1),Fraction(1))
    p1 = p0+p0*Fraction(3)
    print(p1)
    p: Polinomio = Polinomio.of(Fraction(3),Fraction(-4),Fraction(5),Fraction(7))
    print(p)
    print(p.grado)
    print(isinstance(p.coeficiente(0), Number))
    print(p.value(Fraction(1)))
    print(p+p)
    print(p*Fraction(2))
    print('__________________')
    print(p.derivada)
    print(p.integral(Fraction(0)))
    print('__________________')
    p2 : Polinomio = Polinomio.of(Fraction(3,5),Fraction(-4,5),Fraction(7))
    print(p2)
    print(p2.grado)
    print(isinstance(p2.coeficiente(0), Number))
    print('__________________')
    print(p2.derivada)
    print(p2.integral(Fraction(0)))
    print('__________________')
    
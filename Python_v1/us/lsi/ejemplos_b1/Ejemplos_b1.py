'''
Created on 17 ago 2022

@author: migueltoro
'''
from us.lsi.tools.Preconditions import checkArgument
from us.lsi.tools.File import lineas_de_fichero, encoding
from math import sqrt, pi
import re

def parte_entera(a:float) -> int:
    return int(a)

def digito_decimal(a:float,n:int)->int:
    return int(a*10**n) %10

def digito_parte_entera(a:float,n:int)->int:
    return (int(a) // int(10**n)) % 10

def fact(n:int)->int:
    checkArgument(n>=0,f'n debe ser mayor que cero y es {n}')
    r = 1
    for i in range(2,n+1):
        r = r*i
    return r

def sol_ecuacion_primer_grado(a:float,b:float) -> float: 
    checkArgument(a>0,f'El coeficiente a debe ser distinto de cero y es {a:.2f}')
    return -b/a
    
def sol_ecuacion_segundo_grado(a:float,b:float,c:float) -> tuple[float,float] | tuple[complex,complex]:
    checkArgument(a>0,f'El coeficiente a debe ser distinto de cero y es {a:.2f}')
    disc = b*b-4*a*c
    if disc >= 0 :
        r1 = -b/(2*a)
        r2 = sqrt(disc)/(2*a)
        s1,s2 = r1+r2,r1-r2
        return (s1,s2)
    else :
        re = -b/(2*a)
        im = sqrt(-disc)/(2*a)
        s1,s2 = complex(re,im),complex(re,-im)
        return (s1,s2) 
    
def area_circulo(radio:float) -> float:
    checkArgument(radio>=0,f'El radio debe ser mayor o igual a cero y es {radio:.2f}')
    return pi*radio**2

def longitud_circunferencia(radio:float) -> float:
    checkArgument(radio>=0,f'El radio debe ser mayor o igual a cero y es {radio:.2f}')
    return 2*pi*radio

def mcd(a:int, b:int)->int:
    checkArgument(a>=0 and b>0,f'El coeficiente a debe ser mayor o igual que cero y b mayor que cero y son: a = {a}, b = {b}')
    while b > 0:
        a, b = b, a%b
    return a

def numero_de_lineas(file: str) -> int:
    return len(lineas_de_fichero(file,encoding='utf-16'))

def numero_de_palabras_distintas(file: str) -> int:
    sep = r'[ ,;.\n():?!\"]'
    lns = lineas_de_fichero(file,encoding='utf-16')
    s = 0
    for linea in lns:
        for _ in re.split(sep, linea):
            s = s+1
    return s

if __name__ == '__main__':
    print(parte_entera(82.345))
    print(digito_decimal(82.345,4))
    print(digito_parte_entera(82457.34509,3))
    print(fact(11))
    print(sol_ecuacion_segundo_grado(1,-3,2))
    print(area_circulo(5.))
    print(encoding("../../../resources/quijote.txt"))
    print(numero_de_lineas("../../../resources/quijote.txt"))
    print(numero_de_palabras_distintas("../../../resources/quijote.txt"))
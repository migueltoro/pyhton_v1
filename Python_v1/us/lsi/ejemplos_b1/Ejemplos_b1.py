'''
Created on 17 ago 2022

@author: migueltoro
'''

from math import sqrt, pi

def parte_entera(a:float) -> int:
    return int(a)

def digito_decimal(a:float,n:int)->int:
    return int(a*10**n) %10

def digito_parte_entera(a:float,n:int)->int:
    return (int(a) // int(10**n)) % 10

def fact(n:int)->int:
    assert n>=0,f'n debe ser mayor que cero y es {n}'
    r = 1
    for i in range(2,n+1):
        r = r*i
    return r

def sol_ecuacion_primer_grado(a:float,b:float) -> float: 
    assert a>0,f'El coeficiente a debe ser distinto de cero y es {a:.2f}'
    return -b/a
    
def sol_ecuacion_segundo_grado(a:float,b:float,c:float) -> tuple[float,float] | tuple[complex,complex]:
    assert a != 0, f'El coeficiente a debe ser distinto de cero y es {a:.2f}'
    disc = b * b - 4 * a * c
    real_part = -b / (2 * a)
    imaginary_part = sqrt(abs(disc)) / (2 * a)
    if disc >= 0:
        return (real_part + imaginary_part, real_part - imaginary_part)
    else:
        return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part)) 
    
def area_circulo(radio:float) -> float:
    assert radio>=0,f'El radio debe ser mayor o igual a cero y es {radio:.2f}'
    return pi*radio**2

def longitud_circunferencia(radio:float) -> float:
    assert radio>=0,f'El radio debe ser mayor o igual a cero y es {radio:.2f}'
    return 2*pi*radio

def area_cilindro(radio:float,altura:float) -> float:
    assert radio>=0,f'El radio debe ser mayor o igual a cero y es {radio:.2f}'
    assert altura>=0,f'La altura debe ser mayor o igual a cero y es {altura:.2f}'
    return 2*pi*radio*(radio+altura)

def area_triangulo(a:float,b:float,c:float) -> float:
    assert a>0,f'El lado a debe ser mayor que cero y es {a:.2f}'
    assert b>0,f'El lado b debe ser mayor que cero y es {b:.2f}'
    assert c>0,f'El lado c debe ser mayor que cero y es {c:.2f}'
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))

if __name__ == '__main__':
    print(parte_entera(82.345))
    print(digito_decimal(82.345,4))
    print(digito_parte_entera(82457.34509,3))
    print(fact(11))
    print(sol_ecuacion_segundo_grado(1,-3,2))
    print(area_circulo(5.))
    
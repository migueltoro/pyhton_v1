'''
Created on 17 jul. 2020

@author: migueltoro

'''
from typing import Iterator, Tuple, Union
from math import pi,sqrt
from us.lsi.tools import Preconditions

ComplexFloat = Union[float,complex]
StrFloat = Union[float,str]

def area_circulo(radio:float) -> float:
    Preconditions.checkArgument(radio>=0,'El radio debe ser mayor o igual a cero y es {0:.2f}'.format(radio))
    return pi*radio**2

def longitud_circunferencia(radio:float) -> float:
    Preconditions.checkArgument(radio>=0,'El radio debe ser mayor o igual a cero y es {0:.2f}'.format(radio))
    return 2*pi*radio

#media = sum(x)/n
def media(iterable:Iterator[Union[int,float]]) -> float:
    a = (0.,0) #(sum x, num elem)
    for e in iterable:
        a = (a[0]+e,a[1]+1)
    return a[0]/a[1]  

# desv = sqrt(sum(x^2)/n-(sum(x)/n)^2)
def deviacion_tipica(iterable:Iterator[Union[int,float]]) -> float:
    a = (0.,0.,0)  #(sum x^2, sum x, num elem)
    for e in iterable:
        a = (a[0]+e*e,a[1]+e,a[2]+1)
    return sqrt(a[0]/a[2]-(a[1]/a[2])**2)  

def sol_ecuacion_primer_grado(a:float,b:float) -> StrFloat: 
    if b == 0 and a == 0:
        return 'Cualquier valor es valido'
    elif b == 0 and a != 0:
        return 0
    elif b != 0 and a == 0:
        return 'No hay solucion'
    else:
        return -b/a
    
def sol_ecuacion_segundo_grado(a:float,b:float,c:float) -> Union[StrFloat,Tuple[ComplexFloat,ComplexFloat]]: 
    if a == 0: 
        return sol_ecuacion_primer_grado(b,c)
    disc = b*b-4*a*c
    if disc >= 0 :
        s1,s2 = (-b+sqrt(disc))/(2*a),(-b-sqrt(disc))/(2*a)
        return (s1,s2)
    else :
        s1,s2 = complex(-b/(2*a),sqrt(-disc)/(2*a)),complex(-b/(2*a),-sqrt(-disc)/(2*a))
        return (s1,s2)
                                 
             
if __name__ == '__main__':
    print(sol_ecuacion_segundo_grado(1,1,1))
    print(area_circulo(5.))
    print(media(x for x in range(10,100) if x%2 == 0))
    print(deviacion_tipica(x*x for x in range(10,100) if x%3 == 0))
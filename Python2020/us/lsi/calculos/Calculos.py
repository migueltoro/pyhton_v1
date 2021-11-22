'''
Created on 17 jul. 2020

@author: migueltoro

'''
from typing import Iterable
from math import pi,sqrt
from us.lsi.tools import Preconditions
from statistics import mean, stdev, quantiles, pstdev
import random
from enum import Enum
from us.lsi.tools.Iterable import flat_map
from us.lsi.tools.File import lineas_de_fichero, lineas_de_csv, lineas_iterable

num = int | float

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    

def area_circulo(radio:float) -> float:
    Preconditions.checkArgument(
        radio>=0,'El radio debe ser mayor o igual a cero y es {0:.2f}'.format(radio))
    return pi*radio**2

def longitud_circunferencia(radio:float) -> float:
    Preconditions.checkArgument(radio>=0,'El radio debe ser mayor o igual a cero y es {0:.2f}'.format(radio))
    return 2*pi*radio

def cuadrados_de_multiplos_entre(a:int,b:int,c:int)-> Iterable[int]:
    return (x**2 for x in range(a,b) if x%c == 0)

def list_de_enteros_aleatorios_entre(a:int,b:int,n:int)-> Iterable[int]:
    return [random.randint(a,b) for _ in range(0,n)]

def conjunto_de_enteros_aleatorios_entre(a:int,b:int,n:int)-> set[int]:
    return {random.randint(a,b) for _ in range(0,n)}

# pares formados por enteros que son multiplos de c y estan entre a y b y sus cuadrados
def cuadrados_de_multiplos_entre_dict(a:int,b:int,c:int)-> dict[int,int]:
    return {x:x*x for x in range(a,b) if x%c == 0}

def progresion_aritmetica(a:int,b:int,c:int) -> Iterable[int]:
    return range(a,b,c)

def suma(iterable:Iterable[num]) -> num:
    a = 0 #(sum x, num elem)
    for e in iterable:
        a = a+e
    return a  

#media = sum(x)/n
def media(iterable:Iterable[num]) -> float:
    a = (0.,0) #(sum x, num elem)
    for e in iterable:
        a = (a[0]+e,a[1]+1)
    Preconditions.checkArgument(a[1]>0,'El iterador esta vacio')
    return a[0]/a[1]  

# desv = sqrt(sum(x^2)/n-(sum(x)/n)^2)
def deviacion_tipica(iterable:Iterable[num]) -> float:
    a = (0.,0.,0)  #(sum x^2, sum x, num elem)
    for e in iterable:
        a = (a[0]+e*e,a[1]+e,a[2]+1)
    Preconditions.checkArgument(a[2]>0,'El iterador esta vacio')
    return sqrt(a[0]/a[2]-(a[1]/a[2])**2)  

def sol_ecuacion_primer_grado(a:float,b:float) -> float: 
    Preconditions.checkArgument(a>0,'El coeficiente a debe ser distinto de cero y es {0:.2f}'.format(a))
    return -b/a
    
def sol_ecuacion_segundo_grado(a:float,b:float,c:float) -> tuple[float,float] | tuple[complex,complex]:
    Preconditions.checkArgument(a>0,'El coeficiente a debe ser distinto de cero y es {0:.2f}'.format(a))
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

def sum_file(file:str)->int:  
    itf =  lineas_de_csv(file) 
    it2 = (int(e) for e in flat_map(itf))
    return sum(it2)
                 
             
if __name__ == '__main__': 
    print(list(progresion_aritmetica(5,20, 3)))
    print(sol_ecuacion_segundo_grado(1,-3,2))
    print(area_circulo(5.))
    print(media(x for x in range(10,100) if x%2 == 0))
    print(deviacion_tipica(x*x for x in range(10,100) if x%3 == 0))
    it = cuadrados_de_multiplos_entre(10, 100, 3)
    print(deviacion_tipica(it))
    print(stdev(cuadrados_de_multiplos_entre(10, 100, 3)))
    print(media(cuadrados_de_multiplos_entre(10, 100, 3)))
    print(mean(cuadrados_de_multiplos_entre(10, 100, 3)))
    print(quantiles(cuadrados_de_multiplos_entre(10, 100, 3),n=10))
    print(list_de_enteros_aleatorios_entre(10,100,3))
    print(conjunto_de_enteros_aleatorios_entre(10,100,50))
    print(list(cuadrados_de_multiplos_entre(10, 100, 3)))
    print(cuadrados_de_multiplos_entre_dict(10, 100, 3))
    print(list(progresion_aritmetica(3,40,7)))
    print(deviacion_tipica(progresion_aritmetica(10,100,7)))
    print(pstdev(progresion_aritmetica(10,100,7)))
    print(media(progresion_aritmetica(10,100,7)))
    print(mean(progresion_aritmetica(10,100,7)))
    print(range(10,100)[2])
    print('__________________________')
    print(sum_file("../../../resources/datos_2.txt"))
    print(len(range(1000)))
    
    
    
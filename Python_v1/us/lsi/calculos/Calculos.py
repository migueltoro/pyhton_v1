'''
Created on 17 jul. 2020

@author: migueltoro

'''
from typing import Iterable
from math import sqrt
from us.lsi.tools import Preconditions
from statistics import mean, stdev, quantiles, pstdev
import random
from enum import Enum
from us.lsi.tools.Iterable import flat_map
from us.lsi.tools.File import lineas_de_csv


num = int | float

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    
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
    a:num = 0 #(sum x, num elem)
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



def sum_file(file:str)->int:  
    it0:Iterable[list[str]] =  lineas_de_csv(file) 
    it1:Iterable[int] = flat_map(it0)
    it2:Iterable[int] = (int(e) for e in it1)
    return sum(it2)
            
             
if __name__ == '__main__': 
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
    print
    
    
    
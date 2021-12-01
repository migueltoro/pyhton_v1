'''
Created on 11 nov 2021

@author: migueltoro
'''
import random
import math
from us.lsi.tools.File import lineas_de_fichero
numeros = [random.randint(1, 100) for _ in range(10)]
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.tools.Draw import draw_multiline

def montecarlo(n:int):
    puntos = (Punto2D.of(random.uniform(-1.,1.),random.uniform(-1.,1.)) for _ in range(n))
    pt=0
    pi = 0
    for p in puntos:
        pt = pt +1
        if p.distancia_al_origen <= 1:
            pi = pi +1
    return 4*pi/pt

def montecarlo_list(n:int):
    ls = []
    puntos = (Punto2D.of(random.uniform(-1.,1.),random.uniform(-1.,1.)) for _ in range(n))
    pt=0
    pi = 0
    i = 0
    for p in puntos:
        pt = pt +1
        i = i+1
        if p.distancia_al_origen <= 1:
            pi = pi +1
        if i%500==0:
            ls.append((i,4*pi/pt))
    return ls
    
if __name__ == '__main__':
    i = 0
    for n in numeros:
        print(i, n, sep=': ') 
        i = i+1

    texto = "Muestrame con puntos"
    for c in texto:
        print(c,end='.') 
    
    with open('../../../resources/datos_2.txt', encoding='utf-8') as f:
        contenido = f.read()
    
    print(contenido)  # Mostramos el contenido del fichero
    
    with open('../../../resources/datos_2.txt', encoding='utf-8') as f:
        for linea in f:
            print(linea,end='')
    
    print(f)
            
    ls = lineas_de_fichero('../../../resources/datos_2.txt')
    print(ls)
    
    print(math.pi)
    r = montecarlo_list(1000000)
    draw_multiline(r)
    print(r[-1])



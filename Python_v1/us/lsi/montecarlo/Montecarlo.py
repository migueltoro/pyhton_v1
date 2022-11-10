'''
Created on 10 nov 2022

@author: migueltoro
'''

from us.lsi.geometria.Punto2D import Punto2D
import random
import math
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

def montecarlo_list(n:int)->list[tuple[float,float]]:
    ls:list[tuple[float,float]] = []
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
    print(math.pi)
    print(montecarlo(1000000))
    r = montecarlo_list(1000000)
    draw_multiline(r)
    print(r[-1][0])
    print(r[-1][1])
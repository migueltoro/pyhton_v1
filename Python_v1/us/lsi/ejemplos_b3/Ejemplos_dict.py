'''
Created on 6 nov 2022

@author: migueltoro
'''

from collections import Counter
import random


diccionario = {"clave1": "valor1", "clave2": "valor2", \
     "clave3": "valor3"}
iterable = (random.randint(0,100) for _ in range(100))
frecuencias:Counter[int] = Counter(iterable)
mc:list[tuple[int,int]] = frecuencias.most_common(5)
fc:tuple[int,int] = frecuencias.most_common(1)[0]

if __name__ == '__main__':
    print(set(diccionario.keys()))
    print(set(diccionario.values()))
    print(set(diccionario.items()))
    print(frecuencias)
    print(mc)
    print(fc)
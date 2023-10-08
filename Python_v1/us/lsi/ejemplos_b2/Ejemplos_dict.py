'''
Created on 6 nov 2022

@author: migueltoro
'''

from collections import Counter
import random
from typing import Iterable, Iterator


diccionario = {"clave1": "valor1", "clave2": "valor2", \
     "clave3": "valor3"}
iterable = (random.randint(0,100) for _ in range(100))
frecuencias:Counter[int] = Counter(iterable)
mc:list[tuple[int,int]] = frecuencias.most_common(5)
fc:tuple[int,int] = frecuencias.most_common(1)[0]
f2: dict[int,int] = frecuencias
# mc = f2.most_common(5)
# fc= f2.most_common(1)[0]

if __name__ == '__main__':
    print(set(diccionario.keys()))
    print(set(diccionario.values()))
    print(set(diccionario.items()))
    print(frecuencias)
    print(mc)
    print(fc)
    it1:Iterable[str] = diccionario.keys()
    it2:Iterable[tuple[str,str]] = diccionario.items()
    it4:Iterator[str] = iter(it1)
    try:
        while True:
            print(next(it4))
    except StopIteration:
        pass
    
'''
Created on 10 nov 2022

@author: migueltoro
'''


from typing import Iterable
from us.lsi.tools.Iterable import str_iter,flat_map
from us.lsi.tools.Dict import str_dict
from collections import Counter
import random

iterable = (random.randint(0,100) for _ in range(100))
frecuencias:Counter[int] = Counter(iterable)

if __name__ == '__main__':
    print(str_iter(range(0,100)))
    r: Iterable[int] = flat_map([[0,1],[2,3,4],[5,6],[9]],lambda x:x)
    print(str_iter(r,sep=';',prefix='[',suffix=']'))
    print(str_iter(range(2,100,5)))
    print(str_dict(frecuencias,sep='\n',prefix='',suffix=''))
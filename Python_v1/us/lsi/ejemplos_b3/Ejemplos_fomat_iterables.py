'''
Created on 10 nov 2022

@author: migueltoro
'''

from typing import Iterable
from us.lsi.tools.Iterable import strfiter,flat_map
from us.lsi.tools.Dict import strfdict
from collections import Counter
import random

iterable = (random.randint(0,100) for _ in range(100))
frecuencias:Counter[int] = Counter(iterable)

if __name__ == '__main__':
    print(strfiter(range(0,100)))
    r: Iterable[int] = flat_map([[0,1],[2,3,4],[5,6],[9]],lambda x:x)
    print(strfiter(r,sep=';',prefix='[',suffix=']'))
    print(strfiter(range(2,100,5)))
    print(strfdict(frecuencias,sep='\n',prefix='',suffix=''))
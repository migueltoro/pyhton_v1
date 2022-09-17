'''
Created on 19 jul. 2020

@author: migueltoro
'''


from typing import TypeVar
from us.lsi.tools.Preconditions import check_argument

E = TypeVar('E')

def identity(e:E) -> E:
    return e

def mcd(a:int, b:int)->int:
    check_argument(a>=0 and b>0,'El coeficiente a debe ser mayor o igual que cero y b mayor que cero y son: \
    a = {0}, b = {1}'.format(a,b))
    while b > 0:
        a, b = b, a%b
    return a

if __name__ == '__main__':
    pass
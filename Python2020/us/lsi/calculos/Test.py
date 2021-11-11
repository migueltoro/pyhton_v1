'''
Created on 11 nov 2021

@author: migueltoro
'''
from typing import Iterator

def n()->int:
    n = 0
    yield n
    n = n+1
    
def it()->Iterator[int]:
    return iter(n())

if __name__ == '__main__':
    a = it()
    print(next(a))
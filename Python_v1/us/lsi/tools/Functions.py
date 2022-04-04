'''
Created on 19 jul. 2020

@author: migueltoro
'''


from typing import TypeVar


E = TypeVar('E')

def identity(e:E) -> E:
    return e

if __name__ == '__main__':
    pass
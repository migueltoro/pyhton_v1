'''
Created on 19 jul. 2020

@author: migueltoro
'''

from typing import TypeVar
from optional import Optional


E = TypeVar('E')

def identity(e:E) -> E:
    return e

def optional(e:E) -> Optional:
    if e is None:
        return Optional.empty()
    else:
        return Optional.of(e)

if __name__ == '__main__':
    print(optional(3).get())
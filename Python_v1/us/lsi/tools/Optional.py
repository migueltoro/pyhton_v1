'''
Created on 20 nov 2023

@author: migueltoro
'''

from typing import TypeVar, Optional

E = TypeVar('E')

def optional_get(e:Optional[E])->E:
    assert e is not None, f'El elemento {e} es None'
    return e

def is_empty(e:Optional[E])->bool:
    if e is None:
        return True
    else:
        return False
    
if __name__ == '__main__':
    pass
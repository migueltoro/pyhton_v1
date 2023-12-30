'''
Created on 20 nov 2023

@author: migueltoro
'''

from typing import TypeVar, Optional

E = TypeVar('E')

def optional_get(e:Optional[E])->E:
    assert e is not None, f'El elemento {e} es None'
    return e

def optional_is_empty(e:Optional[E])->bool:
    if e is None:
        return True
    else:
        return False

def optional_get_or_else(e:Optional[E], other:E)->E:
    if e is None:
        return other
    else:
        return e

    
    
    
if __name__ == '__main__':
    pass
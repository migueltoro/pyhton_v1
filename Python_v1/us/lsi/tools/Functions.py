'''
Created on 25 nov 2022

@author: migueltoro
'''

from typing import TypeVar, Optional

E = TypeVar('E')

identity = lambda x: x

def optional_has_value(value:Optional[E])->bool:
    if value is None:
        return False
    else:
        return True

def optional_get(value:Optional[E])->E:
    if value is not None:
        return value
    else:
        raise(Exception('El valor es None'))
    


if __name__ == '__main__':
    pass
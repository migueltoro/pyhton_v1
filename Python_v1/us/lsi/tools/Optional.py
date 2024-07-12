'''
Created on 20 nov 2023

@author: migueltoro
'''

from typing import TypeVar, Optional

E = TypeVar('E')

def optional_get(e:Optional[E])->E:
    '''
    This function asserts that the input is not None and returns the input.

    Parameters:
    e: The input which should not be None.

    Returns:
    The input e.

    Raises:
    AssertionError: If the input e is None.
    '''
    assert e is not None, f'El elemento {e} es None'
    return e

def optional_is_empty(e:Optional[E])->bool:
    '''
    This function checks if the input is None.

    Parameters:
    e: The input which is checked for None.

    Returns:
    True if the input e is None, False otherwise.
    '''
    return e is None

def optional_is_present(e:Optional[E])->bool:
    '''
    This function checks if the input is not None.

    Parameters:
    e: The input which is checked for None.

    Returns:
    True if the input e is not None, False otherwise.
    '''
    return e is not None

def optional_get_or_else(e:Optional[E], other:E)->E:
    '''
    This function returns the input e if it is not None, otherwise it returns the other input.

    Parameters:
    e: The input which is checked for None.
    other: The input which is returned if e is None.

    Returns:
    The input e if it is not None, otherwise the input other.
    '''
    return e if e is not None else other  
    
if __name__ == '__main__':
    pass
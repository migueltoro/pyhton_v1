'''
Created on 15 jul. 2020

@author: migueltoro
'''

from typing import TypeVar

E = TypeVar('E')

'''
* Checks that the boolean is true. Use for validating arguments to methods.
* @param message A message
* @param condition A condition
'''
def check_argument(condition:bool,message=None)->None: 
    assert condition, message

'''
* Checks some state of the object, not dependent on the method arguments. 
* @param message Mensaje a imprimir
* @param condition A condition
'''
def check_state(condition:bool,message=None):
    assert condition,message
       
'''
Checks that the value is not null. 
Returns the value directly, so you can use check_not_null(value) inline.
T El tipo del elemento    
reference Parametro a comprobar
El parametro a comprobar
'''
   
def check_not_null(reference:E):
    assert reference is not None, f"Es nulo {reference}"
        
'''
* Checks that index_bool is a valid element index_bool into a list, string, or array with the specified size. 
* An element index_bool may range from 0 inclusive to size exclusive. 
* You don't pass the list, string, or array directly; you just pass its size. 
* @param index_bool Un indice 
* @param size El tamanyo de la lista
* @return Index El indice del elemento
'''
   
def check_element_index(index:int,size:int):
    assert (index>=0 and index<size), f"Index = {index}, size= {size}"
    return index
    
'''
* Checks that index_bool is a valid position index_bool into a list, string, or array with the specified size. 
* A position index_bool may range from 0 inclusive to size inclusive. 
* You don't pass the list, string, or array directly; you just pass its size. Returns index_bool.
* @param index_bool El indice del elemento
* @param size El tamanyo de la lista
* @return Index El indice del elemento
'''
def check_position_index(index:int,size:int):
    assert (index>=0 and index<=size), f"Index = {index}, size= {size}"
    return index
    

if __name__ == '__main__':
    print("Index = {0:d}, size {1:d}".format(5,4))
    check_position_index(7,4)   
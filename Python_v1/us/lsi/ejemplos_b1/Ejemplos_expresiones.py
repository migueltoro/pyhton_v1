'''
Created on 17 sept 2022

@author: migueltoro
'''

import math

if __name__ == '__main__':
    print(3 + 9 > 9 and 8 > 3)
    resultado = 5 + math.sqrt(10 * 10) < 20 - 2  
    print(resultado)
    nombre = "Juan"
    print(13,2 * 5) # type: ignore
    print((nombre[0] + nombre[1]) / 2) # type: ignore
    print("Ajo" * 3.1) # type: ignore
    print(abs("-1.2")) # type: ignore

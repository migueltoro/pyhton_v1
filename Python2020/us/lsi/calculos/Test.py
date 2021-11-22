'''
Created on 11 nov 2021

@author: migueltoro
'''
import random
from us.lsi.tools.File import lineas_de_fichero
numeros = [random.randint(1, 100) for _ in range(10)]
    
if __name__ == '__main__':
    i = 0
    for n in numeros:
        print(i, n, sep=': ') 
        i = i+1

    texto = "Muestrame con puntos"
    for c in texto:
        print(c,end='.') 
    
    with open('../../../resources/datos_2.txt', encoding='utf-8') as f:
        contenido = f.read()
    
    print(contenido)  # Mostramos el contenido del fichero
    
    with open('../../../resources/datos_2.txt', encoding='utf-8') as f:
        for linea in f:
            print(linea,end='')
    
    print(f)
            
    ls = lineas_de_fichero('../../../resources/datos_2.txt')
    print(ls)



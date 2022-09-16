'''
Created on 16 sept 2022

@author: migueltoro
'''
import re



if __name__ == '__main__':
    print(re.split('[ ,]','En un lugar de la Mancha, de cuyo nombre no quiero acordarme'))
    a:int = 2
    b:float = 4.567
    i: int = 5
    print('El resultado de {0} multiplicado por {1:.1f} es {2}'.format(a, b, a*b))
    print(f'El resultado de {a} multiplicado por {b:.1f} es {a*b}'.format(a, b, a*b))
    print('{0} {1:2d} {2:3d}'.format(i, i*i, i*i*i))
    print(f'{i} {i*i:2d} {i*i*i:3d}')
    print(f'{i:03d} {i*i:03d} {i*i*i:03d}')
    print('Si x es igual a {x:d} e y es igual a {y:.2f}, entonces la inecuacion {t:s} es {inecuacion}' \
         .format(x=a, y=b, t = 'x < (y * 2)', inecuacion = a<(b*2)))
    nombre: str = 'Juan'
    telefono: int = 678900123
    altura: float = 182.3
    print(f'{nombre*2:10s} ==> {telefono:10d}  => {altura:.2f}')
    print('  Juan  '.strip())
    print('juan'.capitalize())
    print('juan'.upper())



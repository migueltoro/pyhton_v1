'''
Created on 17 sept 2022

@author: migueltoro
'''

from us.lsi.tools.File import lineas_de_fichero, absolute_path
from typing import Iterator


def mcd(a:int, b:int)->int:
#    check_argument(a>=0 and b>0,f'El coeficiente a debe ser mayor o igual que cero y b mayor que cero y son: a = {a}, b = {b}')
    assert a>=0 and b>0,f'El coeficiente a debe ser mayor o igual que cero y b mayor que cero y son: a = {a}, b = {b}'
    while b > 0:
        a, b = b, a%b
    return a

def saludo()->None:
    print("Hola")
    bienestar:int = int(input())

    while bienestar < 1 or bienestar > 5:
        print("Por favor, introduce un valor del 1 al 5:")
        bienestar = int(input())

    if bienestar < 3: # 1 o 2
        print("Veras como el dia mejora.")
    elif bienestar < 5: # 3 o 4
        print("No esta mal, hoy sera un gran dia")
    else: # 5
        print("Me alegro de que te sientas bien")
    
def test2():
    a = 5
    b = 1
    try:
        r:float = a/b
    except ArithmeticError:
        print(f'Se ha producido una division por cero de {a} entre {b}')
    else:
        print(f"el resultado es {r}")
    finally:
        print("ejecutando clausula final")
              
def test3():
    try:
        ap:str=absolute_path('/resources/quijote.txt')
        lns:list[str] = lineas_de_fichero(ap,encoding='utf-16')
        print(len(lns))
    except AssertionError:
        print(f'No se encuentra el fichero {ap}')

def test4():
    x = 4
    if x > 5:
        raise Exception(f'x no deberia superar 5. Su valor fue: {x}')
    
def test5():
    ''' Equivalencia entre for y while '''
   
    print('________________________')  
    s1:int=0
    for e in range(10,30,5):
        s1 = s1 + e
        print(s1)
    print('________________________')    
    s2:int=0
    i:int = 10
    while i < 30:
            s2 = s2 + i
            i = i + 5
            print(s2)
    
def test6():
    ''' Equivalencia entre for y while '''
   
    print('________________________')  
    s1:int=0
    for e in range(10,30,5):
        s1 = s1 + e
        print(s1)
    print('________________________')    
    s2:int=0
    it:Iterator[int] = iter(range(10,30,5))
    r2:bool = True
    while r2:
        try:
            e2:int = next(it)
            s2 = s2 + e2
            print(s2)
        except StopIteration:
            r2 = False
                 
    
if __name__ == '__main__':
    test5()
    
   
        
    


    
        

'''
Created on 17 sept 2022

@author: migueltoro
'''
from math import sqrt
from us.lsi.tools.Preconditions import check_argument
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from typing import Iterator

def media(ls:list[int]) -> float:
    a = (0,0)
    for e in ls:
        a = (a[0]+e,a[1]+1)
    check_argument(a[1]>0,'La lista esta vacia')
#    assert a[1]>0, 'La lista esta vacia'
    return a[0]/a[1]

def desviacion_tipica(ls:list[int]) -> float:
    a = (0.,0.,0)  #(sum x^2, sum x, num elem)
    for e in ls:
        a = (a[0]+e*e,a[1]+e,a[2]+1)
#    check_argument(a[2]>0,'La lista esta vacia')
    assert a[2]>0,'La lista esta vacia'
    return sqrt(a[0]/a[2]-(a[1]/a[2])**2) 

def suma_aritmetica(a:int,b:int,c:int)->int:
    s = 0
    for e in range(a,b,c):
        s = s + e
    return s

def suma_primeros(m:int,n:int)->int:
    i = 0;
    a = 0
    for e in range(m):
        if i < n:
            a = a + e
        else:
            break
        i = i +1
    return a

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

def test1():
    a,b,c = 2,500,7
    print(f"La suma de la progresion aritmetica de {a} a {b} con razon {c} es {suma_aritmetica(a,b,c)}")
    m,n=10000000, 10
    print(f'Suma de los primeros {n} numeros de la secuencia 0 a {m} es {suma_primeros(m, n)}')
    print(mcd(1204,56))
    
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
    
   
        
    


    
        

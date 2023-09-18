'''
Created on 10 nov 2021

@author: migueltoro
'''

from us.lsi.tools.File import lineas_de_csv 
from typing import Iterable, TypeVar, Callable
from us.lsi.tools.Iterable import flat_map, distinct, count_if, first_index_if
from functools import reduce
from fractions import Fraction

E = TypeVar('E')
R = TypeVar('R')

identity = lambda x:x

def ej1(a:int,b:int,c:int,d:int)->Iterable[int]:
    it1 = map(lambda x:x**2,range(a,b,c))
    it2 = filter(lambda x:x%d==0, it1)
    return it2

def ej2(fichero:str)->Iterable[int]:
    it1 = lineas_de_csv(fichero)
    it2: Iterable[str] = flat_map(it1,lambda x:x)
    it3 = map(lambda e:int(e),it2)
    it4 = distinct(it3)
    return it4

def ej3(cadena:str):
    it1 = enumerate(cadena)
    it2 = filter(lambda e:e[0]%2==0,it1)
    it3 = map(lambda e: e[1],it2)
    return it3

def tolist(iterable:Iterable[E])->list[E]:
    ls= []
    for e in iterable:
        ls.append(e)
    return ls

def toset(iterable:Iterable[E])->set[E]:
    st : set[E]= set()
    for e in iterable:
        st.add(e)
    return st

def tomap(iterable:Iterable[E],t1=identity,t2=ord)->dict[E,E]:
    dt = {}
    for e in iterable:
        dt[t1(e)] = t2(e)
    return dt
    

if __name__ == '__main__':
    texto:str = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
    print("Apariciones de la letra a:", count_if(texto,lambda e:e=="a"))
    print("Primera aparicion de la letra a:", first_index_if(texto,lambda e:e=="a"))
    f: Callable[[set[E],E],set[E]] = lambda s,e: s | {e}
    es:set[str] = set()
    print(reduce(f, texto, es))
    print(reduce(lambda x,y:x|{y},texto,es))
    print(reduce(lambda x,y:x+y,range(0,30)))
    print(count_if(distinct(texto)))
    e = 2
    r = e*e if e%2==0 else e*e*e
    print(r)
    print(tolist("En un lugar de la Mancha de cuyo nombre no quiero acordarme"))
    print(toset("En un lugar de la Mancha de cuyo nombre no quiero acordarme"))
    print({e:ord(e) for e in "En un lugar de la Mancha de cuyo nombre no quiero acordarme"})
    print(tomap("En un lugar de la Mancha de cuyo nombre no quiero acordarme"))
    nombres = ["Miguel", "Ana", "Jose Maraa", "Guillermo", "Maria", "Luisa"]
    ranking = {nombre: nombres.index(nombre) for nombre in nombres}
    print(ranking)
    texto = "este es un pequenyo texto para probar la siguiente definicion por comprension"
    iniciales = {p[0] for p in texto.split()}
    palabras = {p for p in texto.split()}
    palabras_por_iniciales = {c: [p for p in palabras if p[0]==c] for c in iniciales}
    print(palabras_por_iniciales)
    ls = [1,2,3,4,5,6]
    s = [e+x for e,x in zip(ls,range(10,3000,7))]
    print(s)
    
    s = []
    it1 = iter(ls)
    it2 = iter(range(10,3000,7))
    try:
        while True:
            e = next(it1)
            x = next(it2) 
            s.append(e+x)               
    except StopIteration:
        pass

    print(s)

    s = []
    ls2 = list(range(10,3000,7))
    for i in range(min(len(ls),len(ls2))):
        s.append(ls[i]+ls2[i])
    print(s)
  
    print (Fraction(11, 35))
    # returns Fraction(11, 35)
  
    print (Fraction(10, 18))
    # returns Fraction(5, 9)
 
    print (Fraction())
    # returns Fraction(0, 1)
    
        

'''
Created on 18 sept 2022

@author: migueltoro
'''

s:list[int] = [x**2 for x in range(3, 70) if x % 3 == 0]

nombres:list[str] = ["Miguel", "Ana", "Jose Maria", "Guillermo", "Maria", "Luisa"]
ranking:dict[str,int] = {nombre: nombres.index(nombre) for nombre in nombres}

texto = "este es un pequenyo texto para probar la siguiente definicion por comprension"
iniciales = {p[0] for p in texto.split()}
palabras = {p for p in texto.split()}
palabras_por_iniciales = {c: [p for p in palabras if p[0]==c] for c in iniciales}

if __name__ == '__main__':
    print(s)
    print(ranking)
    print(palabras_por_iniciales)
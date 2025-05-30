'''
Created on 29 ago 2024

@author: migueltoro
'''

import random
import string
from us.lsi.tools.File import absolute_path


def generate_random_city(nombre:str)->str:
    # Genera un nombre de ciudad aleatorio de longitud 5
    # Genera un número aleatorio de habitantes entre 1000 y 1000000
    habitantes = random.randint(1000, 1000000)
    return f'{nombre},{habitantes}'

def generate_cities_file(num_cities:int, file_path:str)->set[str]:
    st:set[str] = set()
    with open(absolute_path(file_path), 'w') as f:
        for _ in range(num_cities):
            nombre = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
            if  nombre not in st:
                city = generate_random_city(nombre)
                f.write(city + '\n')
                st.add(nombre)
    return st

def generate_random_road(source:str, target:str,i:int)->str: 
    nombre = 'c' + str(i)
    km = random.randint(1, 500)
    s = f'{source},{target},{nombre},{km}'
    return s

def generate_roads_file(num_roads:int, ciudades:list[str], file_path:str):
    st:set[tuple[str,str]] = set()
    with open(absolute_path(file_path), 'w') as f:
        for i in range(num_roads):   
            source = random.choice(ciudades)
            target = random.choice(ciudades)
            # Genera un nombre de carretera y una longitud aleatorios
            if (source,target) not in st and (target,source) not in st:
                st.add((source,target))
                road = generate_random_road(source, target,i)
                print(road)
                f.write(road + '\n')

if __name__ == '__main__':
    # Genera un fichero con 100 ciudades
    ciudades = generate_cities_file(100, 'ficheros/ciudades_2.txt')
    # Genera un archivo con 200 carreteras
    generate_roads_file(200, list(ciudades), 'ficheros/carreteras_2.txt')
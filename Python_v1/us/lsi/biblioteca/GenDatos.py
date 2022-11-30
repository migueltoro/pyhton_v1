'''
Created on 17 nov 2022

@author: migueltoro
'''

import random
from us.lsi.biblioteca.Libro import Libro
from us.lsi.biblioteca.Ejemplar import Ejemplar
from us.lsi.biblioteca.Prestamo import Tipo_prestamo
from us.lsi.types.Persona import Persona
from us.lsi.biblioteca.Usuario import Usuario
from us.lsi.tools.File import write_iterable, iterable_de_fichero, absolute_path
from us.lsi.tools.Iterable import flat_map
from datetime import datetime, timedelta
from typing import Iterable
from itertools import cycle

from faker import Faker
Faker.seed(0)
fake = Faker('es_ES')
import re

def persona_random(a:int,b:int)->Persona:
    apellidos:str = fake.last_name()+" "+fake.last_name()
    nombre:str = fake.first_name()
    dni: str = fake.nif()
    fdate:str = fake.date_of_birth(minimum_age=a,maximum_age=b)
    fhora:str = fake.time(pattern = '%H:%M')
    fecha_nacimiento = f'{fdate} {fhora}'
    telefono: str = fake.phone_number().replace(' ','')
    direccion: str = fake.address()
    direccion = re.sub(' \n|\n',';',direccion)
    direccion = direccion.replace(', ',';')
    s = f'{apellidos},{nombre},{dni},{fecha_nacimiento},{telefono},{direccion}'
    return Persona.of_file(s)

def usuario_random(a:int,b:int)->str:
    p:Persona = persona_random(a,b)
    f:datetime = fake.date_between(start_date=p.fecha_de_nacimiento+timedelta(days=6570),
                                   end_date=datetime.now())
    return f"{p.apellidos},{p.nombre},{p.dni},{p.fecha_de_nacimiento.strftime('%Y-%m-%d %H:%M')},{p.telefono},{p.direccion},{f}"

def usuarios_random(n:int,a:int,b:int,file:str)->None:
    r:Iterable[str] = (usuario_random(a,b) for _ in range(n) )
    write_iterable(file,r)        
   
def libro_random() -> str:
    return f'{fake.isbn13()},{fake.sentence()},{fake.name()},{random.randrange(1000)},{random.uniform(5.0,30.0):.2f},\
{fake.date_between(start_date=datetime(2000,1,1),end_date=datetime.now())},{random.randrange(10000)}'

def libros_random(n:int,file:str)->None:
    r:Iterable[str] = (libro_random() for _ in range(n) )
    write_iterable(file,r)  
         
def ejemplar_random(libro:Libro, codigo:int) -> str:
    fecha=fake.date_between(start_date=libro.fecha_publicacion,end_date=datetime.now())
    return f'{libro.isbn},{codigo},{fecha}'

def ejemplares_random(k:int,file_libros:str,file:str):
    libros: Iterable[Libro] = (Libro.parse(x) for x in iterable_de_fichero(file_libros))
    f = lambda lb: (ejemplar_random(lb,cd) for cd in range(k))
    r:Iterable[str] = flat_map(libros,f)
    write_iterable(file,r)
   
def prestamo_random(ejemplar:Ejemplar,usuario:Usuario)->str:
    fecha = fake.date_between(start_date=ejemplar.fecha_adquisicion,end_date=datetime.now())
    tipo:str=random.choice(list(Tipo_prestamo)).name
    return f'{ejemplar.isbn},{ejemplar.codigo},{usuario.dni},{fecha},{tipo}'
    
def prestamos_random(file_ejemplares:str,file_usuarios:str,file:str):
    ejemplares: Iterable[Ejemplar] = (Ejemplar.parse(x) for x in iterable_de_fichero(file_ejemplares) 
                                      if random.uniform(0.,1.) > 0.6)
    usuarios: Iterable[Usuario] = (Usuario.parse_usuario(x) for x in iterable_de_fichero(file_usuarios)
                                    if random.uniform(0.,1.) > 0.6)
    r:Iterable[str] = (prestamo_random(e,u) for e,u in zip(ejemplares,cycle(usuarios)))
    write_iterable(file,r)

if __name__ == '__main__':
#    usuarios_random(100,20,40,absolute_path('/biblioteca/usuarios.txt'))
#    libros_random(200,absolute_path('/biblioteca/libros.txt'))
#    ejemplares_random(3,absolute_path('/biblioteca/libros.txt'),absolute_path('/biblioteca/ejemplares.txt'))
    prestamos_random(absolute_path('/biblioteca/ejemplares.txt'),absolute_path('/biblioteca/usuarios.txt'),
                     absolute_path('/biblioteca/prestamos.txt'))
    
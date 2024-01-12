'''
Created on 13 ago 2023

@author: migueltoro
'''

import random
from datetime import datetime, timedelta
from us.lsi.bancos.gen_data.gen_data_direccion import generate_direccion
from us.lsi.tools.File import absolute_path

# Función para generar letra verificadora de DNI
def calculate_dni_letter(dni_number):
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letters[dni_number % 23]

# Función para generar un dni válido con letra
# Función para generar DNI aleatorio con letra
def generate_dni(used_dnis:set[str])->str:
    while True:
        dni_number = random.randint(10000000, 99999999)
        dni_letter = calculate_dni_letter(dni_number)
        dni = f"{dni_number}{dni_letter}"
        if dni not in used_dnis:
            used_dnis.add(dni)
            break
    return dni

# Función para generar una fecha de nacimiento aleatoria en el pasado
def generate_fecha_de_nacimiento():
    horas = random.randint(0, 23)
    minutos = random.randint(0, 59)
    segundos = random.randint(0, 59)
    ten_years_ago = datetime.now() - timedelta(days=random.randint(3650, 36500)) \
        - timedelta(hours=horas, minutes=minutos, seconds=segundos)
    return ten_years_ago

# Función para generar un número de teléfono con prefijo internacional
def generate_telefono():
    prefijo = random.choice(["+34"])  # Prefijo internacional de España
    numero = random.randint(600000000, 699999999)
    return f"{prefijo}{numero}"

def genera_nombre():
    nombres = [
        "Antonio", "María", "Manuel", "Laura", "David", "Carmen", "José", "Ana", "Francisco", "Isabel",
        "Juan", "Sara", "Pedro", "Elena", "Miguel", "Raquel", "Ángel", "Nuria", "Javier", "Luisa",
        "Carlos", "Marta", "Jorge", "Silvia", "Diego", "Natalia", "José Antonio", "Lucía", "Rafael", "Marina",
        "Daniel", "Andrea", "Fernando", "Patricia", "Pablo", "Paula", "Alejandro", "Beatriz", "Ricardo", "Alicia"
    ]
    
    return random.choice(nombres)

def genera_apellidos():
    apellidos = [
        "García", "Rodríguez", "Martínez", "Fernández", "López", "Pérez", "González", "Hernández", "Díaz", "Moreno",
        "Álvarez", "Romero", "Muñoz", "Jiménez", "Ruiz", "Cabrera", "Torres", "Vargas", "Serrano", "Ortega",
        "Morales", "Rojas", "Cortés", "Navarro", "Núñez", "Delgado", "Castro", "Sánchez", "Gómez", "Molina"
        # Agrega más apellidos según sea necesario
    ]
    
    return f"{random.choice(apellidos)} {random.choice(apellidos)}"

# Generar archivo con 200 personas
def generate_personas(file_name:str,n:int)->set[str]:
    f:str = absolute_path(file_name)
    used_dnis:set[str] = set()
    with open(f, "w", encoding="utf-8") as file:
        for _ in range(n):
            apellidos = genera_apellidos()
            nombre = genera_nombre()
            dni = generate_dni(used_dnis)
            fecha_de_nacimiento = generate_fecha_de_nacimiento()
            telefono = generate_telefono()
            direccion = generate_direccion()
        
            # Escribir la línea en el archivo
            line = f"{apellidos},{nombre},{dni},{fecha_de_nacimiento.strftime('%Y-%m-%d %H:%M:%S')},{telefono},{direccion.calle};{direccion.ciudad};{direccion.zip_code}\n"
            file.write(line)
    return used_dnis

if __name__ == '__main__':
    generate_personas('/bancos/personas.txt',200)
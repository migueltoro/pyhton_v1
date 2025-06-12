'''
Created on 12 ago 2023

@author: migueltoro
'''

from us.lsi.tools.File import absolute_path
import random
from datetime import datetime, timedelta
from us.lsi.bancos.gen_data.gen_data_persona import generate_personas
from us.lsi.bancos.gen_data.gen_data_empleados import generate_empleados
from us.lsi.bancos.gen_data.gen_data_prestamos import generate_prestamos

# Función para generar IBAN aleatorio
def generate_iban(used_ibans:set[str])->str:
    
    while True:
        iban = "ES"  # Código de país para España
        for _ in range(2):
            iban += str(random.randint(0, 9))
        for _ in range(20):
            iban += str(random.randint(0, 9))
                
        if iban not in used_ibans:
            used_ibans.add(iban)
            break
    
    return iban

# Función para generar DNI aleatorio con letra
def generate_dni(used_dnis:list[str])->str:
    return random.choice(used_dnis)

# Generar archivo con 200 cuentas
def generate_cuentas(file_name:str,n:int,limit:int,used_dnis:list[str]):
    f:str = absolute_path(file_name)
    used_ibans:set[str] = set()
    with open(f, "w", encoding="utf-8") as file:
        for _ in range(n):
            iban = generate_iban(used_ibans)
            dni = generate_dni(used_dnis)
            # Generar horas, minutos y segundos aleatorios
            horas = random.randint(0, 23)
            minutos = random.randint(0, 59)
            segundos = random.randint(0, 59)
            fecha_de_creacion = datetime.now() - timedelta(days=random.randint(1, 3650)) \
                - timedelta(hours=horas, minutes=minutos, seconds=segundos)
            
            saldo = round(random.uniform(0, limit), 2)  # Saldo positivo o cero
        
            # Escribir la línea en el archivo
            line = f"{iban},{dni},{fecha_de_creacion.strftime('%Y-%m-%d %H:%M:%S')},{saldo:.2f}\n"
            file.write(line)

if __name__ == '__main__':
    dnis:list[str]= [d for d in generate_personas('/bancos/personas.txt',200)]
    generate_cuentas('/bancos/cuentas.txt',200,1000000,dnis)
    dnis_empleados:list[str]=generate_empleados('/bancos/empleados.txt',30,6000, dnis)
    assert set(dnis_empleados) <= set(dnis),f'El dni de los empleados debe estar incuido en el de las personas'
    generate_prestamos('/bancos/prestamos.txt',100,100000,dnis,dnis_empleados)
    
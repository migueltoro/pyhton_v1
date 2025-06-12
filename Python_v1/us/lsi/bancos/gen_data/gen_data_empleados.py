'''
Created on 13 nov 2023

@author: migueltoro
'''

from us.lsi.tools.File import absolute_path
import random
from datetime import datetime, timedelta

# Generar archivo con n empleados
def generate_empleados(file_name:str,n:int,limit:float,used_dnis:list[str])->list[str]:
    f:str = absolute_path(file_name)
    dnis_empleados:set[str] = set()
    with open(f, "w", encoding="utf-8") as file:
        for _ in range(n):
            dni = random.choice(used_dnis)
            dnis_empleados.add(dni)
            assert dnis_empleados <= set(used_dnis),f'El dni de los empleados debe estar incuido en el de las personas'
            fecha_de_contratato = datetime.now() - timedelta(days=random.randint(1, 3650))
            
            salario_mensual = round(random.uniform(0, limit), 2)  # Saldo positivo o cero
        
            # Escribir la línea en el archivo
            line = f"{dni},{fecha_de_contratato.strftime('%Y-%m-%d %H:%M:%S')},{salario_mensual:.2f}\n"
            file.write(line)
    return list(dnis_empleados)

if __name__ == '__main__':
    pass
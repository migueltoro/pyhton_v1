'''
Created on 13 nov 2023

@author: migueltoro
'''

from us.lsi.tools.File import absolute_path
import random
from datetime import datetime, timedelta

# Generar archivo con n empleados
def generate_prestamos(file_name:str,n:int,limit:float,dnis_usuarios:list[str],dnis_empleados:list[str]):
    f:str = absolute_path(file_name)
    nid:int=0
    with open(f, "w", encoding="utf-8") as file:
        for _ in range(n):
            dni_usuario = random.choice(dnis_usuarios)
            dni_empleado = random.choice(dnis_empleados)
            fecha_de_comienzo = datetime.now() - timedelta(days=random.randint(1, 3650))
            duracion:int = random.randint(10,60)
            cantidad:float = round(random.uniform(0, limit), 2)  # Cantidad a prestar
            interes:float = round(random.uniform(0, 10), 2)  # Interés en tanto por ciento
        
            # Escribir la línea en el archivo
            line = \
            f"{nid},{dni_usuario},{dni_empleado},{fecha_de_comienzo.strftime('%Y-%m-%d %H:%M:%S')},{duracion:d},{cantidad:.2f},{interes:.2f}\n"
            file.write(line)
            nid = nid+1
            

if __name__ == '__main__':
    pass
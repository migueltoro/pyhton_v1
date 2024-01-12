'''
Created on 13 ago 2023

@author: migueltoro
'''

import random

class Direccion:
    
    def __init__(self, calle, ciudad, zip_code):
        self.calle = calle
        self.ciudad = ciudad
        self.zip_code = zip_code

# Función para generar un código postal aleatorio en España
def generate_zip_code():
    zip_codes = [
        "08001", "28001", "41001", "46001", "29001", "48001", "50001", "30001", "03001", "18001"
    ]
    return random.choice(zip_codes)

# Función para generar una ciudad aleatoria
def generate_ciudad():
    ciudades = [
        "Madrid", "Barcelona", "Valencia", "Sevilla", "Málaga", "Bilbao", "Zaragoza", "Murcia", "Alicante", "Granada"
    ]
    return random.choice(ciudades)

def generar_nombre_calle():
    nombres_calles = [
        "Gran Vía", "Calle Mayor", "Paseo de la Castellana", "Avenida Diagonal", "Rambla de Catalunya",
        "Calle Serrano", "Calle Alcalá", "Calle Princesa", "Paseo del Prado", "Calle del Carmen",
        "Calle Preciados", "Calle Portaferrissa", "Calle Velázquez", "Calle Goya", "Calle Tetuán",
        "Calle San Bernardo", "Calle La Paz", "Calle Sagasta", "Calle Duque de Alba", "Calle Huertas",
        "Calle Atocha", "Calle Hortaleza", "Calle Chueca", "Calle Montera", "Calle Fuencarral",
        "Calle Argumosa", "Calle Almirante", "Calle Bailén", "Calle Plaza Mayor", "Calle Ortega y Gasset",
        "Calle Castelló", "Calle Ponzano", "Calle Doctor Esquerdo", "Calle Pelayo", "Calle Larios",
        "Calle Navas", "Calle Lope de Vega", "Calle del Mar", "Calle San Juan", "Calle Sevilla"
        # Agrega más nombres de calles según sea necesario
    ]
    
    return random.choice(nombres_calles)

def generate_direccion():
    calle = generar_nombre_calle()
    ciudad = generate_ciudad()
    zip_code = generate_zip_code()
    return Direccion(calle, ciudad, zip_code)


if __name__ == '__main__':
    pass
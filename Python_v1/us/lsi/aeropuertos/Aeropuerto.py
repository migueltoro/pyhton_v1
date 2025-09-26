'''
Created on 19 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Aeropuerto:
    codigo: str
    ciudad: str
    pais:str
    nombre:str
    
    @staticmethod 
    def parse(text: str)-> Aeropuerto:
        campos: list[str] = text.split(",")
        codigo: str = campos[2];
        ciudad: str = campos[3];
        pais: str = campos[1];
        nombre: str = campos[0];
        return Aeropuerto.of(codigo,ciudad,pais,nombre);
    
    @staticmethod 
    def of(codigo: str, ciudad: str, pais:str, nombre:str) -> Aeropuerto:
        return Aeropuerto(codigo,ciudad,pais,nombre)
    
    def __str__(self)->str:
        return f'({self.codigo},{self.ciudad},{self.pais},{self.nombre})'

if __name__ == '__main__':
    print(Aeropuerto.parse('Tirana Airport,Albania,TIA,Tirana'))
    print(Aeropuerto.parse('Berl�n Brandeburgo�Airport,Alemania,BER,Berlin'))
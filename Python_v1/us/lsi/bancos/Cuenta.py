'''
Created on 13 nov 2023

@author: migueltoro
'''

from __future__ import annotations
from datetime import datetime


class Cuenta:
    
    def __init__(self,iban: str,dni:str,fecha_de_creacion:datetime,saldo:float):
        self.__iban: str = iban
        self.__dni:str = dni
        self.__fecha_de_creacion:datetime=fecha_de_creacion
        self.__saldo:float=saldo
    
    @staticmethod    
    def of(iban: str,dni:str,fecha_de_creacion:datetime,saldo:float)->Cuenta:
        return Cuenta(iban,dni,fecha_de_creacion,saldo)
    
    @staticmethod    
    def parse(text:str)->Cuenta:
        iban,dni,fecha_de_creacion,saldo = text.split(',')
        fecha_de_creacion_p:datetime = datetime.strptime(fecha_de_creacion,'%Y-%m-%d %H:%M:%S')
        saldo_p: float= float(saldo)
        return Cuenta.of(iban,dni,fecha_de_creacion_p,saldo_p)
    
    @property    
    def iban(self)->str:
        return self.__iban
    
    @property
    def dni(self)->str:
        return self.__dni
    
    @property
    def saldo(self)->float:
        return self.__saldo
    
    @property
    def fecha_de_creacion(self)->datetime:
        return self.__fecha_de_creacion
    
    def ingresar(self,c:float)->None:
        self.__saldo += c
        
    def retirar(self,c:float)->None:
        self.__saldo -= c
        
    def __eq__(self, other)->bool:
        if isinstance(other, Cuenta):
            return self.iban == other.iban
        return False
    
    def __hash__(self)->int:
        return  hash(self.__iban)
        
    def __str__(self):
        return f'{self.iban},{self.saldo}'
     
if __name__ == '__main__': 
    cuenta:Cuenta = Cuenta.parse('ES1161954191929372160031,99212318R,2017-04-09 00:17:51,549928.47')
    print(cuenta)
        
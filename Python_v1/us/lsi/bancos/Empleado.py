'''
Created on 13 nov 2023

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from us.lsi.ejemplos_types.Persona import Persona
from us.lsi.bancos.Personas import Personas
from typing import Optional
from dateutil.relativedelta import relativedelta

@dataclass(frozen=True,order=True)
class Empleado:
    dni:str
    fecha_de_contrado:date
    salario_mensual:float
    
    @staticmethod    
    def of(dni:str,fecha_de_contrado:datetime,salario_mensual:float)->Empleado:
        return Empleado(dni,fecha_de_contrado,salario_mensual)
        
    @staticmethod    
    def parse_empleado(text:str)->Empleado:
        dni,fecha_de_contrado,salario_mensual = text.split(',')
        fecha_de_contrado_p:datetime=datetime.strptime(fecha_de_contrado,'%Y-%m-%d %H:%M:%S')
        salario_mensual_p=float(salario_mensual)
        return Empleado.of(dni,fecha_de_contrado_p,salario_mensual_p)
    
    @property
    def persona(self)->Persona:
        p:Optional[Persona] = Personas.of().persona_dni(self.dni)
        assert p is not None, f'El empleado {self.dni} no está dado de alta como persona'
        return p
    
    @property
    def meses_contratado(self)->int:
        now:datetime = datetime.now()
        return relativedelta(now,self.fecha_de_contrado).months
    
    def __str__(self):
        return f'{self.dni},{self.fecha_de_contrado.strftime("%d-%m-%Y")}'

if __name__ == '__main__':  
    print(Personas.of().persona_dni('26212107L')) 
    e:Empleado=Empleado.of('26212107L',datetime.strptime('2021-06-22 11:07:38','%Y-%m-%d %H:%M:%S'),float('1292.37'))  
    print(e)  
    e2:Empleado=Empleado.parse_empleado('26212107L,2021-06-22 11:07:38,1292.37')  
    print(e2.persona)         
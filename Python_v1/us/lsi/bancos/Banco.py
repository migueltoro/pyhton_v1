'''
Created on 13 nov 2023

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass, astuple, asdict
from us.lsi.tools.Preconditions import check_argument
from us.lsi.tools.File import root_project, absolute_path
from us.lsi.tools.Iterable import str_iter, grouping_reduce
from us.lsi.tools.Dict import str_dict
from us.lsi.ejemplos_types.Persona import Persona
from typing import Optional

from us.lsi.bancos.Cuenta import Cuenta
from us.lsi.bancos.Cuentas import Cuentas
from us.lsi.bancos.Empleado import Empleado
from us.lsi.bancos.Empleados import Empleados
from us.lsi.bancos.Prestamo import Prestamo
from us.lsi.bancos.Prestamos import Prestamos
from us.lsi.bancos.Personas import Personas

class Banco: 
    
    __gestor_de_banco: Optional[Banco] = None

    def __init__(self, nombre:str, codigo_postal:int, email:str, personas:Personas,empleados: Empleados, cuentas: Cuentas, prestamos: Prestamos):   
        self.__nombre: str = nombre
        self.__codigo_postal: int = codigo_postal
        self.__email: str = email
        
        self.__personas: Personas = personas
        self.__empleados: Empleados = empleados
        self.__cuentas: Cuentas = cuentas
        self.__prestamos: Prestamos = prestamos  
   
   
    @staticmethod
    def of(nombre:str='Reina Mercedes',codigo_postal:int=41012,email:str='bib@us.es',
           fp:str='bancos/personas.txt',
           fe:str='bancos/empleados.txt',
           fc:str='bancos/cuentas.txt',
           fpt:str='bancos/prestamos.txt')->Banco:
        if Banco.__gestor_de_banco is None:
            personas:Personas=Personas.of(absolute_path(fp))
            empleados:Empleados=Empleados.of(absolute_path(fe))
            cuentas:Cuentas=Cuentas.of(absolute_path(fc))
            prestamos:Prestamos=Prestamos.of(absolute_path(fpt))
            Banco.__gestor_de_banco = Banco(nombre, codigo_postal,email,personas,empleados, cuentas, prestamos)
        return Banco.__gestor_de_banco
    
    @property
    def nombre(self)->str:
        return self.__nombre
    
    @property
    def codigo_postal(self)-> int:
        return self.__codigo_postal
    
    @property
    def email(self) -> str: 
        return self.__email
        
    @property
    def personas(self)-> Personas:
        return self.__personas
        
    @property
    def empleados(self) -> Empleados:
        return self.__empleados
        
    @property
    def cuentas(self) -> Cuentas:
        return self.__cuentas
    
    @property
    def prestamos(self)-> Prestamos:
        return self.__prestamos
    
    '''
    Préstamos gestionados por un empleado
    '''
    
    def prestamos_de_empleado(self,dni:str)->set[Prestamo]:
        return {p for p in self.prestamos.todos if p.dni_empleado == dni}
    
    '''
    Préstamos de un cliente
    '''
    def prestamos_de_cliente(self,dni:str)->set[Prestamo]:
        return {p for p in self.prestamos.todos if p.dni_cliente == dni}
    
    '''
    Empleado más joven
    '''
    def empleado_mas_joven(self)->Persona:
        return max((e.persona for e in self.empleados.todos), key= lambda p: p.fecha_de_nacimiento)
    
    '''
    Número de cuentas de cada cliente
    '''
    def numero_de_cuentas_de_cliente(self)->dict[str,int]:
        return grouping_reduce(self.cuentas.todos,lambda c: c.dni,lambda x,y:x+y,lambda _:1)
    
if __name__ == '__main__':  
    banco:Banco = Banco.of()
    print(banco.empleados.empleado_dni('52184462S'))
    print(str_iter(banco.prestamos_de_cliente('52184462S'),sep='\n',prefix='',suffix=''))
    print(banco.empleado_mas_joven())
    print(str_dict(banco.numero_de_cuentas_de_cliente(),sep='\n'))
    
        
'''
Created on 17 nov 2022

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime,date
from us.lsi.ejemplos_types.Persona import Persona

@dataclass(frozen=True,order=True)
class Usuario(Persona):
    fecha_alta:date
    
    @staticmethod
    def of_persona(p:Persona,fecha_alta:date)->Usuario: 
        return Usuario(p.apellidos,p.nombre,p.dni,p.fecha_de_nacimiento,p.telefono,p.direccion,fecha_alta) 
    
    @staticmethod
    def parse(text:str)->Usuario: 
        ls:list[str] = text.split(',')
        fecha_alta:date = datetime.strptime(ls[-1].strip(),"%Y-%m-%d").date()
        p:Persona = Persona.parse_list(ls[0:-1])
        return Usuario.of_persona(p,fecha_alta)
    
    @staticmethod
    def parse_list_usuario(ls:list[str])->Usuario: 
        fecha_alta:date = datetime.strptime(ls[-1].strip(),"%Y-%m-%d")
        p:Persona = Persona.parse_list(ls[0:-1])
        return Usuario.of_persona(p,fecha_alta)

if __name__ == '__main__':
    u = Usuario.parse('Plaza Rivero,Apolinar,91447244A,1990-09-08 19:14:00,+34664759382,Callejón Virginia Collado 21;Lugo;37687,2010-05-21')
    print(u)
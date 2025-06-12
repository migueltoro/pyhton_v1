'''
Created on 19 nov 2023

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass, astuple, asdict
from us.lsi.tools.File import absolute_path
from us.lsi.tools.Iterable import str_iter, grouping_reduce
from us.lsi.tools.Dict import str_dict
from us.lsi.tools.Optional import optional_get, optional_is_empty
from datetime import date, datetime
from us.lsi.ejemplos_types.Persona import Persona
from us.lsi.biblioteca.Usuarios import Usuarios
from typing import Optional, Callable
from collections import Counter
from statistics import mean

from us.lsi.bancos.Cuenta import Cuenta
from us.lsi.bancos.Cuentas import Cuentas
from us.lsi.bancos.Empleado import Empleado
from us.lsi.bancos.Empleados import Empleados
from us.lsi.bancos.Prestamo import Prestamo
from us.lsi.bancos.Prestamos import Prestamos
from us.lsi.bancos.Personas import Personas
from us.lsi.bancos.Banco import Banco

'''
Vencimiento de los prestamos de un cliente
'''
def vencimiento_de_prestamos_de_cliente(banco:Banco,dni:str)->set[date]:
    return {p.fecha_vencimiento for p in banco.prestamos.todos if p.dni_cliente == dni}

'''
Persona con más prestamos
'''

def cliente_con_mas_prestamos(banco:Banco)->Persona:
    c:Counter[str] = Counter(p.dni_cliente for p in banco.prestamos.todos)
    dni:str = c.most_common(1)[0][0]
    p:Optional[Persona]=banco.personas.persona_dni(dni)
    assert p is not None, f'la persona con dni {dni} no existe'
    return p

'''
Cantidad total de los créditos gestionados por un empleado
'''

def cantidad_prestamos_empledado(banco:Banco,dni:str)->float:
    return sum(p.cantidad for p in banco.prestamos.todos if p.dni_empleado == dni)

'''
Empleado más longevo
'''

def empleado_mas_longevo(banco:Banco)->Persona:
    emp: Empleado = max((e for e in banco.empleados.todos), key=lambda e: e.meses_contratado)
    p:Optional[Persona] = banco.personas.persona_dni(emp.dni)
    assert p is not None, f'La persona no existe'
    return p

'''
Interés mínimo, máximo y medio de los préstamos
'''

def rango_de_intereses_de_prestamos(banco:Banco)->tuple[float,float,float]:
    int_min:float=min(p.interes for p in banco.prestamos.todos)
    int_max:float=max(p.interes for p in banco.prestamos.todos)
    int_mean:float=mean(p.interes for p in banco.prestamos.todos)
    return (int_min,int_max,int_mean)


'''
Préstamos a empleados
'''
def prestamos_a_empleados(banco:Banco)->set[Persona]:
    dnis:set[str] = {p.dni_cliente for p in banco.prestamos.todos if not optional_is_empty(Empleados.of().empleado_dni(p.dni_cliente))}
    return {optional_get(Empleados.of().empleado_dni(d)).persona for d in dnis}

'''
Número de préstamos por mes y año
'''
def num_prestamos_por_mes_año(banco:Banco)->dict[tuple[int,int],int]:
    return Counter((p.fecha_comienzo.month,p.fecha_comienzo.year) for p in banco.prestamos.todos)

if __name__ == '__main__':
    pass
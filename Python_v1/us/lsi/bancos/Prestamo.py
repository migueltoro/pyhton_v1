'''
Created on 13 nov 2023

@author: migueltoro
'''

from __future__ import annotations
from dataclasses import dataclass, astuple, asdict
from us.lsi.tools.Preconditions import check_argument
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

@dataclass(frozen=True,order=True)
class Prestamo:
    nid:int
    dni_cliente: str
    cantidad: float
    fecha_comienzo: datetime
    duracion: int
    interes:float
    dni_empleado:str
    
    @staticmethod    
    def of(nid:int,dni_cliente: str, cantidad: float, fecha_comienzo: datetime, duracion: int, 
           interes:float, dni_empleado:str)->Prestamo:
        return Prestamo(nid,dni_cliente, cantidad, fecha_comienzo, duracion, interes, dni_empleado)
    
    '''
    0,79597814N,26170537X,2023-06-30 20:34:43,51,99353.52,8.27
    '''
    @staticmethod    
    def parse(text:str)->Prestamo:
        nid,dni_cliente, dni_empleado, fecha_comienzo, duracion, cantidad,  interes  = text.split(',')
        fecha_comienzo_p:datetime = datetime.strptime(fecha_comienzo,'%Y-%m-%d %H:%M:%S')
        nid_p:int = int(nid)
        cantidad_p: float= float(cantidad)
        interes_p:float= float(interes)
        duracion_p:int=int(duracion)
        return Prestamo(nid_p,dni_cliente,cantidad_p,fecha_comienzo_p,duracion_p,interes_p, dni_empleado)
    
    @property
    def fecha_vencimiento(self)->date:
        años:int = self.duracion//12
        meses:int = self.duracion%12
        return (self.fecha_comienzo+relativedelta(years=años,months=meses)).date()
     
    def __str__(self):
        return f'{self.dni_cliente},{self.fecha_comienzo.strftime("%d-%m-%Y")},{self.cantidad}' 
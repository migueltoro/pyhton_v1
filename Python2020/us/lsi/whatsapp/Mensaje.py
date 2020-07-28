'''
Created on 26 jul. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from datetime import time,date
from us.lsi.tools.Dates import parse_time, str_time, parse_date, str_date
from us.lsi.tools.String import to_unicode
from typing import TypeVar
import re

Mensaje = TypeVar('Mensaje')

RE = r'(?P<fecha>\d\d?/\d\d?/\d\d?) (?P<hora>\d\d?:\d\d) - (?P<usuario>[^:]+): (?P<texto>.+)'

@dataclass(frozen=True,order=True)
class Mensaje:
    fecha:date 
    hora: time 
    usuario: str
    texto: str
    
    @staticmethod   
    def parse(mensaje: str) -> Mensaje:
        matches = re.match(RE,mensaje)
        if(matches):
            fecha = parse_date(matches.group('fecha'), '%d/%m/%y')
            hora = parse_time(matches.group('hora'), '%H:%M')
            usuario = matches.group('usuario')
            texto = matches.group('texto')
            return Mensaje(fecha, hora, usuario, texto)
        else:
            return None
    
    def __str__(self):
        return "%s %s - %10s:\n  %s" % (str_date(self.fecha,'%d/%m/%y'),str_time(self.hora,'%H:%M'),self.usuario,to_unicode(self.texto))

if __name__ == '__main__':
    m = Mensaje.parse('26/2/16 9:16 - Leonard: De acuerdo, ¿cuál es tu punto?')
    print(m)
'''
Created on 26 jul. 2020

@author: migueltoro
'''
from __future__ import annotations
from typing import Optional
from dataclasses import dataclass
from datetime import time,date,datetime
import re

RE = r'(?P<fecha>\d\d?/\d\d?/\d\d?) (?P<hora>\d\d?:\d\d) - (?P<usuario>[^:]+): (?P<texto>.+)'

@dataclass(frozen=True,order=True)
class Mensaje:
    fecha:date 
    hora: time 
    usuario: str
    texto: str
    
    @staticmethod   
    def parse(mensaje: str) -> Optional[Mensaje]:
        matches = re.match(RE,mensaje)
        if(matches):
            fecha = datetime.strptime(matches.group('fecha'), '%d/%m/%y').date()
            hora = datetime.strptime(matches.group('hora'), '%H:%M').time()
            usuario = matches.group('usuario')
            texto = matches.group('texto')
            return Mensaje(fecha, hora, usuario, texto)
        else:
            return None
    
    def __str__(self):
        return f"{self.fecha.strftime('%d/%m/%y')} {self.hora.strftime('%H:%M')} - {self.usuario:10}:\n  {self.texto}"
    
if __name__ == '__main__':
    m = Mensaje.parse('26/2/16 9:16 - Leonard: De acuerdo, ¿cuál es tu punto?')
    print(m)
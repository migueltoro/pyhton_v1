'''
Created on 26 jul. 2020

@author: migueltoro
'''
from __future__ import annotations
from typing import Optional
from dataclasses import dataclass
from datetime import time,date,datetime
import re
from us.lsi.tools.Dict import str_dict
from us.lsi.tools.Optional import optional_get
from collections import Counter
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from re import Match


RE = r'(?P<fecha>\d\d?/\d\d?/\d\d?) (?P<hora>\d\d?:\d\d) - (?P<usuario>[^:]+): (?P<texto>.+)'
sep = r'[ ,;.\n():¿?!¡\"]'

@dataclass(frozen=True,order=True)
class Mensaje:
    fecha:date 
    hora: time 
    usuario: str
    texto: str
    frecuencia_de_palabras: Counter[str]
    
    @staticmethod   
    def parse(mensaje: str, ph:set[str]) -> Optional[Mensaje]:
        matches: Optional[Match[str]] = re.match(RE,mensaje)
        if(matches):
            fecha = datetime.strptime(matches.group('fecha'), '%d/%m/%y').date()
            hora = datetime.strptime(matches.group('hora'), '%H:%M').time()
            usuario = matches.group('usuario')
            texto = matches.group('texto')
            palabras = (p for p in re.split(sep, texto) if len(p) > 0 and not p in ph)
            frecuencia_de_palabras = Counter(palabras)
            return Mensaje(fecha, hora, usuario, texto,frecuencia_de_palabras)
        else:
            return None
    
    def __str__(self):
        return f"{self.fecha.strftime('%d/%m/%y')} {self.hora.strftime('%H:%M')} - {self.usuario:10}:\n  {self.texto}"
    
if __name__ == '__main__':
    fph: str = absolute_path('/resources/palabras_huecas.txt')
    ph = {p for p in lineas_de_fichero(fph) if len(p) >0}
    m = Mensaje.parse('26/2/16 9:16 - Leonard: De acuerdo, ¿cuál es tu punto?',ph)
    print(m)
    print(str_dict(optional_get(m).frecuencia_de_palabras,sep='\n'))
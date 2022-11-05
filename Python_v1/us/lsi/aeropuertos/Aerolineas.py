'''
Created on 20 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.Aerolinea import Aerolinea
from us.lsi.tools.File import lineas_de_fichero, absolute_path, encoding

class Aerolineas:  
    __aerolineas: Aerolineas
    
    def __init__(self,aerolineas:list[Aerolinea])->None:
        self._aerolineas = aerolineas
        self._codigos_aerolineas = {a.codigo:a for a in aerolineas}
        
    @staticmethod
    def of()->Aerolineas:
        return Aerolineas.__aerolineas
               
    @staticmethod
    def lee_aerolineas(fichero:str)->Aerolineas:
        datos: list[Aerolinea] = [Aerolinea.parse(x) for x in lineas_de_fichero(fichero,encoding='Windows-1252')]
        Aerolineas.__aerolineas = Aerolineas(datos)
        return Aerolineas.__aerolineas

    @property
    def lista(self)->list[Aerolinea]:
        return self._aerolineas

    def aerolinea_codigo(self,codigo:str)->Aerolinea:
        return self._codigos_aerolineas[codigo]
    
    def size(self):
        return len(self._aerolineas)
    
    def aerolinea_int(self,i:int)->Aerolinea:
        return self._aerolineas[i]
    
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self._aerolineas)
        return f'Aerolineas\n\t{txt}'


if __name__ == '__main__':
    print(encoding(absolute_path("/resources/aerolineas.csv")))
    a = Aerolineas.lee_aerolineas(absolute_path("/resources/aerolineas.csv"))
    print(a)
    print(a.aerolinea_int(0))
    
'''
Created on 20 ago 2022

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.aeropuertos.Aerolinea import Aerolinea
from us.lsi.tools.File import lineas_de_fichero, absolute_path, encoding

class Aerolineas:  
    __aerolineas: Aerolineas = None
    
    def __init__(self,aerolineas: list[Aerolinea],codigos_aerolineas: dict[str,Aerolinea]=None)->Aerolineas:
        self._aerolineas = aerolineas
        self._codigos_aerolineas = codigos_aerolineas
    
    @staticmethod  
    def get()->Aerolineas:
        return Aerolineas.__aerolineas
    
    @staticmethod
    def lee_aerolineas(fichero:str)->Aerolineas:
        datos: list[Aerolinea] = [Aerolinea.parse(x) for x in lineas_de_fichero(fichero,encoding='Windows-1252')]
        Aerolineas.__aerolineas = Aerolineas(datos)
        return Aerolineas.__aerolineas
        

    def aerolinea(self,codigo:str)->Aerolinea:
        if not self._codigos_aerolineas:
            self._codigos_aerolineas = {a.codigo():a for a in self._aerolineas}
        return self._codigos_aerolineas[codigo]
    
    def size(self):
        return len(self._aeroLineas)
    
    def get_aerolinea(self,i:int)->Aerolinea:
        return self._aerolineas[i]
    
    def __str__(self):
        txt = "\n\t".join(str(a) for a in self._aerolineas)
        return f'Aerolineas\n\t{txt}'


if __name__ == '__main__':
    print(encoding(absolute_path("/resources/aerolineas.csv")))
    Aerolineas.lee_aerolineas(absolute_path("/resources/aerolineas.csv"))
    print(Aerolineas.get())
    print(Aerolineas.get().get_aerolinea(0))
    
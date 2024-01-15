'''
Created on 13 nov 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.tools.File import lineas_de_fichero, absolute_path, root_project, encoding
from us.lsi.ejemplos_types.Persona import Persona
from us.lsi.tools.Iterable import str_iter
from typing import Optional

class Personas:
    
    __gestor_de_personas:Optional[Personas] = None
    
    def __init__(self,personas:set[Persona])->None:
        self.__personas:set[Persona] = personas
        self.__persona_dni:dict[str,Persona] = {a.dni : a for a in self.__personas}
        self.__dnis:set[str] = set(self.__persona_dni.keys()) 
#        print(self.__persona_dni)
        
    @staticmethod
    def of()->Personas:
        if Personas.__gestor_de_personas is None:
            Personas.__gestor_de_personas = Personas.parse(absolute_path('/bancos/personas.txt',root_project()))   
        return Personas.__gestor_de_personas
               
    @staticmethod
    def parse(fichero:str,ft:str = "%Y-%m-%d %H:%M:%S")->Personas:
        personas:set[Persona] = {Persona.parse(ln,ft) for ln in lineas_de_fichero(fichero,encoding='utf-8')}
        Personas.__gestor_de_personas = Personas(personas)
        return Personas.__gestor_de_personas

    @property
    def todos(self)->set[Persona]:
        return self.__personas

    @property
    def dnis(self)->set[str]:
        return self.__dnis
        
    def persona_dni(self,dni:str)->Optional[Persona]:
        return self.__persona_dni.get(dni,None)
    
    @property
    def size(self):
        return len(self.__personas)
    
    def persona_index(self,index:int)->Persona:
        return [a for a in self.__personas][index]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__personas)
        return f'Personas\n\t{txt}' 
    
if __name__ == '__main__': 
    
    p:Persona = Persona.parse('González Cortés,Ricardo,97986110S,1975-05-27 02:01:29,+34693730797,Calle Alcalá;Murcia;08001', \
                              ft = "%Y-%m-%d %H:%M:%S")   
    print(p)
    print(encoding(absolute_path('/bancos/personas.txt')))
    print('_________')
    print(Personas.of())
    print(Personas.of().persona_dni('34759012D'))
    print(Personas.of().persona_dni('59853381K'))
#    print(Personas.of().persona_dni('48775639E'))
#    print(Personas.of().persona_dni('26212107L')) 
    print('_________')
#    personas:Personas = Personas.parse(absolute_path('/bancos/personas.txt')) 
#    print(str_iter(personas.todos,sep='\n',prefix='',suffix=''))
    print('_________')

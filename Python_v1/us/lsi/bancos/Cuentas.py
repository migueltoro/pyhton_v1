'''
Created on 13 nov 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.tools.File import lineas_de_fichero, absolute_path, root_project
from us.lsi.tools.Iterable import str_iter
from us.lsi.bancos.Cuenta import Cuenta
from typing import Optional

class Cuentas:
    
    __gestor_de_cuentas:Cuentas
    
    def __init__(self,cuentas:set[Cuenta])->None:
        self.__cuentas:set[Cuenta] = cuentas
        self.__cuentas_iban:dict[str,Cuenta] = {a.iban : a for a in self.__cuentas}
        
    @staticmethod
    def of()->Cuentas:
        if Cuentas.__gestor_de_cuentas is None:
            Cuentas.__gestor_de_cuentas = Cuentas.parse(absolute_path('/bancos/cuentas.txt',root_project()))   
        return Cuentas.__gestor_de_cuentas
               
    @staticmethod
    def parse(fichero:str)->Cuentas:
        cuentas:set[Cuenta] = {Cuenta.parse(ln) for ln in lineas_de_fichero(fichero,encoding='utf-8')}
        Cuentas.__gestor_de_cuentas = Cuentas(cuentas)
        return Cuentas.__gestor_de_cuentas

    @property
    def todos(self)->set[Cuenta]:
        return self.__cuentas

    def cuenta_iban(self,iban:str)->Optional[Cuenta]:
        return self.__cuentas_iban.get(iban,None)
    
    @property
    def size(self):
        return len(self.__cuentas)
    
    def Cuenta_index(self,index:int)->Cuenta:
        return [a for a in self.__cuentas][index]
    
    def __str__(self):
        txt:str = "\n\t".join(str(a) for a in self.__cuentas)
        return f'Cuentas\n\t{txt}'  
    
if __name__ == '__main__':    
    cuentas:Cuentas = Cuentas.parse(absolute_path('/bancos/cuentas.txt')) 
    print(str_iter(cuentas.todos,sep='\n',prefix='',suffix=''))
    print('______________')
    print(cuentas.cuenta_iban('ES5267093500351659831393'))
        
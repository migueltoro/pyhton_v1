'''
Created on 13 nov 2023

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from us.lsi.tools.Iterable import str_iter
from us.lsi.bancos.Cuenta import Cuenta
from typing import Optional

class Cuentas:
    
    __gestor_de_cuentas:Optional[Cuentas] = None
    
    def __init__(self,file:str)->None:
        self.__cuentas:set[Cuenta] = {Cuenta.parse(ln) for ln in lineas_de_fichero(file,encoding='utf-8')}
        self.__cuentas_iban:dict[str,Cuenta] = {a.iban : a for a in self.__cuentas}
        
    @staticmethod
    def of(file:str=absolute_path('bancos/cuentas.txt'))->Cuentas:
        if Cuentas.__gestor_de_cuentas is None:
            Cuentas.__gestor_de_cuentas = Cuentas(file) 
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
    cuentas:Cuentas = Cuentas.of() 
    print(str_iter(cuentas.todos,sep='\n',prefix='',suffix=''))
    print('______________')
    print(cuentas.cuenta_iban('ES5267093500351659831393'))
        
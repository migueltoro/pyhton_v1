'''
Created on 27 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.tools import Preconditions
from dataclasses import dataclass
from typing import TypeVar

Card= TypeVar('Card')

nombre_valores = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
symbols_palos = ['C', 'H', 'S', 'D']
nombre_palos = ["clubs","hearts","spades","diamonds"]

@dataclass(frozen=True,order=True)
class Card:
    palo:int  # [0,4)
    valor:int # [0,14)
    _ide:int = None # palo*4+valor # [0,54)
    

    
    @staticmethod
    def of_text(text):     
        p = text[len(text)-1]
        v = text[0:len(text)-1]
        palo = symbols_palos.index(p)
        valor = nombre_valores.index(v)      
        return Card.of(palo, valor)
    
    @staticmethod
    def of_id(ide):
        Preconditions.checkArgument(ide >= 0 and ide < 52, "No es posible {0:d}".format(ide))
        palo = ide % 4
        valor = ide % 13
        return Card(palo,valor)

    
    @staticmethod
    def of(palo,valor):
        Preconditions.checkArgument(valor >= 0 and valor <14 and palo >=0 and palo < 52, 
                    "No es posible valor = %d, palo = %d".format(valor,palo))
        return Card(palo,valor)

    
    def __str__(self): 
        return '{0}{1}'.format(nombre_valores[self.valor],symbols_palos[self.palo])
    
    @property
    def id(self) -> int:
        if self._id is None:
            self._id = self.palo*4+self.valor
        return self._id
    
    @property
    def name_of_file(self):
        r = None
        if(self.valor<9):
            r = "resources/images/%s_of_%s.svg" % (nombre_valores[self.valor],nombre_palos[self.palo])
        else:
            switcher = {
            9 : "resources/images/jack_of_%s.svg" % (nombre_palos[self.palo]),
            10: "resources/images/queen_of_%s.svg" % (nombre_palos[self.palo]),
            11: "resources/images/king_of_%s.svg" % (nombre_palos[self.palo]),
            12: "resources/images/ace_of_%s.svg" % (nombre_palos[self.palo])
            }
            r = switcher.get(self.valor,None)
        return r

if __name__ == '__main__':
    pass
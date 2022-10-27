'''
Created on 27 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from typing import Optional
from us.lsi.montecarlo.Card import Card
from us.lsi.tools.Iterable import groups_size, first_index_true, strfiter
from us.lsi.tools.Graphics import cartas_graphic
import random 
from functools import total_ordering

nombres_jugadas: list[str] =  ['EscaleraReal','EscaleraDeColor','Poker','Full','Color', \
                        'Escalera','Trio', \
                        'DoblePareja','Pareja','CartaMasAlta']
numero_de_cartas: int = 5 

@total_ordering
class Mano:
  
    def __init__(self, cartas: list[Card]):       
        self._cartas: list[Card]  = cartas
        self._frecuencias_de_valores: Optional[dict[int,int]] = None
        self._valores_ordenados_por_frecuencias: Optional[list[int]] = None
        self._son_5_valores_consecutivos: Optional[bool] = None
        self._frecuencias_de_palos: Optional[dict[int,int]] = None
        self._palos_ordenados_por_frecuencias: Optional[list[int]] = None
        self._jugada: Optional[int] = None
        self._fuerza: Optional[float] = None        
    
    @staticmethod
    def of(cartas):
        return Mano(cartas)
    
    @staticmethod
    def of_text(txt): 
        txt = txt[1:len(txt)-1]
        partes = txt.split(",")        
        cartas = [Card.of_text(x) for x in partes]
        return Mano.of(cartas)
    
    @staticmethod
    def random():
        cartas = []
        for _ in range(numero_de_cartas):
            n = random.randint(0,51)
            card = Card.of_id(n)
            cartas.append(card)
        return Mano(cartas)
    
    @property
    def cartas(self) -> list[Card]:
        return self._cartas
    
    @property
    def son_5_valores_consecutivos(self) -> bool:
        if not self._son_5_valores_consecutivos:  
            ls = self.valores_ordenados_por_frecuencias
            self._son_5_valores_consecutivos = False        
            if len(ls) == 5:               
                self._son_5_valores_consecutivos = all(ls[x+1]-ls[x]==1 for x in range(0,len(ls)-1))
        return self._son_5_valores_consecutivos
    
    @property
    def frecuencias_de_valores(self) -> dict[int,int]:
        if not self._frecuencias_de_valores:
            self._frecuencias_de_valores = groups_size(self._cartas,key=lambda c:c.valor)           
        return self._frecuencias_de_valores
    
    @property
    def valores_ordenados_por_frecuencias(self) -> list[int]:
        if not self._valores_ordenados_por_frecuencias:
            ls  = [e for e in self.frecuencias_de_valores.items()]
            ls.sort(key = lambda e: e[1], reverse= True)
            ls1 = [e[0] for e in ls]
            self._valores_ordenados_por_frecuencias = ls1
        return self._valores_ordenados_por_frecuencias

    @property
    def frecuencias_de_palos(self) -> dict[int,int]:
        if not self._frecuencias_de_palos:
            self._frecuencias_de_palos = groups_size(self._cartas,key=lambda c:c.palo) 
        return self._frecuencias_de_palos
    
    @property
    def palos_ordenados_por_frecuencias(self) -> list[int]:
        if not self._palos_ordenados_por_frecuencias:
            ls  = [e for e in self.frecuencias_de_palos.items()]
            ls.sort(key = lambda e: e[1], reverse= True)
            ls1 = [e[0] for e in ls]
            self._palos_ordenados_por_frecuencias = ls1
        return self._palos_ordenados_por_frecuencias
    
    @property
    def es_color(self)-> bool:
        pal0 = self.palos_ordenados_por_frecuencias[0]
        return self.frecuencias_de_palos[pal0] == 5
    
    @property
    def es_escalera(self)-> bool:
        return self.son_5_valores_consecutivos
    
    @property
    def es_poker(self)-> bool:
        val0 = self.valores_ordenados_por_frecuencias[0]
        return self.frecuencias_de_valores[val0] == 4
    
    @property
    def es_escalera_de_color(self)-> bool:
        pal0 = self.palos_ordenados_por_frecuencias[0]
        return self.son_5_valores_consecutivos and self.frecuencias_de_palos[pal0] == 5
    
    @property
    def es_full(self) -> bool:
        r = False
        if len(self.valores_ordenados_por_frecuencias) >= 2 :
            val0 = self.valores_ordenados_por_frecuencias[0]
            val1 = self.valores_ordenados_por_frecuencias[1]
            r = self.frecuencias_de_valores[val0] == 3 and self.frecuencias_de_valores[val1] == 2
        return r
    
    @property       
    def es_trio(self)-> bool:
        val0 = self.valores_ordenados_por_frecuencias[0]
        return self.frecuencias_de_valores[val0] == 3
    
    @property 
    def es_doble_pareja(self)-> bool:
        r = False
        if len(self.valores_ordenados_por_frecuencias) >= 2 :
            val0 = self.valores_ordenados_por_frecuencias[0]
            val1 = self.valores_ordenados_por_frecuencias[1]
            r = self.frecuencias_de_valores[val0] == 2 and self.frecuencias_de_valores[val1] == 2
        return r
    
    @property
    def es_pareja(self)-> bool:
        val0 = self.valores_ordenados_por_frecuencias[0]
        return self.frecuencias_de_valores[val0] == 2
    
    @property
    def es_escalera_real(self)-> bool:
        return self.es_escalera_de_color and 12 in {x.valor for x in self.cartas}
    
    @property           
    def es_carta_mas_alta(self)-> bool:
        return True
    
    @property                     
    def jugada(self) -> int:
        if not self._jugada:
            self._jugada = first_index_true(self.predicados_jugadas)
        return self._jugada
    
    @property
    def nombre_de_jugada(self) -> str:
        return nombres_jugadas[self.jugada]
    
    @property
    def predicados_jugadas(self) -> list[bool]:
        return  [self.es_escalera_real,self.es_escalera_de_color,self.es_poker,self.es_full,self.es_color, \
                 self.es_escalera,self.es_trio, \
                 self.es_doble_pareja,self.es_pareja,self.es_carta_mas_alta] 
    
    def fuerza(self, n=5000) -> float:
        if self._fuerza: 
            return self._fuerza
        gana = 0;
        pierde = 0;
        empata = 0;
        for _ in range(n):
            mr = Mano.random()
            if self < mr :
                pierde = pierde+1
            elif self > mr:
                gana = gana +1
            elif self == mr:
                empata = empata+1
        self._fuerza = gana/(gana+pierde+empata)
        return self._fuerza
    
    def __lt__(self,mano):
        r = False
        if  self.jugada > mano.jugada:
            return True
        if self.jugada == mano.jugada and \
            self.valores_ordenados_por_frecuencias[0] < mano.valores_ordenados_por_frecuencias[0]:
            return True
        return r
              
    def __eq__(self,mano):
        return self.jugada == mano.jugada and \
            self.valores_ordenados_por_frecuencias[0] == mano.valores_ordenados_por_frecuencias[0]
    
    def __ne__(self, other)->bool:
        return not (self == other)
    
                        
    def __str__(self):
        mano = strfiter((c for c in self.cartas),separator=',',prefix='[',suffix=']')
        return '{}={}={}'.format(mano,self.nombre_de_jugada,str(self.fuerza()))

    def to_graphics(self, file_out: str) -> None:
        fuerza = self.fuerza(n=5000)
        cartas_graphic(file_out,self.cartas,fuerza,self.nombre_de_jugada)
        

if __name__ == '__main__':
    m1 = Mano.random()
    m2 = Mano.of_text('[7H,8H,3C,3S,6H]')
    m3 = Mano.of_text('[10D,10H,10C,10S,5H]')
    print(m1)
    print(m2)
    print(m3)
    print(m1 < m2)
    m3.to_graphics('../../../ficheros/cartas_out.html')
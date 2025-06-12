'''
Created on 23 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.ruta.Marca import Marca
from us.lsi.ruta.Intervalo import Intervalo, Type
from us.lsi.tools.File import iterable_de_csv, absolute_path
from us.lsi.tools.Dict import str_dict
from us.lsi.tools import Graphics
from us.lsi.tools import Draw
from itertools import accumulate 
from us.lsi.tools.GraphicsMaps import  polyline, set_tipo, TipoMapa
from collections import Counter
from statistics import mean
from typing import Optional

class Ruta:
    
    def __init__(self, marcas:list[Marca])->None:
        self.__marcas = marcas
        self.__n = len(marcas)
    
    @staticmethod
    def parse(fichero: str) -> Ruta: 
        marcas = [Marca.parse(x) for x in iterable_de_csv(fichero)]
        return Ruta(marcas)
    
    @property
    def marcas(self)->list[Marca]:
        return self.__marcas
    
    @property
    def n(self)->int:
        return self.__n
    
    def __str__(self)->str:
        return '\n'.join(str(m) for m in self.marcas) 

    @property
    def tiempo(self) -> float:
        return sum(self.intervalo(i).tiempo for i in range(0,self.n-1))
   
    @property
    def longitud(self) -> float:
        return sum(self.intervalo(i).longitud for i in range(0,self.n-1))
    
    @property
    def velocidad_media(self) -> float:
        return self.longitud/self.tiempo
    
    def intervalo(self, i:int) -> Intervalo:
        assert 0 <= i < self.__n-1, f'Índice {i} fuera de rango [0,{self.__n-1}]'
        return Intervalo.of(self.marcas[i],self.marcas[i+1])
        
    @property
    def desnivel_creciente_acumulado(self) -> float:
        return sum(self.intervalo(i).longitud for i in range(0,self.n-1) if self.intervalo(i).desnivel > 0)
    
    @property
    def media_tiempo2(self) -> float:
        r:float= 0.
        n:int= 0
        for i in range(0,self.n-1):
            r += self.intervalo(i).tiempo
            n +=1
        return r/n
    
    @property
    def tiempo2(self) -> float:
        r:float= 0.
        for i in range(0,self.n-1):
            r += self.intervalo(i).tiempo
        return r
    
    @property
    def longitud2(self) -> float:
        r:float= 0.
        for i in range(0,self.n-1):
            r += self.intervalo(i).longitud
        return r
    
    @property
    def desnivel_creciente_acumulado2(self) -> float:
        r:float= 0.
        for i in range(0,self.n-1):
            if self.intervalo(i).desnivel > 0:
                r += self.intervalo(i).longitud
        return r
    
    @property
    def desnivel_decreciente_acumulado(self) -> float:
        return sum(self.intervalo(i).longitud for i in range(0,self.n-1) if self.intervalo(i).desnivel < 0)
            
    @property
    def media_desnivel_decreciente_acumulado(self) -> float:
        return mean(self.intervalo(i).longitud for i in range(0,self.n-1) if self.intervalo(i).desnivel < 0)
    
    
    @property
    def media_desnivel_decreciente_acumulado2(self) -> Optional[float]:
        r:float= 0.
        n:int = 0
        for i in range(0,self.n-1):
            if self.intervalo(i).desnivel < 0:
                r += self.intervalo(i).longitud
                n += 1
        if n ==0:
            return None
        return r/n
    
    @property
    def todos_mayores_que_cero(self) -> bool:
        return all(self.intervalo(i).longitud > 0  for i in range(0,self.n-1))
    
    @property
    def todos_mayores_que_cero2(self) -> bool: 
        r: bool = True
        for i in range(0,self.n-1):
            r = self.intervalo(i).longitud > 0
            if  not r:
                break
        return r
    
    
    def alguno_mayor_que_valor(self,a:float) -> bool:
        return any(self.intervalo(i).longitud > a  for i in range(0,self.n-1))
    
   
    def alguno_mayor_que_valor2(self,a:float) -> bool: 
        r: bool = False
        for i in range(0,self.n-1):
            r = self.intervalo(i).longitud > a
            if  r:
                break
        return r
    
    @property
    def el_mayor(self) -> Optional[Intervalo]:
        return max((self.intervalo(i)  for i in range(0,self.n-1)), key=lambda e:e.longitud)
    
    @property
    def el_mayor2(self) ->  Optional[Intervalo]: 
        r: Optional[Intervalo] = None
        for i in range(0,self.n-1):
            e:Intervalo = self.intervalo(i)
            if r is None or e.longitud > r.longitud:
                r = e          
        return r
    
    @property
    def contar_por_tipo(self)->dict[Type,int]:
        r: dict[Type,int] = {}
        for i in range(0,self.n-1):
            key: Type = self.intervalo(i).type
            if key in r.keys():
                r[key] = r[key] +1
            else:
                r[key] =  1                    
        return r
    
    @property
    def contar_por_tipo2(self)->Counter[Type]:
        return Counter(self.intervalo(i).type  for i in range(0,self.n-1))
    
    @property
    def sumar_por_tipo(self)->dict[Type,float]:
        r: dict[Type,float] = {}
        for i in range(0,self.n-1):
            key: Type = self.intervalo(i).type
            if key in r.keys():
                r[key] = r[key] + self.intervalo(i).longitud
            else:
                r[key] =  self.intervalo(i).longitud                   
        return r
    
    @property
    def agrupar_por_tipo_en_lista(self)->dict[Type,list[Intervalo]]:
        r: dict[Type,list[Intervalo]] = {}
        for i in range(0,self.n-1):
            key: Type = self.intervalo(i).type
            if key in r.keys():
                r[key] = r[key] + [self.intervalo(i)]
            else:
                r[key] =  [self.intervalo(i)]                 
        return r
    
    @property
    def agrupar_por_tipo_en_conjunto(self)->dict[Type,set[Intervalo]]:
        r: dict[Type,set[Intervalo]] = {}
        for i in range(0,self.n-1):
            key: Type = self.intervalo(i).type
            if key in r.keys():
                r[key] = r[key] | {self.intervalo(i)}
            else:
                r[key] =  {self.intervalo(i)}                 
        return r
            
    def mostrar_altitud(self)->None:
        distancias = list(accumulate((self.intervalo(i).longitud for i in range(0, self.n-1)),initial=0))
        alturas = [self.marcas[i].coordenadas.altitud for i in range(0,self.n)]     
        Draw.draw_multiline(distancias,alturas,y_label='Altura',x_label='kms',title='Recorrido de Ronda')
        
    def mostrar_altitud_google(self,fileOut):
        dd:list[float] = list(accumulate((self.intervalo(i).longitud for i in range(0, self.n-1)),initial=0))
        distancias:list[int] = [int(d) for d in dd]
        alturas:list[float] = [self.marcas[i].coordenadas.altitud for i in range(len(self.marcas))]
        campos = ["Posicion","Altura"]
        Graphics.line_chart(fileOut,"Ruta Ronda",campos,(distancias,alturas))
       
    def mostrar_mapa_google(self,fileOut:str)->None:
        set_tipo(TipoMapa.Google)
        coordenadas = [c.coordenadas.to2D for c in self.marcas]
        polyline(fileOut,coordenadas)
    
    def mostrar_mapa_bing(self,fileOut:str)->None:
        set_tipo(TipoMapa.Google)
        coordenadas = [c.coordenadas.to2D for c in self.marcas]
        polyline(fileOut,coordenadas)

if __name__ == '__main__':
    r = Ruta.parse(absolute_path("resources/ruta.csv"));
#    print(r.marcas[:30])
#    print(r)
    print("__________")
#    r.mostrar_altitud()
    r.mostrar_altitud_google("../../../ficheros/alturasGoogle.html")
#    r.mostrar_mapa_google("../../../ficheros/mapaGoogle.html")
#    r.mostrar_mapa_bing("../../../ficheros/mapaBing.html")
    print(r.el_mayor)
    print(str_dict(r.contar_por_tipo,sep='\n',suffix="\n__________"))
    print(str_dict(r.contar_por_tipo2,sep='\n',suffix="\n__________"))
    print(str_dict(r.sumar_por_tipo,sep='\n',suffix="\n__________"))
    
    
    
    
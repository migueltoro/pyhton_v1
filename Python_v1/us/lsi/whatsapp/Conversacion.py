'''
Created on 26 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Callable, Optional
from us.lsi.whatsapp.Mensaje import Mensaje
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from us.lsi.tools.Iterable import str_iter, grouping_list, groups_size,\
    grouping_set
from datetime import date
from us.lsi.tools import Graphics
from collections import Counter
from functools import reduce

P = TypeVar('P')

week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
n_week_days = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}


class Conversacion:
    
    def __init__(self, mensajes: list[Mensaje],ph:set[str]):
        self.__mensajes: list[Mensaje] = mensajes
        self.__palabras_huecas = ph
        self.__usuarios: Optional[set[str]] = None
        self.__mensajes_por_usuario: Optional[dict[str,list[Mensaje]]] = None
        self.__numero_de_mensajes_por_usuario: Optional[Counter[str]] = None
        self.__frecuencia_de_palabras: Optional[Counter[str]] =  None
        self.__numero_de_palabras: Optional[int] = None
        self.__frecuencia_de_palabras_por_usuario: Optional[Counter[tuple[str,str]]] = None
        self.__numero_de_palabras_por_usuario: Optional[Counter[str]] = None
        self.__palabras_de_usuario: Optional[dict[str,set[str]]]  = None
        self.__frecuencia_de_palabras_por_resto_de_usuarios: Optional[Counter[tuple[str,str]]] = None
        self.__numero_de_palabras_por_resto_de_usuarios: Optional[Counter[str]] = None
        
    @staticmethod   
    def of_file(file: str) -> Conversacion:
        fph: str = absolute_path('/resources/palabras_huecas.txt')
        ph = {p for p in lineas_de_fichero(fph) if len(p) >0}
        ms = (Mensaje.parse(m,ph) for m in lineas_de_fichero(file))
        mensajes = [m for m in ms if m is not None]
        return Conversacion(mensajes,ph)
    
    def __str__(self) -> str:
        it1 = str_iter(self.palabras_huecas)
        it2 = str_iter(self.mensajes,sep='\n',prefix='',suffix='')
        return 'Palabras huecas = \n{0:s}\nMensajes = \n{1:s}'.format(it1, it2) 
    
    @property
    def mensajes(self)->list[Mensaje]:
        return self.__mensajes
    
    @property
    def palabras_huecas(self)->set[str]:
        return self.__palabras_huecas
    
    def __mensajes_por_propiedad(self, key: Callable[[Mensaje],P]) -> dict[P,list[Mensaje]]:
        return grouping_list(self.mensajes,key=key)
           
    def __numero_de_mensajes_por_propiedad(self, key: Callable[[Mensaje],P]) -> Counter[P]:
        return Counter(groups_size(self.mensajes,key=key))
    
    @property
    def usuarios(self)->set[str]:
        if self.__usuarios is None:
            self.__usuarios = {m.usuario for m in self.mensajes}
        return self.__usuarios
    
    @property
    def mensajes_por_usuario(self)->dict[str,list[Mensaje]]:
        if self.__mensajes_por_usuario is None:
            self.__mensajes_por_usuario = self.__mensajes_por_propiedad(key=lambda m: m.usuario)
        return self.__mensajes_por_usuario
    
    @property
    def numero_de_mensajes_por_usuario(self)->Counter[str]:
        if self.__numero_de_mensajes_por_usuario is None:
            self.__numero_de_mensajes_por_usuario = self.__numero_de_mensajes_por_propiedad(lambda m: m.usuario)
        return self.__numero_de_mensajes_por_usuario
    
    @property
    def frecuencia_de_palabras(self)->dict[str,int]:
        if self.__frecuencia_de_palabras is None:
            c:Counter[str] = Counter()
            self.__frecuencia_de_palabras =  reduce(lambda x,y: x+y,(m.frecuencia_de_palabras for m in self.mensajes),c)
        return self.__frecuencia_de_palabras
    
    @property
    def numero_de_palabras(self)->int:
        if self.__numero_de_palabras is None:
            self.__numero_de_palabras = sum(n for _,n in self.frecuencia_de_palabras.items())
        return self.__numero_de_palabras
    
    @property
    def frecuencia_de_palabras_por_usuario(self)->Counter[tuple[str,str]]:
        if self.__frecuencia_de_palabras_por_usuario is None:
            cv: Counter[tuple[str,str]] = Counter()
            cf:Callable[[Counter[str],str],Counter[tuple[str,str]]] = lambda c,u: Counter({(u,p):f for p,f in c.items()})
            self.__frecuencia_de_palabras_por_usuario = \
                reduce(lambda x,y: x+y,(cf(m.frecuencia_de_palabras,m.usuario) for m in self.mensajes),cv)
        return self.__frecuencia_de_palabras_por_usuario
    
    @property
    def numero_de_palabras_por_usuario(self)->Counter[str]:     
        if self.__numero_de_palabras_por_usuario is None:
            self.__numero_de_palabras_por_usuario = \
                Counter(groups_size(self.frecuencia_de_palabras_por_usuario.items(), \
                                key=lambda e:e[0][0],value=lambda e:e[1]))                              
        return self.__numero_de_palabras_por_usuario
    
    @property
    def palabras_de_usuario(self)->dict[str,set[str]]:
        if self.__palabras_de_usuario is None:
            self.__palabras_de_usuario  = \
                grouping_set(self.frecuencia_de_palabras_por_usuario.keys(),key=lambda x:x[0],value=lambda x:x[1])
        return self.__palabras_de_usuario
    
    @property
    def frecuencia_de_palabras_por_resto_de_usuarios(self)->Counter[tuple[str,str]]:
        if self.__frecuencia_de_palabras_por_resto_de_usuarios is None:
            self.__frecuencia_de_palabras_por_resto_de_usuarios = \
                Counter({(u,p):self.frecuencia_de_palabras[p]-self.frecuencia_de_palabras_por_usuario[(u,p)] \
                     for u,p in self.frecuencia_de_palabras_por_usuario.keys()})
        return self.__frecuencia_de_palabras_por_resto_de_usuarios
    
    @property
    def numero_de_palabras_por_resto_de_usuarios(self)->Counter[str]:
        if self.__numero_de_palabras_por_resto_de_usuarios is None:
            self.__numero_de_palabras_por_resto_de_usuarios = \
                Counter(groups_size(self.frecuencia_de_palabras_por_resto_de_usuarios.items(), \
                                key=lambda e:e[0][0],value=lambda e:e[1]))
        return self.__numero_de_palabras_por_resto_de_usuarios      
    
    @property
    def mensajes_por_dia_de_semana(self) -> dict[str,list[Mensaje]]:
        return  self.__mensajes_por_propiedad(key = lambda m: m.fecha.strftime('%A'))
    
    @property
    def mensajes_por_fecha(self) -> dict[date,list[Mensaje]]:
        return self.__mensajes_por_propiedad(lambda m: m.fecha) 
    
    @property
    def mensajes_por_hora(self) -> dict[int,list[Mensaje]]:
        return self.__mensajes_por_propiedad(lambda m: m.hora.hour)
    
    @property
    def numero_de_mensajes_por_dia_de_semana(self) -> Counter[str]:
        return self.__numero_de_mensajes_por_propiedad(key = lambda m: m.fecha.strftime('%A'))
    
    @property
    def numero_de_mensajes_por_fecha(self) -> Counter[date]:
        return self.__numero_de_mensajes_por_propiedad(key = lambda m: m.fecha) 
    
    @property
    def numero_de_mensajes_por_hora(self) -> Counter[int]:
        return self.__numero_de_mensajes_por_propiedad(key = lambda m: m.hora.hour) 
    
    def importancia_de_palabra(self,usuario:str,palabra:str) -> float:             
        return (self.frecuencia_de_palabras_por_usuario[(usuario,palabra)] \
                * self.numero_de_palabras_por_resto_de_usuarios[usuario]) \
                 / (self.numero_de_palabras_por_usuario[usuario] \
                 * max(0.00001,self.frecuencia_de_palabras_por_resto_de_usuarios.get((usuario,palabra),0.00001)))
    
    def palabras_caracteristicas_de_usuario(self,usuario:str) -> dict[str,float]:
        return {p:self.importancia_de_palabra(usuario, p) 
                    for p in self.palabras_de_usuario[usuario] if self.importancia_de_palabra(usuario, p) >0}
    
    def diagrama_de_barras_mensajes_por_dia_de_semana(self,file_out:str) -> None: 
        ls:list[tuple[str,int]] = [x for x in self.numero_de_mensajes_por_dia_de_semana.items()] 
        ls.sort(key=lambda e:e[0])    
        nombres_columna = [x[0] for x in ls]       
        datos =  [x[1] for x in ls]     
        nombres_datos = ['DiaDeSemana','NumeroDeMensajes']       
        Graphics.columns_bar_chart(file_out, "MensajesPorDiaDeSemana", nombres_datos,nombres_columna, datos)
              
    def diagrama_de_tarta_mensajes_por_dia_de_semana(self,file_out:str) -> None: 
        ls = [x for x in self.numero_de_mensajes_por_dia_de_semana.items()] 
        ls.sort(key=lambda e:e[0])    
        nombres_columna = [x[0] for x in ls]       
        datos =  [x[1] for x in ls]     
        nombres_datos = ['DiaDeSemana','NumeroDeMensajes']       
        Graphics.pie_chart(file_out, "MensajesPorDiaDeSemana",nombres_datos,nombres_columna, datos)
    
if __name__ == '__main__':
    c = Conversacion.of_file(absolute_path("/resources/bigbangtheory_es.txt"))
#    print(c)    
    print(str_iter(c.numero_de_mensajes_por_usuario.items()))
    print('___________')
    tsf = lambda e:'{0:s}={1}'.format(e[0],e[1])
    print(str_iter(c.numero_de_palabras_por_usuario.items(),key=tsf,sep='\n',prefix='',suffix=''))
    print('___________')
    print(str_iter(c.numero_de_palabras_por_resto_de_usuarios.items(),key=tsf,sep='\n',prefix='',suffix=''))
    print('___________')
    print(c.numero_de_palabras_por_resto_de_usuarios['Leonard'])
    c.diagrama_de_barras_mensajes_por_dia_de_semana(absolute_path("/ficheros/por_dia_de_semana_barras.html"))
    c.diagrama_de_tarta_mensajes_por_dia_de_semana(absolute_path("/ficheros/por_dia_de_semana_tarta.html"))
    print('___________')
    ls = [e for e in c.palabras_caracteristicas_de_usuario('Sheldon').items()]
    ls.sort(key= lambda e: e[1], reverse = True)
    print(str_iter(ls,sep='\n',key=lambda x:f'{x[0]:15}{x[1]:.2f}',prefix='',suffix=''))
    
    
    
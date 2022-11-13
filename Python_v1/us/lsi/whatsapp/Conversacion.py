'''
Created on 26 jul. 2020

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Callable, Optional
from us.lsi.whatsapp.Mensaje import Mensaje
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from us.lsi.tools.Iterable import strfiter, grouping_list, groups_size, flat_map
from us.lsi.whatsapp.UsuarioPalabra import UsuarioPalabra
from datetime import date
import re
from us.lsi.tools import Graphics

P = TypeVar('P')

week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
n_week_days = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
sep = r'[ ,;.\n():?!\"]'


class Conversacion:
    
    def __init__(self, mensajes: list[Mensaje], palabras_huecas: set[str]):
        self.__mensajes: list[Mensaje] = mensajes
        self.__palabras_huecas: set[str] = palabras_huecas
        self.__usuarios: set[str] = {m.usuario for m in self.__mensajes}
        self.__mensajes_por_usuario: Optional[dict[str,list[Mensaje]]] = None
        self.__numero_de_mensajes_por_usuario: Optional[dict[str,int]] = None
        self.__frecuencia_de_palabras: Optional[dict[str,int]] = None
        self.__numero_de_palabras: Optional[int] = None
        self.__frecuencia_de_palabras_por_usuario: Optional[dict[UsuarioPalabra,int]] = None
        self.__numero_de_palabras_por_usuario: Optional[dict[str,int]] = None
        self.__frecuencia_de_palabras_por_resto_de_usuarios: Optional[dict[UsuarioPalabra,int]] = None
        self.__numero_de_palabras_por_resto_de_usuarios: Optional[dict[str,int]] = None

    @staticmethod   
    def parse(file: str) -> Conversacion:
        ms = (Mensaje.parse(m) for m in lineas_de_fichero(file))
        mensajes = [m for m in ms if m is not None]
        palabrasHuecas = {p for p in lineas_de_fichero("../../../resources/palabras_huecas.txt") if len(p) >0}
        return Conversacion(mensajes,palabrasHuecas)
    
    def __str__(self) -> str:
        it1 = strfiter(self.palabras_huecas)
        it2 = strfiter(self.mensajes,sep='\n',prefix='',suffix='')
        return 'Palabras huecas = \n{0:s}\nMensajes = \n{1:s}'.format(it1, it2)       
 
    def _mensajes_por_propiedad(self, key: Callable[[Mensaje],P]) -> dict[P,list[Mensaje]]:
        return grouping_list(self.mensajes,key=key)
           
    def _numero_de_mensajes_por_propiedad(self, key: Callable[[Mensaje],P]) -> dict[P,int]:
        return groups_size(self.mensajes,key=key)
    
    @property
    def mensajes(self) -> list[Mensaje]:
        return self.__mensajes
    
    @property
    def palabras_huecas(self) -> set[str]:
        return self.__palabras_huecas
    
    @property
    def usuarios(self) -> set[str]:
        return self.__usuarios
       
    @property
    def mensajes_por_usuario(self) -> dict[str,list[Mensaje]]:
        if self.__mensajes_por_usuario is None:
            self.__mensajes_por_usuario = self._mensajes_por_propiedad(key=lambda m: m.usuario)
            return self.__mensajes_por_usuario
        else:
            return self.__mensajes_por_usuario
    
    @property
    def mensajes_por_dia_de_semana(self) -> dict[str,list[Mensaje]]:
        return  self._mensajes_por_propiedad(key = lambda m: m.fecha.strftime('%A'))
    
    @property
    def mensajes_por_fecha(self) -> dict[date,list[Mensaje]]:
        return self._mensajes_por_propiedad(lambda m: m.fecha) 
    
    @property
    def mensajes_por_hora(self) -> dict[int,list[Mensaje]]:
        return self._mensajes_por_propiedad(lambda m: m.hora.hour)
    
    @property
    def numero_de_mensajes_por_usuario(self) -> dict[str,int]:
        if self.__numero_de_mensajes_por_usuario is None:
            self.__numero_de_mensajes_por_usuario = self._numero_de_mensajes_por_propiedad(lambda m: m.usuario)
        return self.__numero_de_mensajes_por_usuario
    
    @property
    def numero_de_mensajes_por_dia_de_semana(self) -> dict[str,int]:
        return self._numero_de_mensajes_por_propiedad(key = lambda m: m.fecha.strftime('%A'))
    
    @property
    def numero_de_mensajes_por_fecha(self) -> dict[date,int]:
        return self._numero_de_mensajes_por_propiedad(key = lambda m: m.fecha) 
    
    @property
    def numero_de_mensajes_por_hora(self) -> dict[int,int]:
        return self._numero_de_mensajes_por_propiedad(key = lambda m: m.hora.hour) 
    
    @property
    def frecuencia_de_palabras(self) -> dict[str,int]:
        if self.__frecuencia_de_palabras is None:
            ms_tex = (m.texto for m in self.mensajes)
            ps = flat_map(ms_tex,lambda x: re.split(sep, x))
            palabras = (p for p in ps if len(p) > 0 and p not in self.palabras_huecas)
            self.__frecuencia_de_palabras = groups_size(palabras,key=lambda x:x)
        return self.__frecuencia_de_palabras
    
    @property
    def numero_de_palabras(self) -> int:
        if self.__numero_de_palabras is None:
            self.__numero_de_palabras = sum(n for _,n in self.frecuencia_de_palabras.items())
        return self.__numero_de_palabras
    
    @property
    def frecuencia_de_palabras_por_usuario(self) -> dict[UsuarioPalabra,int]:
        if self.__frecuencia_de_palabras_por_usuario is None:
            ms_us_tex = ((m.usuario,m.texto) for m in self.mensajes)
            plsu = (UsuarioPalabra.of(u,p) for u,t in ms_us_tex for p in re.split(sep,t))
            plsuf = (pu for pu in plsu if len(pu.palabra) > 0 and pu.palabra not in self.palabras_huecas)
            self.__frecuencia_de_palabras_por_usuario = groups_size(plsuf)
        return self.__frecuencia_de_palabras_por_usuario
    
    @property
    def numero_de_palabras_por_usuario(self) -> dict[str,int]:
        return groups_size(self.frecuencia_de_palabras_por_usuario.items(),key=lambda e:e[0].usuario)
    
    @property     
    def frecuencia_de_palabras_por_resto_de_usuarios(self) -> dict[UsuarioPalabra,int]:
        if self.__frecuencia_de_palabras_por_resto_de_usuarios is None:
            fpal = ((up.usuario,up.palabra,f) for up,f in self.frecuencia_de_palabras_por_usuario.items())
            d:dict[UsuarioPalabra,int] = {}
            for u,p,f in fpal:
                for x in self.usuarios:
                    if x != u:
                        up = UsuarioPalabra.of(x,p)
                        d[up] = d.get(up,0) + f
            self.__frecuencia_de_palabras_por_resto_de_usuarios = d
        return self.__frecuencia_de_palabras_por_resto_de_usuarios
    
    @property     
    def numero_de_palabras_por_resto_de_usuarios(self) -> dict[str,int]:
        return groups_size(self.frecuencia_de_palabras_por_resto_de_usuarios.items(),key=lambda e:e[0].usuario)
    
    def importancia_de_palabra(self,usuario:str,palabra:str) -> float:
        return (self.frecuencia_de_palabras_por_usuario[UsuarioPalabra.of(usuario,palabra)] \
                / self.numero_de_palabras_por_usuario[usuario]) * \
                (self.numero_de_palabras_por_resto_de_usuarios[usuario] \
                /self.frecuencia_de_palabras_por_resto_de_usuarios[UsuarioPalabra.of(usuario,palabra)])
    
    def palabras_caracteristicas_de_usuario(self,usuario:str,umbral:int) -> dict[str,float]:
        r1 = (e for e in self.frecuencia_de_palabras_por_usuario.items() if e[0].usuario == usuario) 
        r2 = (e for e in r1 if self.frecuencia_de_palabras.get(e[0].palabra,0) > umbral)
        r3 = (e for e in r2 if e[1] > umbral)
        r4 = (e for e in r3 if self.frecuencia_de_palabras_por_resto_de_usuarios.get(e[0],0) > umbral)
        r5 = ((e[0].palabra,self.importancia_de_palabra(e[0].usuario,e[0].palabra)) for e in r4)
        return {e[0]:e[1] for e in r5}
    
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
    c = Conversacion.parse(absolute_path("/resources/bigbangtheory_es.txt"))
#    print(c)    
    print(strfiter(c.numero_de_mensajes_por_usuario.items()))
    tsf = lambda e:'{0:s}={1}'.format(e[0],e[1])
    print(strfiter(c.numero_de_palabras_por_usuario.items(),key=tsf,sep='\n',prefix='',suffix=''))
    print(strfiter(c.numero_de_palabras_por_resto_de_usuarios.items(),key=tsf,sep='\n',prefix='',suffix=''))
    print(c.numero_de_palabras_por_resto_de_usuarios['Leonard'])
#    c.diagrama_de_barras_mensajes_por_dia_de_semana("../../../ficheros/por_dia_de_semana_barras.html")
#    c.diagrama_de_tarta_mensajes_por_dia_de_semana("../../../ficheros/por_dia_de_semana_tarta.html")
    ls = [e for e in c.palabras_caracteristicas_de_usuario('Leonard',3).items()]
    ls.sort(key= lambda e: e[1], reverse = True)
    print(strfiter(ls,sep='\n'))
    
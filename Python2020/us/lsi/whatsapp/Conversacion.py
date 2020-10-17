'''
Created on 26 jul. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from typing import TypeVar, List, Set, Dict, Callable
from us.lsi.whatsapp.Mensaje import Mensaje
from us.lsi.tools.File import lineas_de_fichero
from us.lsi.tools.Functions import identity
from us.lsi.tools.Iterable import str_iterable, grouping_list, grouping, flat_map
from us.lsi.whatsapp.UsuarioPalabra import UsuarioPalabra
from datetime import date
import re
from us.lsi.tools import Graphics

Conversacion = TypeVar('Conversacion')
P = TypeVar('P')

week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
sep = r'[ ,;.\n():?!\"]'

@dataclass
class Conversacion:
    _mensajes: List[Mensaje]
    _palabras_huecas: Set[str]
    _usuarios: Set[str] = None
    _mensajes_por_usuario: Dict[str,Mensaje] = None
    _mensajes_por_dia_de_semana: Dict[int,Mensaje] = None
    _mensajes_por_fecha: Dict[date,Mensaje] = None
    _mensajes_por_hora: Dict[int,Mensaje] = None
    _numero_de_mensajes_por_usuario: Dict[str,int] = None
    _numero_de_mensajes_por_dia_de_semana: Dict[int,int] = None
    _numero_de_mensajes_por_fecha: Dict[date,int] = None
    _numero_de_mensajes_por_hora: Dict[int,int] = None
    _frecuencia_de_palabras: Dict[str,int] = None
    _numero_de_palabras: int = None
    _frecuencia_de_palabras_por_usuario: Dict[UsuarioPalabra,int] = None
    _numero_de_palabras_por_usuario: Dict[str,int] = None
    _frecuencia_de_palabras_por_resto_de_usuarios: Dict[UsuarioPalabra,int] = None
    _numero_de_palabras_por_resto_de_usuarios: Dict[str,int] = None

    @staticmethod   
    def data_of_file(file: str) -> Conversacion:
        ms = (Mensaje.parse(m) for m in lineas_de_fichero(file))
        mensajes = [m for m in ms if m is not None]
        palabrasHuecas = {p for p in lineas_de_fichero("../../../resources/palabras_huecas.txt") if len(p) >0}
        return Conversacion(mensajes,palabrasHuecas)
    
    def __str__(self) -> str:
        return 'Palabras huecas = \n{0:s}\nMensajes = \n{1:s}'.format(str_iterable(self.palabras_huecas), str_iterable(self.mensajes,separator='\n',prefix='',suffix=''))       
 
    def _mensajes_por_propiedad(self, p: Callable[[Mensaje],P]) -> Dict[P,List[Mensaje]]:
        return grouping_list(self.mensajes,fkey=p)
           
    def _numero_de_mensajes_por_propiedad(self, p: Callable[[Mensaje],P]) -> Dict[P,int]:
        return grouping(self.mensajes,fkey=p,op=lambda x,_: x+1,a0=0)
    
    @property
    def mensajes(self) -> List[Mensaje]:
        return self._mensajes
    
    @property
    def palabras_huecas(self) -> Set[str]:
        return self._palabras_huecas
    
    @property
    def usuarios(self) -> Set[str]:
        if self._usuarios is None:
            self._usuarios = {m.usuario for m in self.mensajes}
        return self._usuarios
       
    @property
    def mensajes_por_usuario(self) -> Dict[str,Mensaje]:
        if self._mensajes_por_usuario is None:
            self._mensajes_por_usuario = self._mensajes_por_propiedad(lambda m: m.usuario)
        return self._mensajes_por_usuario
    
    @property
    def mensajes_por_dia_de_semana(self) -> Dict[str,Mensaje]:
        if self._mensajes_por_dia_de_semana is None:
            self._mensajes_por_dia_de_semana = self._mensajes_por_propiedad(lambda m: m.fecha.weekday())
        return self._mensajes_por_dia_de_semana
    
    @property
    def mensajes_por_fecha(self) -> Dict[date,Mensaje]:
        if self._mensajes_por_fecha is None:
            self._mensajes_por_fecha = self._mensajes_por_propiedad(lambda m: m.fecha)
        return self._mensajes_por_fecha 
    
    @property
    def mensajes_por_hora(self) -> Dict[int,Mensaje]:
        if self._mensajes_por_hora is None:
            self._mensajes_por_hora = self._mensajes_por_propiedad(lambda m: m.hora.hour)
        return self._mensajes_por_hora 
    
    @property
    def numero_de_mensajes_por_usuario(self) -> Dict[str,int]:
        if self._numero_de_mensajes_por_usuario is None:
            self._numero_de_mensajes_por_usuario = self._numero_de_mensajes_por_propiedad(lambda m: m.usuario)
        return self._numero_de_mensajes_por_usuario
    
    @property
    def numero_de_mensajes_por_dia_de_semana(self) -> Dict[str,int]:
        if self._numero_de_mensajes_por_dia_de_semana is None:
            self._numero_de_mensajes_por_dia_de_semana = self._numero_de_mensajes_por_propiedad(lambda m: m.fecha.weekday())
        return self._numero_de_mensajes_por_dia_de_semana
    
    @property
    def numero_de_mensajes_por_fecha(self) -> Dict[date,int]:
        if self._numero_de_mensajes_por_fecha is None:
            self._numero_de_mensajes_por_fecha = self._numero_de_mensajes_por_propiedad(lambda m: m.fecha)
        return self._numero_de_mensajes_por_fecha 
    
    @property
    def numero_de_mensajes_por_hora(self) -> Dict[int,int]:
        if self._numero_de_mensajes_por_hora is None:
            self._numero_de_mensajes_por_hora = self._numero_de_mensajes_por_propiedad(lambda m: m.hora.hour)
        return self._numero_de_mensajes_por_hora 
    
    @property
    def frecuencia_de_palabras(self) -> Dict[str,int]:
        if self._frecuencia_de_palabras is None:
            ms_tex = (m.texto for m in self.mensajes)
            ps = flat_map(ms_tex,lambda x: re.split(sep, x))
            palabras = (p for p in ps if len(p) > 0 and p not in self.palabras_huecas)
            self._frecuencia_de_palabras = grouping(palabras,fkey=identity,op=lambda x,_: x+1,a0=0)
        return self._frecuencia_de_palabras
    
    @property
    def numero_de_palabras(self) -> int:
        return sum(n for _,n in self.frecuencia_de_palabras.items())
    
    @property
    def numero_de_palabras_por_usuario(self) -> Dict[str,int]:
        return grouping(self.frecuencia_de_palabras_por_usuario.items(),fkey=lambda e:e[0].usuario,op=lambda x,e: x+e[1],a0=0)
    
    @property
    def frecuencia_de_palabras_por_usuario(self) -> Dict[UsuarioPalabra,int]:
        if self._frecuencia_de_palabras_por_usuario is None:
            ms_us_tex = ((m.usuario,m.texto) for m in self.mensajes)
            plsu = (UsuarioPalabra.of(u,p) for u,t in ms_us_tex for p in re.split(sep,t))
            plsuf = (pu for pu in plsu if len(pu.palabra) > 0 and pu.palabra not in self.palabras_huecas)
            self._frecuencia_de_palabras_por_usuario = grouping(plsuf,fkey=identity,op=lambda x,_: x+1,a0=0)
        return self._frecuencia_de_palabras_por_usuario
    
    @property     
    def frecuencia_de_palabras_por_resto_de_usuarios(self) -> Dict[UsuarioPalabra,int]:
        if self._frecuencia_de_palabras_por_resto_de_usuarios is None:
            fpal = ((up.usuario,up.palabra,f) for up,f in self.frecuencia_de_palabras_por_usuario.items())
            d = {}
            for u,p,f in fpal:
                for x in self.usuarios:
                    if x != u:
                        up = UsuarioPalabra.of(x,p)
                        d[up] = d.get(up,0) + f
            self._frecuencia_de_palabras_por_resto_de_usuarios = d
        return self._frecuencia_de_palabras_por_resto_de_usuarios
    
    @property     
    def numero_de_palabras_por_resto_de_usuarios(self) -> Dict[str,int]:
        return grouping(self.frecuencia_de_palabras_por_resto_de_usuarios.items(),fkey=lambda e:e[0].usuario,op=lambda x,e: x+e[1],a0=0)
    
    def importancia_de_palabra(self,usuario:str,palabra:str) -> float:
        return (self.frecuencia_de_palabras_por_usuario[UsuarioPalabra.of(usuario,palabra)] \
                / self.numero_de_palabras_por_usuario[usuario]) * \
                (self.numero_de_palabras_por_resto_de_usuarios[usuario] \
                /self.frecuencia_de_palabras_por_resto_de_usuarios[UsuarioPalabra.of(usuario,palabra)])
    
    def palabras_caracteristicas_de_usuario(self,usuario:str,umbral:int) -> Dict[str,float]:
        r1 = (e for e in self.frecuencia_de_palabras_por_usuario.items() if e[0].usuario == usuario) 
        r2 = (e for e in r1 if self.frecuencia_de_palabras.get(e[0].palabra,0) > umbral)
        r3 = (e for e in r2 if e[1] > umbral)
        r4 = (e for e in r3 if self.frecuencia_de_palabras_por_resto_de_usuarios.get(e[0],0) > umbral)
        r5 = ((e[0].palabra,self.importancia_de_palabra(e[0].usuario,e[0].palabra)) for e in r4)
        return {e[0]:e[1] for e in r5}
    
    def diagrama_de_barras_mensajes_por_dia_de_semana(self,file_out:str) -> None: 
        ls = [x for x in self.numero_de_mensajes_por_dia_de_semana.items()] 
        ls.sort(key=lambda e:e[0])    
        nombres_columna = [week_days[x[0]] for x in ls]       
        datos =  [x[1] for x in ls]     
        nombres_datos = ['DiaDeSemana','NumeroDeMensajes']       
        Graphics.columnsBarChart(file_out, "MensajesPorDiaDeSemana", nombres_datos,nombres_columna, datos)
        
    def diagrama_de_tarta_mensajes_por_dia_de_semana(self,file_out:str) -> None: 
        ls = [x for x in self.numero_de_mensajes_por_dia_de_semana.items()] 
        ls.sort(key=lambda e:e[0])    
        nombres_columna = [week_days[x[0]] for x in ls]       
        datos =  [x[1] for x in ls]     
        nombres_datos = ['DiaDeSemana','NumeroDeMensajes']       
        Graphics.pieChart(file_out, "MensajesPorDiaDeSemana",nombres_datos,nombres_columna, datos)
    
if __name__ == '__main__':
    c = Conversacion.data_of_file("../../../resources/bigbangtheory_es.txt")
#    print(c)    
    print(str_iterable(c.numero_de_mensajes_por_usuario.items()))
    tsf = lambda e:'{0:s}={1}'.format(e[0],e[1])
    print(str_iterable(c.numero_de_palabras_por_usuario.items(),ts=tsf,separator='\n',prefix='',suffix=''))
    print(str_iterable(c.numero_de_palabras_por_resto_de_usuarios.items(),ts=tsf,separator='\n',prefix='',suffix=''))
    print(c.numero_de_palabras_por_resto_de_usuarios['Leonard'])
#    c.diagrama_de_barras_mensajes_por_dia_de_semana("../../../ficheros/por_dia_de_semana_barras.html")
#    c.diagrama_de_tarta_mensajes_por_dia_de_semana("../../../ficheros/por_dia_de_semana_tarta.html")
    ls = [e for e in c.palabras_caracteristicas_de_usuario('Leonard',3).items()]
    ls.sort(key= lambda e: e[1], reverse = True)
    print(str_iterable(ls,separator='\n'))
    
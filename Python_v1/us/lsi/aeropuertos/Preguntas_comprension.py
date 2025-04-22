'''
Created on 21 ago 2022

@author: migueltoro
'''

from datetime import date,datetime
from collections import OrderedDict
from sortedcontainers import SortedSet # type: ignore
from us.lsi.aeropuertos.VueloProgramado import VueloProgramado
from us.lsi.aeropuertos.Vuelo import Vuelo
from us.lsi.tools.Iterable import first, grouping_list,grouping_set,groups_size,grouping_reduce
from us.lsi.tools.Iterable import str_iter
from us.lsi.tools.Dict import str_dict
from collections import Counter
from us.lsi.aeropuertos.Espacio_aereo import Espacio_aereo
from typing import Optional, Iterable, Callable
from statistics import mean, StatisticsError

#1. Dada una cadena de caracteres s devuelve el numero total de pasajeros a
# ciudades destino que tienen
# como prefijo s (esto es, comienzan por s).  
 
def numero_de_pasajeros(prefix:str)->int:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    return sum(v.num_pasajeros for v in ls if v.vuelo_programado.ciudad_destino.startswith(prefix))

#2.  Dado un conjunto de ciudades destino s y una fecha f devuelve cierto si
# existe un vuelo en la fecha f con destino en s.

 
def hay_destino(destinos:set[str], f:date)-> bool:
    ls:list[Vuelo] = Espacio_aereo.of().vuelos.todos
    return any(v.fecha.date() == f for v in ls if v.vuelo_programado.ciudad_destino in destinos)


#3. Dada una fecha f devuelve el conjunto de ciudades destino diferentes de todos
# los vuelos de fecha f

 
def destinos_diferentes(f:date)->set[str]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    return {v.vuelo_programado.ciudad_destino for v in ls if v.fecha_salida == f}

#4. Dado un anyo devuelve un OrderedDict que relacione cada destino con el
# total de pasajeros a ese destino en el anyo a


def total_pasajeros_a_destino(a:int)->OrderedDict[str,int]:
    ls: list[Vuelo] = list(v for v in Espacio_aereo.of().vuelos.todos if v.fecha.year == a)
    d:dict[str,int] = grouping_reduce(ls,key=lambda v:v.vuelo_programado.ciudad_destino,op=lambda x,y:x+y,value=lambda v:v.num_pasajeros)
    return OrderedDict(sorted(d.items()))

#5. Dado un destino devuelve el codigo de la aerolinea del primer vuelo con plazas libres a ese
# destino y posterior a una fecha dada


def primer_vuelo(destino:str,f:datetime)->Optional[str]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    return first(v.vuelo_programado.codigo_aerolinea for v in ls if v.vuelo_programado.ciudad_destino == destino and \
            v.vuelo_programado.num_plazas > v.num_pasajeros and \
            v.fecha > f)

#6. Devuelve para los vuelos con menos n de plazas libres un Map que haga corresponder a cada ciudad
# destino la media de los precios de los vuelos a ese destino.


def precios_medios(n:int)->dict[str,float]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    s = (v for v in ls if v.vuelo_programado.num_plazas-v.num_pasajeros < n)
    r: dict[str,list[float]] = grouping_list(s,key=lambda x:x.vuelo_programado.ciudad_destino,value=lambda x:x.vuelo_programado.precio)
    return {c:mean(r[c]) for c in r.keys()}

#7. Devuelve un Map tal que dado un entero n haga corresponder
# a cada mes la __ocupaciones_vuelos de los n destinos con los vuelos de mayor duracion.

def ldf(ls:list[VueloProgramado],n:int)->list[str]:
    return [v.ciudad_destino for v in sorted(ls,key=lambda v:v.duracion.total_seconds(),reverse=True)][0:n]

ld:Callable[[list[VueloProgramado],int],list[str]] = \
    lambda ls,n:[v.ciudad_destino for v in sorted(ls,key=lambda v:v.duracion.total_seconds(),reverse=True)][0:n]
    
# ldf y ld son equivalentes
    
def destinos_con_mayor_duracion(n:int)->dict[int,list[str]]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    r: dict[int,list[VueloProgramado]] = grouping_list(ls,key=lambda x:x.fecha_salida.month,value=lambda v:v.vuelo_programado)    
    return {k:ldf(r[k],n) for k in r.keys()}

#8. Dada una fecha f devuelve el precio medio de los vuelos con salida posterior
# a f. Si no hubiera vuelos devuelve 0.0

def precio_medio_posterior(f:datetime)->float:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    try:
        return mean(v.vuelo_programado.precio for v in ls if v.fecha > f)
    except StatisticsError:
        return 0.0

#9. Devuelve un Map que haga corresponder a cada destino un conjunto con las
# fechas de los vuelos a ese destino.

 
def fechas_a_destino()->dict[str,set[date]]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    return grouping_set(ls,key=lambda v:v.vuelo_programado.ciudad_destino,value=lambda v:v.fecha_salida)

#10. Devuelve el destino con mayor numero de vuelos

def destino_con_mas_vuelos()->str:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    return Counter(v.vuelo_programado.ciudad_destino for v in ls).most_common(1)[0][0]

#11. Dado un entero m devuelve un conjunto ordenado con las duraciones 
# de todos los vuelos cuya duracion es mayor que m minutos.


def duraciones(m:int)->SortedSet[int]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    s:Iterable[int] = (int(v.vuelo_programado.duracion.total_seconds()/60) for v in ls if v.vuelo_programado.duracion.total_seconds()//60 > m)
    return SortedSet(sorted(s,reverse=True))

#12. Dado un numero n devuelve un conjunto con los n destinos de los vuelos con mayor duracion


def destinos_mayor_duracion(n:int)->set[str]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    s = [v.vuelo_programado.ciudad_destino for v in sorted(ls,
               key=lambda v:v.vuelo_programado.duracion.total_seconds(), reverse=True)][0:n]
    return set(s)

#13. Dado un numero n devuelve un conjunto con los n destinos con mas vuelos

 
def con_mas_vuelos(n:int)->list[tuple[str,int]]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    return Counter(v.vuelo_programado.ciudad_destino for v in ls).most_common(n)
    

# 14. Dado un numero entero n devuelve una __ocupaciones_vuelos con los destinos que tienen mas de n vuelos


def mas_de_n_vuelos(n:int)->list[str]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    return [d for d,c in Counter(v.vuelo_programado.ciudad_destino for v in ls).items() if c>n]

# 15. Devuelve un Map que relacion cada destino con el porcentaje de los vuelos del total que van a ese destino.


def porcentaje_a_destino()->dict[str,float]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    n = len(ls)
    d = groups_size(ls,key=lambda v:v.vuelo_programado.ciudad_destino)
    return {k:d[k]/n for k in d.keys()}
    

# 16. Devuelve un Map que haga corresponder a cada ciudad destino el vuelo mas barato


def mas_barato()->dict[str,VueloProgramado]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    return grouping_reduce(ls,key=lambda v:v.vuelo_programado.ciudad_destino,
                           op=lambda v1,v2:min((v1,v2),key=lambda v:v.precio),
                           value = lambda v:v.vuelo_programado)

# 17. Devuelve un Map que haga corresponder a cada destino el numero de fechas
# distintas en las que hay vuelos a ese destino.

def fechasDistintas()->OrderedDict[str,int]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    g = grouping_set(ls,key=lambda v:v.vuelo_programado.ciudad_destino,value = lambda v:v.fecha_salida)
    d =  {k:len(g[k]) for k in g.keys()}
    return OrderedDict(sorted(d.items(),key=lambda x:x[1],reverse=True))

if __name__ == '__main__':
    print(numero_de_pasajeros('Lon'))
    print(hay_destino({'Berlin','Colonia'},date(2000,1,1)))
    print(destinos_diferentes(date(2020,6,8)))
    print(str_dict(total_pasajeros_a_destino(2020)))
    print(primer_vuelo('Eindhoven',datetime(2019,6,8,0,0)))
    print(str_dict(precios_medios(5)))
    print(str_dict(destinos_con_mayor_duracion(10)))
    print(precio_medio_posterior(datetime(2019,6,8,0,0)))
    print(fechas_a_destino())
    print(destino_con_mas_vuelos())
    print(duraciones(30))
    print(destinos_mayor_duracion(20))
    print(con_mas_vuelos(20))
    print(mas_de_n_vuelos(4))
    print(str_dict(porcentaje_a_destino()))
    print(str_dict(mas_barato()))
    print(str_iter(fechasDistintas().items()))
    print(duraciones(10))

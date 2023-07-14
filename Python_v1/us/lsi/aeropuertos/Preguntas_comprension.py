'''
Created on 21 ago 2022

@author: migueltoro
'''

from datetime import date,datetime
from collections import OrderedDict
from ordered_set import OrderedSet
from us.lsi.aeropuertos.Vuelo import Vuelo
from us.lsi.aeropuertos.Ocupacion_vuelo import Ocupacion_vuelo
from us.lsi.tools.Iterable import first, grouping_list,grouping_set,groups_size,grouping_reduce
from us.lsi.tools.Iterable import str_iter
from us.lsi.tools.Dict import str_dict
from collections import Counter
from us.lsi.aeropuertos.Espacio_aereo import Espacio_aereo
from typing import Optional, Iterable
from statistics import mean

#1. Dada una cadena de caracteres s devuelve el numero total de pasajeros a
# ciudades destino que tienen
# como prefijo s (esto es, comienzan por s).  
 
def numero_de_pasajeros(prefix:str)->int:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    return sum(ocp.num_pasajeros for ocp in ls if ocp.vuelo.ciudad_destino.startswith(prefix))

#2.  Dado un conjunto de ciudades destino s y una fecha f devuelve cierto si
# existe un vuelo en la fecha f con destino en s.

 
def hay_destino(destinos:set[str], f:date)-> bool:
    ls:list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    return any(ocp.fecha.date() == f for ocp in ls if ocp.vuelo.ciudad_destino in destinos)


#3. Dada una fecha f devuelve el conjunto de ciudades destino diferentes de todos
# los vuelos de fecha f

 
def destinos_diferentes(f:date)->set[str]:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    return {ocp.vuelo.ciudad_destino for ocp in ls if ocp.fecha_salida == f}

#4. Dado un anyo devuelve un OrderedDict que relacione cada destino con el
# total de pasajeros a ese destino en el anyo a


def total_pasajeros_a_destino(a:int)->OrderedDict[str,int]:
    ls: list[Ocupacion_vuelo] = list(ocp for ocp in Espacio_aereo.of().ocupaciones_vuelos.todas if ocp.fecha.year == a)
    d:dict[str,int] = grouping_reduce(ls,key=lambda ocp:ocp.vuelo.ciudad_destino,op=lambda x,y:x+y,value=lambda ocp:ocp.num_pasajeros)
    return OrderedDict(sorted(d.items()))

#5. Dado un destino devuelve el codigo de la aerolinea del primer vuelo con plazas libres a ese
# destino y posterior a una fecha dada


def primer_vuelo(destino:str,f:datetime)->Optional[str]:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    return first(ocp.vuelo.codigo_aerolinea for ocp in ls if ocp.vuelo.ciudad_destino == destino and \
            ocp.vuelo.num_plazas > ocp.num_pasajeros and \
            ocp.fecha > f)

#6. Devuelve para los vuelos con menos n de plazas libres un Map que haga corresponder a cada ciudad
# destino la media de los precios de los vuelos a ese destino.


def precios_medios(n:int)->dict[str,float]:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    s = (ocp for ocp in ls if ocp.vuelo.num_plazas-ocp.num_pasajeros < n)
    r: dict[str,list[float]] = grouping_list(s,key=lambda x:x.vuelo.ciudad_destino,value=lambda x:x.vuelo.precio)
    return {c:mean(r[c]) for c in r.keys()}

#7. Devuelve un Map tal que dado un entero n haga corresponder
# a cada mes la __ocupaciones_vuelos de los n destinos con los vuelos de mayor duracion.


def destinos_con_mayor_duracion(n:int)->dict[int,list[str]]:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    r: dict[int,list[Vuelo]] = grouping_list(ls,key=lambda x:x.fecha_salida.month,value=lambda ocp:ocp.vuelo)
    ld = lambda k:(v.ciudad_destino for v in sorted(r[k],key=lambda v:v.duracion.total_seconds(),reverse=True)[0:n])
    return {k:list(ld(k)) for k in r.keys()}

#8. Dada una fecha f devuelve el precio medio de los vuelos con salida posterior
# a f. Si no hubiera vuelos devuelve 0.0

def precio_medio_posterior(f:datetime)->float:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    return mean(ocp.vuelo.precio for ocp in ls if ocp.fecha > f)

#9. Devuelve un Map que haga corresponder a cada destino un conjunto con las
# fechas de los vuelos a ese destino.

 
def fechas_a_destino()->dict[str,set[date]]:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    return grouping_set(ls,key=lambda ocp:ocp.vuelo.ciudad_destino,value=lambda ocp:ocp.fecha_salida)

#10. Devuelve el destino con mayor numero de vuelos

def destino_con_mas_vuelos()->str:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    return Counter(ocp.vuelo.ciudad_destino for ocp in ls).most_common(1)[0][0]

#11. Dado un entero m devuelve un conjunto ordenado con las duraciones 
# de todos los vuelos cuya duracion es mayor que m minutos.


def duraciones(m:int)->OrderedSet[int]:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    s:Iterable[int] = (int(ocp.vuelo.duracion.total_seconds()/60) for ocp in ls if ocp.vuelo.duracion.total_seconds()//60 > m)
    return OrderedSet(sorted(s,reverse=True))

#12. Dado un numero n devuelve un conjunto con los n destinos de los vuelos con mayor duracion


def destinos_mayor_duracion(n:int)->set[str]:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    s = [ocp.vuelo.ciudad_destino for ocp in sorted(ls,
               key=lambda ocp:ocp.vuelo.duracion.total_seconds(), reverse=True)][0:n]
    return set(s)

#13. Dado un numero n devuelve un conjunto con los n destinos con mas vuelos

 
def con_mas_vuelos(n:int)->list[tuple[str,int]]:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    return Counter(ocp.vuelo.ciudad_destino for ocp in ls).most_common(n)
    

# 14. Dado un numero entero n devuelve una __ocupaciones_vuelos con los destinos que tienen mas de n vuelos


def mas_de_n_vuelos(n:int)->list[str]:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    return [d for d,c in Counter(ocp.vuelo.ciudad_destino for ocp in ls).items() if c>n]

# 15. Devuelve un Map que relacion cada destino con el porcentaje de los vuelos del total que van a ese destino.


def porcentaje_a_destino()->dict[str,float]:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    n = len(ls)
    d = groups_size(ls,key=lambda ocp:ocp.vuelo.ciudad_destino)
    return {k:d[k]/n for k in d.keys()}
    

# 16. Devuelve un Map que haga corresponder a cada ciudad destino el vuelo mas barato


def mas_barato()->dict[str,Vuelo]:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    return grouping_reduce(ls,key=lambda ocp:ocp.vuelo.ciudad_destino,
                           op=lambda v1,v2:min((v1,v2),key=lambda v:v.precio),
                           value = lambda ocp:ocp.vuelo)

# 17. Devuelve un Map que haga corresponder a cada destino el numero de fechas
# distintas en las que hay vuelos a ese destino.

def fechasDistintas()->OrderedDict[str,int]:
    ls: list[Ocupacion_vuelo] = Espacio_aereo.of().ocupaciones_vuelos.todas
    g = grouping_set(ls,key=lambda ocp:ocp.vuelo.ciudad_destino,value = lambda ocp:ocp.fecha_salida)
    d =  {k:len(g[k]) for k in g.keys()}
    return OrderedDict(sorted(d.items(),key=lambda x:x[1],reverse=True))


if __name__ == '__main__':
    Espacio_aereo.of()
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

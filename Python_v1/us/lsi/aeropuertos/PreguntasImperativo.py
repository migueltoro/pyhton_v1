'''
Created on 21 ago 2022

@author: migueltoro
'''

from datetime import date,datetime
from collections import OrderedDict
from ordered_set import OrderedSet
from us.lsi.aeropuertos.Vuelo import Vuelo
from us.lsi.aeropuertos.OcupacionVuelo import OcupacionVuelo
from us.lsi.aeropuertos.OcupacionesVuelos import OcupacionesVuelos
from us.lsi.aeropuertos.Vuelos import Vuelos
from us.lsi.aeropuertos.Aeropuertos import Aeropuertos
from us.lsi.aeropuertos.Aerolineas import Aerolineas
from us.lsi.tools.File import absolute_path
from us.lsi.tools.Dict import str_dictionary



#1. Dada una cadena de caracteres s devuelve el numero total de pasajeros a
# ciudades destino que tienen
# como prefijo s (esto es, comienzan por s).  
 
def numero_de_pasajeros(prefix:str)->int:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    s = 0
    for ocp in ls:
        if ocp.vuelo.ciudad_destino.startswith(prefix):
            num_pasajeros = ocp.num_pasajeros
            s = s + num_pasajeros
    return s

#2.  Dado un conjunto de ciudades destino s y una fecha f devuelve cierto si
# existe un vuelo en la fecha f con destino en s.

 
def hay_destino(destinos:set[str], f:date)-> bool:
    ls:list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    a:bool = False
    for ocp in ls:
        if ocp.fecha.date() == f:
            if ocp.vuelo.ciudad_destino in destinos:
                a = True;
                break;
    return a


#3. Dada una fecha f devuelve el conjunto de ciudades destino diferentes de todos
# los vuelos de fecha f

 
def destinos_diferentes(f:date)->set[str]:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    a:set[str] = set()
    for ocp in ls:
        if ocp.fecha_salida == f:
            ciudad_destino = ocp.vuelo.ciudad_destino
            a.add(ciudad_destino);            
    return a;

#4. Dado un anyo devuelve un OrderedDict que relacione cada destino con el
# total de pasajeros a ese destino en el anyo a


def total_pasajeros_a_destino(a:int)->OrderedDict[str,int]:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    r:dict[str,int] = {}
    for ocp in ls:
        if ocp.fecha.year == a:
            key:str = ocp.vuelo.ciudad_destino
            if key in r.keys():
                num_pasajeros = r[key]+ocp.num_pasajeros
                r[key] = num_pasajeros
            else:
                r[key] = ocp.num_pasajeros
    return OrderedDict(r.items())

#5. Dado un destino devuelve el codigo de la aerolinea del primer vuelo con plazas libres a ese
# destino y posterior a una fecha dada


def primer_vuelo(destino:str,f:datetime)->str:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    a: OcupacionVuelo = None
    for ocp in ls:
        if  ocp.vuelo.ciudad_destino == destino and \
            ocp.vuelo.num_plazas > ocp.num_pasajeros and \
            ocp.fecha > f:
            if not a or ocp.fecha < a.fecha:
                a = ocp
    if not a:
        return None
    return a.vuelo.codigo_aerolinea

#6. Devuelve para los vuelos con menos de n plazas libres un Map que haga corresponder a cada ciudad
# destino la media de los precios de los vuelos a ese destino.

def precio_medio(ls:list[float])->float:
    s,n = 0,0
    for e in ls:
        s += e
        n +=1
    return s/n

def precios_medios(n_libres:int)->dict[str,float]:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    r: dict[str,list[float]] = {}
    for ocp in ls:
        if ocp.vuelo.num_plazas-ocp.num_pasajeros < n_libres:
            key = ocp.vuelo.ciudad_destino
            if key in r.keys():
                r[key].append(ocp.vuelo.precio)
            else:
                r[key] = [ocp.vuelo.precio]            
    d: dict[str,float] = {}
    for k in r.keys():
        d[k] = precio_medio(r[k])    
    return d    

#7. Devuelve un Map tal que dado un entero n haga corresponder
# a cada mes la lista de los n destinos con los vuelos de mayor duracion.


def destinos_con_mayor_duracion(n:int)->dict[date,list[str]]:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    r: dict[date,list[Vuelo]] = {}
    for ocp in ls:
        key = ocp.fecha_salida.month
        if key in r.keys():
            r[key].append(ocp.vuelo)
        else:
            r[key] = [ocp.vuelo]
    d: dict[date,list[str]] = {}
    for k in r.keys():
        d[k] = list(v.ciudad_destino for v in sorted(r[k],key=lambda v:v.duracion.total_seconds(),reverse=True)[0:n]) 
    return d    

#8. Dada una fecha f devuelve el precio medio de los vuelos con salida posterior
# a f. Si no hubiera vuelos devuelve 0.0

def precio_medio_posterior(f:datetime)->float:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    s = 0
    n = 0
    for ocp in ls:
        if ocp.fecha > f:
            s += ocp.vuelo.precio
            n += 1
    return s/n
            

#9. Devuelve un Map que haga corresponder a cada destino un conjunto con las
# fechas de los vuelos a ese destino.

 
def fechas_a_destino()->dict[str,set[date]]:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    r: dict[str,set[date]] = {}
    for ocp in ls:
        key = ocp.vuelo.ciudad_destino
        if key in r.keys():
            r[key].add(ocp.fecha_salida)
        else:
            r[key] = {ocp.fecha_salida}
    return r
    

#10. Devuelve el destino con mayor numero de vuelos

def destino_con_mas_vuelos()->tuple[str,int]:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    r: dict[str,list[Vuelo]] = {}
    for ocp in ls:
        key = ocp.vuelo.ciudad_destino
        if key in r.keys():
            r[key].append(ocp.vuelo)
        else:
            r[key] = [ocp.vuelo]
    d = None
    n = None
    for k,lv in r.items():
        if not d or len(lv) > n:
            d,n=k,len(lv)
    return (d,n)

#11. Dado un entero m devuelve un conjunto ordenado con las duraciones 
# de todos los vuelos cuya duracion es mayor que m minutos.


def duraciones(m:int)->OrderedSet[int]:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    r = []
    for ocp in ls:
        if ocp.vuelo.duracion.total_seconds()/60 > m:
            r.append(ocp.vuelo.duracion.total_seconds()/60)
    return OrderedSet(sorted(r,reverse=True))
    

#12. Dado un numero n devuelve un conjunto con los destinos de los vuelos de los vuelos con mayor duracion


def destinos_mayor_duracion(n:int)->set[str]:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    r = sorted(ls,key=lambda ocp:ocp.vuelo.duracion.total_seconds(), reverse=True)[0:n]
    s = []
    for ocp in r:
        s.append(ocp.vuelo.ciudad_destino)
    return set(s)

#13. Dado un numero n devuelve un conjunto con los n destinos con mas vuelos

 
def con_mas_vuelos(n:int)->list[tuple[str,int]]:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    r: dict[str,list[Vuelo]] = {}
    for ocp in ls:
        key = ocp.vuelo.ciudad_destino
        if key in r.keys():
            r[key].append(ocp.vuelo)
        else:
            r[key] = [ocp.vuelo]
    s:list[tuple[str,int]] = []
    for k,v in r.items():
        s.append((k,len(v)))
    return sorted(s,key=lambda x:x[1], reverse=True)[0:n]
        

# 14. Dado un numero entero n devuelve una lista con los destinos que tienen mas de n vuelos
    

def mas_de_n_vuelos(n:int)->list[str]:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    r: dict[str,list[Vuelo]] = {}
    for ocp in ls:
        key = ocp.vuelo.ciudad_destino
        if key in r.keys():
            r[key].append(ocp.vuelo)
        else:
            r[key] = [ocp.vuelo]
    s:dict[str,int] = {}
    for k,v in r.items():
        if len(v) > n:
            s[k]= len(v)
    t = sorted(s.items(),key=lambda x:x[1], reverse=True)
    u = []
    for k in t:
        u.append(k[0])
    return u

# 15. Devuelve un Map que relacion cada destino con el porcentaje de los vuelos del total que van a ese destino.


def porcentaje_a_destino()->dict[str,float]:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    n = len(ls)
    r: dict[str,list[Vuelo]] = {}
    for ocp in ls:
        key = ocp.vuelo.ciudad_destino
        if key in r.keys():
            r[key].append(ocp.vuelo)
        else:
            r[key] = [ocp.vuelo]
    s:dict[str,float] = {}
    for k,v in r.items():
            s[k]= len(v)/n
    return s


# 16. Devuelve un Map que haga corresponder a cada ciudad destino el vuelo de mas barato

def min_precio(lv:list[Vuelo])->Vuelo:   
    vm = None
    p = None
    for v in lv:
        if not p or vm.precio < p:
            vm, p = v,v.precio
    return vm
    
def mas_barato()->dict[str,Vuelo]:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    r: dict[str,list[Vuelo]] = {}
    for ocp in ls:
        key = ocp.vuelo.ciudad_destino
        if key in r.keys():
            r[key].append(ocp.vuelo)
        else:
            r[key] = [ocp.vuelo]
    s:dict[str,Vuelo] = {}
    for k,v in r.items():
            s[k]= min_precio(v)
    return s

# 17. Devuelve un Map que haga corresponder a cada destino el numero de fechas
# distintas en las que hay vuelos a ese destino.


def fechasDistintas()->dict[str,int]:
    ls: list[OcupacionVuelo] = OcupacionesVuelos.get().ocupaciones
    r: dict[str,set[date]] = {}
    for ocp in ls:
        key = ocp.vuelo.ciudad_destino
        if key in r.keys():
            r[key].add(ocp.fecha_salida)
        else:
            r[key] = {ocp.fecha_salida}
    s:dict[str,int] = {}
    for k,v in r.items():
            s[k]= len(v)
    return s

if __name__ == '__main__':
    Aeropuertos.lee_aeropuertos(absolute_path("/resources/aeropuertos.csv"))
    Aerolineas.lee_aerolineas(absolute_path("/resources/aerolineas.csv"))
    Vuelos.lee_vuelos(absolute_path("/resources/vuelos.csv"))
    OcupacionesVuelos.lee_ocupaciones(absolute_path("/resources/ocupacionesVuelos.csv"))
#    print(numero_de_pasajeros('Lon'))
#    print(hay_destino({'Berlin','Colonia'},date(2000,1,1)))
#    print(destinos_diferentes(date(2020,6,8)))
#    print(str_dictionary(total_pasajeros_a_destino(2020)))
#    print(primer_vuelo('Eindhoven',datetime(2019,6,8,0,0)))
#    print(str_dictionary(precios_medios(5)))
#    print(str_dictionary(destinos_con_mayor_duracion(10)))
#    print(precio_medio_posterior(datetime(2019,6,8,0,0)))
#    print(str_dictionary(fechas_a_destino(),strfvalue=lambda f:str_iterable(f,ts=lambda x: x.strftime("%Y-%m-%d"))))
#    print(destino_con_mas_vuelos())
#    print(duraciones(30))
#    print(destinos_mayor_duracion(20))
#    print(con_mas_vuelos(20))
#    print(mas_de_n_vuelos(4))
#    print(str_dictionary(porcentaje_a_destino()))
#    print(str_dictionary(mas_barato()))
    print(str_dictionary(fechasDistintas()))
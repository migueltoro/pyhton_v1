'''
Created on 21 ago 2022

@author: migueltoro
'''

from datetime import date,datetime
from collections import OrderedDict
from sortedcontainers import SortedSet # type: ignore
from us.lsi.aeropuertos.VueloProgramado import VueloProgramado
from us.lsi.aeropuertos.Vuelo import Vuelo
from us.lsi.aeropuertos.Espacio_aereo import Espacio_aereo
from typing import Optional
from us.lsi.tools.Dict import str_dict



#1. Dada una cadena de caracteres s devuelve el numero total de pasajeros a
# ciudades destino que tienen
# como prefijo s (esto es, comienzan por s).  
 
def numero_de_pasajeros(prefix:str)->int:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    s = 0
    for v in ls:
        if v.vuelo_programado.ciudad_destino.startswith(prefix):
            num_pasajeros = v.num_pasajeros
            s = s + num_pasajeros
    return s

#2.  Dado un conjunto de ciudades destino s y una fecha f devuelve cierto si
# existe un vuelo en la fecha f con destino en s.

 
def hay_destino(destinos:set[str], f:date)-> bool:
    ls:list[Vuelo] = Espacio_aereo.of().vuelos.todos
    a:bool = False
    for v in ls:
        if v.fecha.date() == f:
            if v.vuelo_programado.ciudad_destino in destinos:
                a = True;
                break;
    return a


#3. Dada una fecha f devuelve el conjunto de ciudades destino diferentes de todos
# los vuelos de fecha f

 
def destinos_diferentes(f:date)->set[str]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    a:set[str] = set()
    for v in ls:
        if v.fecha_salida == f:
            ciudad_destino = v.vuelo_programado.ciudad_destino
            a.add(ciudad_destino);            
    return a;

#4. Dado un anyo devuelve un OrderedDict que relacione cada destino con el
# total de pasajeros a ese destino en el anyo a


def total_pasajeros_a_destino(a:int)->OrderedDict[str,int]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    r:dict[str,int] = {}
    for v in ls:
        if v.fecha.year == a:
            key:str = v.vuelo_programado.ciudad_destino
            if key in r.keys():
                num_pasajeros = r[key]+v.num_pasajeros
                r[key] = num_pasajeros
            else:
                r[key] = v.num_pasajeros
    return OrderedDict(r.items())

#5. Dado un destino devuelve el codigo de la aerolinea del primer vuelo con plazas libres a ese
# destino y posterior a una fecha dada


def primer_vuelo(destino:str,f:datetime)->Optional[str]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    a: Optional[Vuelo] = None
    for v in ls:
        if  v.vuelo_programado.ciudad_destino == destino and \
            v.vuelo_programado.num_plazas > v.num_pasajeros and \
            v.fecha > f:
            a = v
            break
    if a:
        return a.vuelo_programado.codigo_aerolinea
    else:
        return None

#6. Devuelve para los vuelos con menos de n plazas libres un Map que haga corresponder a cada ciudad
# destino la media de los precios de los vuelos a ese destino.

def precio_medio(ls:list[float])->float:
    s,n = 0.,0
    for e in ls:
        s += e
        n +=1
    return s/n

def precios_medios(n_libres:int)->dict[str,float]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    r: dict[str,list[float]] = {}
    for v in ls:
        if v.vuelo_programado.num_plazas-v.num_pasajeros < n_libres:
            key = v.vuelo_programado.ciudad_destino
            if key in r.keys():
                r[key].append(v.vuelo_programado.precio)
            else:
                r[key] = [v.vuelo_programado.precio]            
    d: dict[str,float] = {}
    for k in r.keys():
        d[k] = precio_medio(r[k])    
    return d    

#7. Devuelve un Map tal que dado un entero n haga corresponder
# a cada mes la __ocupaciones_vuelos de los n destinos con los vuelos de mayor duracion.


def destinos_con_mayor_duracion(n:int)->dict[date,list[str]]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    r: dict[date,list[VueloProgramado]] = {}
    for v in ls:
        key = v.fecha_salida
        if key in r.keys():
            r[key].append(v.vuelo_programado)
        else:
            r[key] = [v.vuelo_programado]
    d: dict[date,list[str]] = {}
    for k in r.keys():
        d[k] = list(v.ciudad_destino for v in sorted(r[k],key=lambda v:v.duracion.total_seconds(),reverse=True)[0:n]) 
    return d    

#8. Dada una fecha f devuelve el precio medio de los vuelos con salida posterior
# a f. Si no hubiera vuelos devuelve 0.0

def precio_medio_posterior(f:datetime)->float:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    s = 0.
    n = 0
    for v in ls:
        if v.fecha > f:
            s += v.vuelo_programado.precio
            n += 1
    if n == 0:
        return 0.0
    return s/n
            

#9. Devuelve un Map que haga corresponder a cada destino un conjunto con las
# fechas de los vuelos a ese destino.

 
def fechas_a_destino()->dict[str,set[date]]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    r: dict[str,set[date]] = {}
    for v in ls:
        key = v.vuelo_programado.ciudad_destino
        if key in r.keys():
            r[key].add(v.fecha_salida)
        else:
            r[key] = {v.fecha_salida}
    return r
    

#10. Devuelve el destino con mayor numero de vuelos

def destino_con_mas_vuelos()->tuple[str,int]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    r: dict[str,list[VueloProgramado]] = {}
    for v in ls:
        key = v.vuelo_programado.ciudad_destino
        if key in r.keys():
            r[key].append(v.vuelo_programado)
        else:
            r[key] = [v.vuelo_programado]
    d = None
    n = None
    for k,lv in r.items():
        if d is None or len(lv) > n:
            d,n=k,len(lv) 
    if d is None or n is None:
        raise ValueError("No hay vuelos")
    return (d,n)

#11. Dado un entero m devuelve un conjunto ordenado con las duraciones 
# de todos los vuelos cuya duracion es mayor que m minutos.


def duraciones(m:int)->SortedSet[int]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    r = []
    for v in ls:
        if v.vuelo_programado.duracion.total_seconds()/60 > m:
            r.append(int(v.vuelo_programado.duracion.total_seconds()/60))
    return SortedSet(sorted(r,reverse=True))
    

#12. Dado un numero n devuelve un conjunto con los destinos de los vuelos de los vuelos con mayor duracion


def destinos_mayor_duracion(n:int)->set[str]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    r = sorted(ls,key=lambda v:v.vuelo_programado.duracion.total_seconds(), reverse=True)[0:n]
    s = []
    for v in r:
        s.append(v.vuelo_programado.ciudad_destino)
    return set(s)

#13. Dado un numero n devuelve un conjunto con los n destinos con mas vuelos

 
def con_mas_vuelos(n:int)->list[tuple[str,int]]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    r: dict[str,list[VueloProgramado]] = {}
    for v in ls:
        key = v.vuelo_programado.ciudad_destino
        if key in r.keys():
            r[key].append(v.vuelo_programado)
        else:
            r[key] = [v.vuelo_programado]
    s:list[tuple[str,int]] = []
    for k,lv in r.items():
        s.append((k,len(lv)))
    return sorted(s,key=lambda x:x[1], reverse=True)[0:n]
        

# 14. Dado un numero entero n devuelve una __ocupaciones_vuelos con los destinos que tienen mas de n vuelos
    

def mas_de_n_vuelos(n:int)->list[str]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    r: dict[str,list[VueloProgramado]] = {}
    for v in ls:
        key = v.vuelo_programado.ciudad_destino
        if key in r.keys():
            r[key].append(v.vuelo_programado)
        else:
            r[key] = [v.vuelo_programado]
    t:list[tuple[str,list[VueloProgramado]]] = sorted(r.items(),key=lambda x:len(x[1]), reverse=True)
    s:list[str] = []
    for i in range(0,n):
        s.append(t[i][0])
    return s

# 15. Devuelve un Map que relacion cada destino con el porcentaje de los vuelos del total que van a ese destino.


def porcentaje_a_destino()->dict[str,float]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    n = len(ls)
    r: dict[str,list[VueloProgramado]] = {}
    for v in ls:
        key = v.vuelo_programado.ciudad_destino
        if key in r.keys():
            r[key].append(v.vuelo_programado)
        else:
            r[key] = [v.vuelo_programado]
    s:dict[str,float] = {}
    for k,lv in r.items():
            s[k]= len(lv)/n
    return s


# 16. Devuelve un Map que haga corresponder a cada ciudad destino el vuelo de mas barato

def min_precio(lv:list[VueloProgramado])->VueloProgramado:   
    vm:VueloProgramado = lv[0]
    p = vm.precio
    for v in lv:
        if vm.precio < p:
            vm, p = v,v.precio
    return vm
    
def mas_barato()->dict[str,VueloProgramado]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    r: dict[str,list[VueloProgramado]] = {}
    for v in ls:
        key = v.vuelo_programado.ciudad_destino
        if key in r.keys():
            r[key].append(v.vuelo_programado)
        else:
            r[key] = [v.vuelo_programado]
    s:dict[str,VueloProgramado] = {}
    for k,lv in r.items():
            s[k]= min_precio(lv)
    return s

# 17. Devuelve un Map que haga corresponder a cada destino el numero de fechas
# distintas en las que hay vuelos a ese destino.


def fechasDistintas()->dict[str,int]:
    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    r: dict[str,set[date]] = {}
    for v in ls:
        key = v.vuelo_programado.ciudad_destino
        if key in r.keys():
            r[key].add(v.fecha_salida)
        else:
            r[key] = {v.fecha_salida}
    s:dict[str,int] = {}
    for k,lv in r.items():
            s[k]= len(lv)
    return s


# 18 Diseñar un método que obtenga el nombre de la ciudad donde está ubicado el aeropuerto con 
# la mayor facturación entre dos fechas dadas a y b. Se entiende por facturación la suma 
# de los precios de los billetes de un conjunto de vuelos. Las fechas a y b, de tipo fecha y hora, 
# deben estar una antes que la otra y tener más de un día de diferencia, 
# en otro caso se disparará una excepción

def ciudad_con_mayor_facturacion(a:datetime,b:datetime)->str:
    if b <= a or (b - a).days <= 1:
        raise ValueError("Dates are not valid. 'b' should be later than 'a' and they should be more than one day apart.")

    ls: list[Vuelo] = Espacio_aereo.of().vuelos.todos
    facturacion: dict[str, float] = {}

    for v in ls:
        if a <= v.fecha <= b:
            ciudad = v.vuelo_programado.ciudad_destino
            precio = v.vuelo_programado.precio
            if ciudad in facturacion:
                facturacion[ciudad] += precio
            else:
                facturacion[ciudad] = precio

    ciudad_mayor_facturacion:str = max(facturacion.keys(),key=lambda k:facturacion[k])
    return ciudad_mayor_facturacion


if __name__ == '__main__':
    print(ciudad_con_mayor_facturacion(datetime(2020, 1, 1), datetime(2020, 12, 31)))                                                         
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
    print(str_dict(fechasDistintas())) 
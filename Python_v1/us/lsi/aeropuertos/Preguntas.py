'''
Created on 21 ago 2022

@author: migueltoro
'''

from datetime import date,datetime,timedelta
from collections import OrderedDict
from ordered_set import OrderedSet
from us.lsi.aeropuertos.Vuelo import Vuelo

#1. Dada una cadena de caracteres s devuelve el número total de pasajeros a
# ciudades destino que tienen
# como prefijo s (esto es, comienzan por s).  ç
 
def numero_depasajeros(self,prefix:str)->int:
    pass

#2.  Dado un conjunto de ciudades destino s y una fecha f devuelve cierto si
# existe un vuelo en la fecha f con destino en s.

 
def hay_destino(destinos:set[str], f:date)-> bool:
    pass


#3. Dada una fecha f devuelve el conjunto de ciudades destino diferentes de todos
# los vuelos de fecha f

 
def destinosDiferentes(f:date)->set[str]:
    pass

#4. Dado un anyo devuelve un OrderedDict que relacione cada destino con el
# total de pasajeros a ese destino en el año anyo


def total_pasajeros_a_destino(a:int)->OrderedDict[str,int]:
    pass

#5. Dado un destino devuelve el código de la aerolinea del primer vuelo con plazas libres a ese
# destino


def primer_vuelo(destino:str)->str:
    pass

#6. Devuelve para los vuelos completos un Map que haga corresponder a cada ciudad
# destino la media de los precios de los vuelos a ese destino.


def precios_medios()->dict[str,float]:
    pass

#7. Devuelve un Map tal que dado un entero n haga corresponder
# a cada fecha la lista de los n destinos con los vuelos de mayor duración.


def destinos_con_mayor_duracion(n:int)->dict[date,list[str]]:
    pass

#8. Dada una fecha f devuelve el precio medio de los vuelos con salida posterior
# a f. Si no hubiera vuelos devuelve 0.0

def precio_medio(f:datetime)->float:
    pass

#9. Devuelve un Map que haga corresponder a cada destino un conjunto con las
# fechas de los vuelos a ese destino.

 
def fechas_a_destino()->dict[str,set[date]]:
    pass

#10. Devuelve el destino con mayor número de vuelos

def destino_con_mas_vuelos()->str:
    pass

#11. Dado un entero m devuelve un conjunto ordenado con las duraciones 
# de todos los vuelos cuya duración es mayor que m minutos.


def duraciones(m:int)->OrderedSet[timedelta]:
    pass

#12. Dado un número n devuelve un conjunto con los destinos de los vuelos que están entre los n que más duración tienen.


def destinos_mayor_duracion(n:int)->set[str]:
    pass

#13. Dado un número n devuelve un conjunto con los n destinos con más vuelos

 
def entreLosMasVuelos(n:int)->set[str]:
    pass

# 14. Dado un número entero n devuelve una lista con los destinos que tienen más de n vuelos


def mas_de_n_vuelos(n:int)->list[str]:
    pass

# 15. Devuelve un Map que relación cada destino con el porcentaje de los vuelos del total que van a ese destino.


def porcentaje_a_destino()->dict[str,float]:
    pass


def porcentaje_a_destino_ocupaciones_vuelos()->dict[str,float]:
    pass

# 16. Devuelve un Map que haga corresponder a cada ciudad destino el vuelo de más barato


def mas_barato()->dict[str,Vuelo]:
    pass

# 17. Devuelve un Map que haga corresponder a cada destino el número de fechas
# distintas en las que hay vuelos a ese destino.


def fechasDistintas()->dict[str,int]:
    pass

if __name__ == '__main__':
    pass
# Aeropuertos

Se dispone de los datos de aeropuertos en el fichero _aeropuertos.csv_. Cada línea contiene, _nombre, pais, codigo, ciudad_. Las líneas son de la forma

```
Tirana Airport,Albania,TIA,Tirana
Berlín Brandeburgo Airport,Alemania,BER,Berlin
Bremen Airport,Alemania,BRE,Bremen
Colonia Bonn Airport,Alemania,CGN,Colonia
```

De aerolíneas dispones del fichero _aerolíneas.csv_. En cada línea podemos obtener el código y nombre de la aerolínea en la forma

```
AA,American Airlines
CO,Continental Airlines,Inc.
DL,Delta Airlines Inc.
N7,National Airlines Inc.
```

El  fichero _vuelosProgramados.csv_ contiene en cada línea el _codigoAerolinea, numero, codigoDestino, codigoOrigen, precio, numPlazas, duracion, hora, diaSemana_. Las líneas son de la forma
```
TP,0705,BER,KTW,294,21,170,287,14:50,FRIDAY
FS,0596,TZX,AAR,761,64,49,45,07:54,THURSDAY
FJ,0612,BHD,TPS,113,98,128,180,16:41,MONDAY
CX,0930,LJU,NCL,741,17,11,159,02:40,WEDNESDAY
```
El fichero _vuelos.csv_ contiene en cada línea _codigoVuelo, fecha, numPasajeros_ de la forma

```
NH0818,2020-04-13 16:43:00,7
PE0174,2020-11-17 09:03:00,89
5Z0373,2020-05-16 01:46:00,64
7F0434,2020-10-01 03:24:00,94
```
Queremos diseñar un programa que pueda llevar a cabo entre otros posibles los cálculos sobre los vuelos como los siguientes:

1.	Si existe un vuelo en una fecha dada Dado a un conjunto de destinos dado 
2.	Encontrar los destinos en una fecha dada
3.	Encontrar el número total de pasajeros de los destinos que tienen un prefijo dado
4.	Encontrar una relación ordenada de destinos con su número de pasajeros de llegada en un año dado. 
5.	Dado un destino encontrar el código del primer vuelo con plazas libres a ese destino.
6.	Encontrar el destino con mayor número de vuelos de entrada y salida
7.	Encontrar una relación que asocie a cada fecha la lista de los destinos de los n vuelos de la mayor duración 
8.	Obtener un conjunto ordenado con las duraciones de todos los vuelos cuya duración es mayor que un número de minutos dado
9.	Dada una fecha f encontrar el precio medio de los vuelos con salida posterior a f. Si no hubiera vuelos devuelve 0.0
10.	Obtener un conjunto con los n destinos de los vuelos con mayor duración.
11.	Obtener una relación de los destinos junto a la media de los precios de los vuelos a ese destino. 
12.	Obtener una relación de destinos junto con las fechas de los vuelos a ese destino. 
13.	Obtener los n destinos que con más vuelos 
14.	Obtener los destinos que tienen más de n vuelos 
15.	Obtener una relación de destinos junto con el porcentaje de vuelos que van a ese destino.
16.	Obtener una relación de destinos junto con el vuelo más barato a ese destino.
17.	Obtener una relación de destinos junto a las fechas posibles a ese destino.


Los tipos que vamos a necesitar son:

Tipos:

## Aeropuerto

Propiedades:  Inmutable

- Codigo: Hilera de caracteres, básica, se compone de tres caracteres, Identifica el aeropuerto de manera única
- Ciudad: Hilera de caracteres, básica
- Pais: Hilera de caracteres, básica
- Nombre: Hilera de caracteres, básica

Representación:
- Codigo, Ciudad, País, Nombre

Igualdad: Si tienen el mismo código. Aunque con la restricción impuesta al código todas las propiedades básicas serán iguales.

Métodos de Factoría:

- parse(text:String): Aeropuerto
- of(Codigo: String,Ciudad: String,Pais: String,Nombre: String): Aeropuerto

## Aeropuertos

Es un tipo que representa una población de aeropuertos. Una población de objetos es un conjunto de objetos de un tipo donde cada uno tiene un identificador distinto de los demás. En este caso el identificador es la propiedad código del aeropuerto. Tiene otros métodos específicos para cada población.

Una forma de diseño de una población es con factoría de tipo _singleton_ que explicaremos abajo. El tipo tiene, además, métodos para recuperar objetos dado un identificador.

Propiedades:

- Aeropuerto aeropuerto(String codigo)
- Aeropuerto get(Integer i)
- String ciudadDeAeropuerto(String codigo)
- Set\<Aeropuerto\> aeropuertosEnCiudad(String ciudad)
- Integer size()
- Set\<Aeropuerto\> todos()

Operaciones:

- void addAeropuerto(Aeropuerto a), Añade un aeropuerto
- void removeAeropuerto(Aeropuerto a), Elimina un aeropuerto

Representación:

- Lista de aeropuertos uno por línea

Métodos de Factoría:

La factoría devuelve siempre el objeto _gestorAeropuertos_ actualizándolo primero si es null.

```java
private static Aeropuertos gestorAeropuertos = null;
public static Aeropuertos of() {
	if(Aeropuertos.gestorAeropuertos == null)
		Aeropuertos.gestorAeropuertos = 
			Aeropuertos.of("ficheros_aeropuertos/aeropuertos.csv");
	return gestorAeropuertos;
}

public static Aeropuertos of(String fichero) {
	Set<Aeropuerto> aeropuertos = File2.streamDeFichero(fichero,"Windows-1252")
		.map(x -> Aeropuerto.parse(x))
		.collect(Collectors.toSet());
	Aeropuertos.gestorAeropuertos = new Aeropuertos(aeropuertos);
	return Aeropuertos.gestorAeropuertos;
}
```

Invariante

- los códigos de los aeropuertos deben ser diferentes

## Aerolínea

Propiedades:  Inmutable

- Código: String, básica, se compone de dos caracteres, Identifica el aeropuerto de manera única
- Nombre: String

Representación:

- Codigo, Nombre

Igualdad: Si tienen el mismo código. Aunque con la restricción impuesta al código todas las propiedades básicas serán iguales

Métodos de Factoría:

- parse(text:String): Aerolinea
- of(Codigo: String,Nombre: String): Aerolinea

## Aerolíneas

Es un tipo que representa una población de aerolíneas. Una población de objetos es un conjunto de objetos de un tipo donde cada uno tiene un identificador distinto de los demás. En este caso el identificador es la propiedad código de la aerolínea. Tiene otros métodos específicos para cada población.

Propiedades:

 - Aerolinea aerolinea(String codigo), básica
 - Aerolinea get(Integer i)
 - Set\<Aerolinea\> todas())
 - size(): Integer, derivada

Operaciones

- void addAerolinea(Aerolinea a), Añade una aerolinea
- void removeAerolinea(Aerolinea a), Elimina una aerolinea

Representación:

- Lista de aerolíneas una por línea

Métodos de Factoría:

 - Aerolineas of()
 - Aerolineas of(String fichero)

Invariante

- los códigos de los aeropuertos deben ser diferentes

## VueloProgramado

Propiedades: Inmutable

- CódigoAerolinea: String, básica
- Numero: String, básica, cuatro caracteres que representan un número de vuelo de una aerolinea
- CodigoDestino: String, básica, código del aeropuerto destino
- CodigoOrigen: String, básica, código del aeropuerto origen
- Precio: Integer, básica, debe ser mayor que cero
- NumPlazas: Integer, básica, debe ser mayor que cero	
- Duración: Duration, básica, duración del vuelo
- Hora: LocalTime, básica,
- DiaSemana, DayOfWeek, básica
- CiudadDestino, String, derivada
- CiudadOrigen, String, derivada
- Codigo, String, derivada, identifica de manera única un vuelo y se compone de la concatenación del CodigoAerolinea y el Numero.

Representación:

- Codigo,Nombre

Igualdad: Si tienen el mismo código. Aunque con la restricción impuesta al código todas las propiedades básicas serán iguales

Métodos de Factoría:

- parse(text:String): Vuelo
- of(Codigo: String,Nombre: String): Aerolínea
- random(): Vuelo, un vuelo construido aleatoriamente con los aeropuertos y las aerolíneas disponibles. 

## VuelosProgramados

Es un tipo que representa una población de vuelos. Una población de objetos es un conjunto de objetos de un tipo donde cada uno tiene un identificador distinto de los demás. En este caso el identificador es la propiedad código del vuelo que es una propiedad derivada. Tiene otros métodos específicos para cada población.

Propiedades:

- Set\<Vuelo\> todos()
- Vuelo vuelo(String codigo) 
- Vuelo get(Integer index)
- Integer size() 

Operaciones:

- void addVuelo(Vuelo v), Añade un vuelo
- void removeVuelo(Vuelo v), Elimina un vuelo

Representación:

-  Lista de vuelos un por línea

Métodos de Factoría:

 - Vuelos of()
 - Vuelos of(String fichero)

Invariante

- los códigos de los aeropuertos deben ser diferentes

## Vuelo

Propiedades: Inmutable

- CódigoVuelo: String, básica
- Fecha: LocalDateTime, básica, fecha-hora de salida
- NumPasajeros: Integer, básica, debe ser mayor o igual a cero
- Vuelo: Vuelo, derivada
- Llegada: LocalDateTime, fecha-hora de llegada
- FechaSalida: LocalDate, fecha de salida
- HoraSalida: LocalTime, hora de salida

Representación:

- CodigoVuelo, FechaSalida, HoraSalida

Igualdad: Si tienen el mismo código. Aunque con la restricción impuesta al código todas las propiedades básicas serán iguales

Métodos de Factoría:

- parse(text:String): Vuelo
- of(Codigo: String,Nombre: String): Aerolínea
- random(): Vuelo, un vuelo construido aleatoriamente con los aeropuertos y las aerolíneas disponibles. 

## Vuelos

Es un tipo que representa una población de ocupacionVuelo. Una población de objetos es un conjunto de objetos de un tipo donde cada uno tiene un identificador distinto de los demás. En este caso el identificador es el par código del vuelo, fecha que es una propiedad derivada. Tiene otros métodos específicos para cada población.

Propiedades:

- Set\<OcupacionVuelo\> todos())
- OcupacionVuelo ocupacionVuelo(String codigoVuelo, LocalDateTime fecha) 
- OcupacionVuelo get(Integer index)
- Integer size() 

Operaciones:

- void addOcupacionVuelo(OcupacionVuelo oc), Añade una ocupación de un vuelo
- void removeOcupacionVuelo(OcupacionVuelo oc), Elimina una ocupación de un vuelo

Representación:

-  Lista de ocupaciones una por línea

Métodos de Factoría:

 - OcupacionesVuelos of()
 - OcupacionesVuelos of(String fichero)

Invariante


- los códigos de los aeropuertos deben ser diferentes





# Sevici

Se dispone de los datos de las estaciones de la red de _Sevici_._ Los datos se encuentran en un fichero CSV. Cada línea del fichero contiene seis datos:

- Nombre de la estación
- Número total de bornetas de la estación
- Número de bornetas vacías
- Número de bicicletas disponibles
- Latitud
- Longitud

Los datos dependen del instante en que se obtiene el fichero, ya que el número de bicicletas y bornetas libres varía de forma continua. Estan serían, por ejemplo, las primeras líneas del fichero en un momento dado:

```
name,slots,empty_slots,free_bikes,latitude,longitude
149_CALLE ARROYO,20,11,9,37.397829929383,-5.97567172039552
257_TORRES ALBARRACIN,20,16,4,37.38376948792722,-5.908921914235877
243_GLORIETA DEL PRIMERO DE MAYO,15,6,9,37.380439481169994,-5.953481197462
109_AVENIDA SAN FRANCISCO JAVIER,15,1,14,37.37988413609134,-5.974382770011
073_PLAZA SAN AGUSTIN,15,10,4,37.38951386231434,-5.984362789545622
```
Los principales aspectos que tendremos que resolver a la hora de procesar estos datos de entrada serán saltar la línea de encabezado del fichero, separar adecuadamente los campos mediante las comas e interpretar el formato de cada uno de los campos, que puede ser de tipo cadena, entero o real.

Tipos:

## Estación:

Propiedades:

- Numero: Integer;
- Name: String
- Slots: Integer;
- Empty_Slots: Integer;
- Free:Bykes; Integer,
- Ubicacion: Coordenadas2D;

Métodos de factoría:

- parse(String linea): Estacion

## Red:

Propiedades:

- Estaciones: Set\<Estacion\>, básica
- Numero: Integer, derivada
- Estacion(String nombre): Set\<Estacion\>, derivada
- Estacion(Integer index): Estacion, derivada
- EstacionesConBicisDisponibles: Set\<Estacion\>, derivada
- EstacionesConBicisDisponibles(Integer n): Set\<Estacion\>, derivada
- Ubicaciones: Set\<Coordenadas2D\>
- UbicacionEstacionesDisponibles(Integer k)
- EstacionMasBicisDisponibles: Estacion, derivada
- EstacionesPorBicisDisponbles: Map\<Integer,List\<Estacion\>\>, derivada
- NumeroDeEstacionesPorBicisDisponibles: Map\<Integer,Integer\>, derivada

Operaciones:

- void add(Estacion e)
- void remove(Estacion e)

Métodos de factoría

- parse(String fichero): Red 
- of(Set\<Estacion\> marcas): Red

Invariante

- Dos estaciones no pueden tener el misno número
# Ruta

El formato de entrada con el que trabajaremos contempla una línea por cada punto del trayecto que incluye cuatro informaciones:

- tiempo en el que fue tomada la medición
- latitud del punto en el que fue tomada la medición
- longitud del punto en el que fue tomada la medición
- altitud del punto en el que fue tomada la medición

He aquí un fragmento de dicho fichero con las cinco primeras líneas:

```
00:00:00,36.74991256557405,-5.147951105609536,712.2000122070312
00:00:30,36.75008556805551,-5.148005923256278,712.7999877929688
00:01:30,36.75017642788589,-5.148165263235569,714.0  
00:02:04,36.750248931348324,-5.148243047297001,714.599975585937
00:02:19,36.750430315732956,-5.148255117237568,715.0
```
Distancia a lo largo de la superficie de la tierra según la fórmula de _Harvesine_:

 # a = sin^2(inclat/2) + cos(lat1) * cos(lat2) * sin^2(inclong/2)
 # d = R * 2 * atan2(sqrt(a),sqrt(1-a))

$$a=\sin^2 (\Delta \phi /2)+\cos(\alpha_1)*\cos(\alpha_2)*\sin^2 (\Delta \lambda /2)$$

$$ d= 2 \ R \ \arctan 2(a,\sqrt{1-a}) $$

Donde  $\alpha_1,\alpha_2$  son las las latitudes de los puntos, $\Delta  \alpha$ la diferencia de latitudes y $\Delta \lambda$ la diferencia de longitudes

## Coordenadas2D

Propiedades:

 - Double latitud() 
 - Double longitud()
 - Double distancia(Coordenadas2D c), distancia Harvesine
 - Double toRadianes()
 - Centro(List\<Coordenadas2D\> ls), Compartida

Representación: (2.3,0.5)

## Coordenadas3D:

Propiedades:

- Double latitud()
- Double longitud()
- Double altitud()
- Coordenadas2D to2D() 
- Double Distancia(Coordenadas3D c):, distancia en tres dimensiones

Representación: (2.3,0.5,7.9)

## Marca:

Propiedades:

- LocalTime tiempo()
- Double latitud()
- Double longitud()
- Double altitud()

Representación: (00:00:30,2.3,0.5,7.9)

Método de factoría

- parse("00:00:30,2.3,0.5,7.9)

## Intervalo:

enum Type {Llano, Ascendente, Descendente}

Propiedades:

- Marca principio()
- Marca fin()
- Double desnivel:(), km
- Double velocidad(), km/hora
- Double longitud(), km
- Double tiempo(), horas
- Type type()

Representación: ((00:00:30,2.3,0.5,7.9), (00:00:35,2.4,0.6,8.1))

## Ruta:

Propiedades:

- List\<Marca\> marcas()
- Double tiempo() 
- Double longitud()
- Double velocidad()
- Double velocidadEnIntervalo(Integer i)
- Double desnivelCrecienteAcumulado();
- Double desnivelDecrecienteAcumulado();
- Map\<Type,Integer\> frecuencias();
- Set\<Intervalo\> llanos();
- Integer numMarcas();

Representación: {(00:00:30,2.3,0.5,7.9), …, (00:00:35,2.4,0.6,8.1)}

Método de factoría:
 
 - Ruta of(String fichero)

Implementación

Se diseñará un clase abstracta _RutaA_ con los métodos comunes a las clases _RutaI_ y _RutaF_. Estas últimas clases, que heredarán de _RutaA_ tendrán el código imperativo y el funcional respectivamente. _RutaA_  implementará el interfaz _Ruta_.


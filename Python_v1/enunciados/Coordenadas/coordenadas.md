# Coordenadas2D

Tipo Inmutable

Propiedades

- latitud: float, en grados, básica
- longitud: float, en grados, básica
- copy: Coordenadas2D, derivada

Métodos individuales

- distancia(c): float, la distancia en kilómetros dese del objeto actual a c usando las fórmulas de abajo
- es_cercana(c:Coordenadas2D, d:float): bool, si c esta a una distancia de c más pequeña que d

Métodos compartidos

- distancia(c1,c2): float, la distancia en kilómetros de c1 a c2 usando las fórmuals de abajo
- center(coordenadas:list[Coordenadas2D]): Coordenadas2D, centro de las coordenadas en los parámetros

Métodos de factoría

- of(latitud:float,longitud:float): Coordenadas2D, con latitud y longitud en grados
- parse(text:str): Coordenadas2D, con el texto en el formato '(37.3828300, -5.9731700)'

Representación

- En la forma (37.3828300, -5.9731700)

Explicación

- Sea $\phi$ la latitud en radianes y $\lambda$ longitud en radianes.
- Sea $\phi_1, \phi_2$ la latitud en radianes de los puntos 1 y dos y $\lambda_1, \lambda_2$ longitud en radianes.
- Sea $\Delta \phi = \phi_2 - \phi_1, \Delta \lambda = \lambda_2 - \lambda_1$
- Sea *R* el radio de la tierra en kilómetros
- Sea 
	$a = \sin^2(\frac{\Delta \phi}{2}) +\cos(\phi_1) \cos(\phi_2) \sin^2(\frac{\Delta \lambda}{2})$
- Sea 
	$d = 2\ R\ atan2(\sqrt{a},\sqrt{1-a})$

# Coordenadas3D

Tipo Inmutable

Propiedades

- latitud: float, en grados, básica
- longitud: float, en grados, básica
- altura, float, en kilómetros, básica
- copy: Coordenadas3D, derivada
- to2D: Coordenadas2D, derivada, las coordenadas 2D asociadas

Métodos individuales

- distancia(c): float, la distancia en kilómetros desde del objeto actual a c usando las fórmualas de abajo
- es_cercana(c:Coordenadas2D, d:float): bool, si c esta a una distancia de c más pequeña que d

Métodos compartidos

- distancia(c1,c2): float, la distancia en kilómetros de c1 a c2 usando las fórmulas de abajo
- center(coordenadas:list[Coordenadas3D]): Coordenadas3D, centro de las coordenadas en los parámetros

Métodos de factoría

- of(latitud:float,longitud:float,altura:floal): Coordenadas3D, con latitud, longitud en grados y altura en kilómetros, la altura debe ser positiva.
- parse(text:str): Coordenadas2D, con el texto en el formato '(37.3828300, -5.9731700, 0.7122)'

Representación

- En la forma (37.3828300, -5.9731700, 0.7122)

Explicación

Sea 

- c21 = c1.to2D
- c22 = c2.to2D
- d2 = c21.distancia(c22)
- $d = \sqrt{{(c1.altitud-c2.altitud)}^2 + d2^2}$
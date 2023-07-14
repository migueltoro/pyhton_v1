# Poker

En este ejercicio usaremos el método de Montecarlo para estimar la probabilidad de victoria de una determinada mano de póker-  El póker es un juego de cartas de apuestas, en el que el jugador que tiene la mejor combinación de cartas gana toda la cantidad apostada en una mano-  Tiene elementos de muchos juegos antiguos pero su expansión, con reglas parecidas a las que se usan hoy en día, tuvo lugar desde Nueva Orleans en el siglo XIX-  

Se juega con la denominada baraja inglesa que tiene trece cartas de cuatro palos distintos-  Las trece cartas ordenadas de menor a mayor según su valor son: 
```
['2','3','4','5','6','7','8','9','10','J','Q','K','A'] 
```

Hay cuatro palos: Tréboles ( T) , Corazones (C) , Picas (P), Diamantes (D)

## Tipos

### Valor: 
```
- enum [V2,V3,V4,V5,V6,V7,V8,V9,V10,VJ,VQ,VK,VA] 
```
## Palo: 
```
enum [T,C,P,D] 
```

## Jugada: 

Es un entero que representa el tipo de jugada

```
nombres_jugadas: list[str] =  ['EscaleraReal','EscaleraDeColor','Poker','Full','Color', 
    'Escalera','Trio','DoblePareja','Pareja','CartaMasAlta']
```
## Carta:

Propiedades:

- Valor: Integer en [0,13), básica, ordenadas de mayor a menor valor
- Palo: Integer en [0,4), básica
- Id: Integer en [0,53), derivada, id = palo*4+valor
- NombresDeValores: List\<String\>, compartida 
- NombresDePalos: List\<Character\>, compartida


Factoria

-  Dado el id
-  Dado valor y palo
-  Dada su representacion textual
Orden natural: por valor

## Mano:

Propiedades:

-  Cartas: List\<Carta\>, tamano numeroDeCartas, ordenadas por valor
-  NumeroDeCartas, Integer, compartida, 5
-  Son5ValoresConsecutivos: Boolean, derivada
-  FrecuenciasDeValores: Map\<Integer,Integer\>, derivada
-  ValoresOrdenadosPorFrecuencias(): List\<Integer\>, de mayor a menor
-  ValorMasFrecuente: Integer, derivada, el valor que mas se repite
-  FrecuenciasDePalos: Map\<Integer,Integer\>,
-  PalosOrdenadosPorFrecuencias: List\<Integer\>, de mayor a menor
-  EsColor: Boolean, derivada
-  EsEscalera: Boolean, derivada
-  EsPoker: Boolean, derivada
-  EsEscaleraDeColor: Boolean, derivada
-  EsFull: Boolean, derivada
-  EsTrio, Boolean, derivada
-  EsDoblePareja: Boolean, derivada
-  EsPareja:Boolean, derivada
-  EsEscaleraReal:Boolean, derivada
-  EsMano:Boolean, , derivada
-  Jugada:Jugada, derivada
-  Fuerza: Double, derivada, la probabilidad de ganar a un mano aleatoria

Representacion: Representacion de las cartas entre parentesis y separadas por comas

Factoria:

-  Random, selecciona 5 cartas sin repeticion al azar
-  Dada un Set\<Carta\> de tamano 5
-  Dada la representacion textual de una mano

Orden Natural: Por tipo de jugada y si es la misma por el valor que mas se repite
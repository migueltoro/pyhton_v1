# Diseño de tipos

Antes de codificar es conveniente diseñar los tipos que usaremos en nuestro código. El diseño de un tipo es como un plano del mismo. En él se indica sus propiedades más relevantes y los mecanismos para crear valores de ese tipo. En la programación orientada a objetos los valores del tipo los llamaremos objetos.

Un tipo es un conjunto de valores, cada uno de esos valores tiene un conjunto de propiedades, adicionalmente un conjunto de operaciones para modificar el valor de las propiedades y mecanismos de factoría para crear los valores del tipo. Cada propiedad tiene un identificador y un tipo del conjunto de tipos previamente existente. Los valores de las propiedades pueden estar restringidos por expresiones lógicas que se indican en el _invariante_ del tipo.

Cada tipo tiene asociado una _dominio del tipo_. Este incluye el conjunto de todos los valores posibles del tipo. Este conjunto de valores se define por comprensión: el conjunto de valores que cumplen el invariante. 

Llamaremos _población de un tipo_ a un conjunto de finito de valores del tipo creado específicamente para un fin. En muchos casos el conjunto de valores será leído de un fichero o construido añadiendo objetos al conjunto. 

Un tipo puede ser inmutable, si no se pueden modificar sus propiedades una vez creado el valor, o mutables si se pueden cambiar. 

Un tipo puede _extender_ a otro (diremos que hereda de o extiende a otro)

Cada propiedad puede ser:

- *Básica*: si su valor no depende del valor de otra propiedad
- *Derivada*: si su valor depende del valor de otras propiedades
- *Individual*: Si el valor de la propiedad es específico de cada valor del tipo
- *Compartida*: Si el valor de la propiedad es compartido por todos los valores del tipo

Las propiedades no pueden cambiar el valor de otras propiedades. Las propiedades pueden tener parámetros para indicar un conjunto de propiedades del mismo tipo. En ese caso podemos indicar el rango permitido para los parámetros. Tambien pueden tener restricciones sobre el conjunto de valores que pueden tomar.
LaLas *operaciones* indican la manera de modificar las propiedades del tipo. Si un tipo no tiene operaciones es inmutable. Las operaciones pueden tener parámetros de entrada y restricciones. Restricciones en los parámetros de entrada que especificamos por un predicado que llamamos *precondición* (@pre p(x)). Restricciones entre los valores de los parámetros de entrada y el valor de las propiedades tras aplicar la operación que especificamos por un predicado llamamos *postcondición* (@post p(x,v)).
LaLas factorías son mecanismos para construir valores de un tipo. Generalmente usaremos los siguientes:

- *of(propiedades)*: Crea un valor del tipo a partir de algunas propiedades del mismo
- *of()*: Crea un valor por defecto del tipo
- *parse(texto)*: Crea un valor del tipo a partir de una cadena de caracteres

- *Representación* es el mecanismo para convertir un valor del tipo en una cadena de caracteres que pueda ser presentada en la consola o grabada en un fichero.

- *Igualdad*: Es una expresión booleana que indica cuando dos valores del tipo son iguales. Por defecto dos valores son iguales si tienen las propiedades básicas iguales.

- *Orden natural*: En algunos tipos se puede definir un orden total sobre los valores del tipo que llamaremos orden natural.

- *Restricciones*: Son predicados que deben cumplir los valores de un tipo o el conjunto de valores de la población de un tipo. Aqui podemos acumular las restricciones de las propiedades y de las operaciones de un tipo. Al conjunto de restricciones también se le suele llamar *Invariante*.


## Diseño de poblaciones

La población de un tipo *E* es un  nuevo tipo *P* cuyos valores son conjuntos de valores del tipo *E* anterior. En este conjunto suele existir una o varias propiedades que identifican de manera única a cada valor del tipo *E* en la población.

Las factorías de las poblaciones las diseñaremos generalmente son el patrón de diseño *singleton*. Este es un mecanismo de factoría que nos permite obtener siempre el mismo valor en las sucesivas llamadas a la factoría. Las poblaciones suelen tener mecanismos para leer los valores de un fichero o de la red en general.

## Implementación

Los tipos se pueden implementar usando una *class* o el mecanismo de *dataclass*. El mecanismo de *dataclass* se usa para tipos inmutables y la *class* para tipos mutables aunque también se puede usar para tipos inmutables.

### dataclass

El mecanismo de *dataclass* sirve para implmentar tipos que pueden estar dotados de orden natural y ser inmutables. El mecanismo nos proporciona:

- un constructor definido automáticamente
- una igualdad y un hashcode definidos automáticmente
- una representación definida automáticamente

De manera sencilla se puede especificar si el tipo es inmutable y si tiene orden natural. Esto se consegue dando valores a los parámetros frozen y order.

```
@dataclass(frozen=True,order=True)
class Persona:
	apellidos: str
	nombre: str
	dni: str
	fecha_de_nacimiento: datetime
	telefono: str
	direccion:Direccion
	...
```
El tipo Persona anterior es inmutable, *frozen=True* y tiene orden natural *order=True*.
Las propiedades básicas son las indicadas después de la línea *class Persona*.
La igualdad viene definida por la igualdad de las propidades básicas
Si tiene orden natural este se establece comparando las propidades básicas por el orden establecido
El constructor Persona(...) viene definido, aunque sólo lo usaremos entro de los métodos de factoría
La representación viene definida aunque se puede sobrescribir diseñando el método

```
def __str__(self)->str:
	...
```

El método *__post_init__* que se al final del constructor puede usarse para acumular comprobación de restricciones.

```
def __post_init__(self):
	assert len(self.apellidos.strip()) > 0, f'Los apellidos no pueden estar en blanco'
	assert len(self.nombre.strip()) > 0, f'El nombre no puede estar en blanco'
	assert self.fecha_de_nacimiento < datetime.now(), f'La fecha debe estar en el pasado'
	assert Persona._check_dni(self.dni), f'El dni no es correcto'
```


### class

La implementación de tipos mediante *class* es más flexible que con dataclass, pero tenemos que implementar más detalles.

Sirve par implementar tipos mutables e inmutables.

En una *class* hay que tener en cuanta atributos y métodos. Estos, a su vez, pueden ser públicos, privados y compartidos. También pueden ser individuales y compartidos.

Los *atributos* son un conjunto de valores que forman el *estado* del objeto. Usualmente los declaramos privados y por eso su ientificador empezará por un subrayado como en *_numerador*. Si empiezan por dos subrayados entonces serán protegidos como en *__numerador*. Si no empiezan por un subrayado entonces serán públicos como en *numerador*. 

Cada clase debe tener un método *__init__*.

```
@total_ordering
class Fraccion:
	
	def __init__(self,n:int,d:int)->None:
		self.__numerador = n
		self.__denominador = d
```

Este método define el constructor, los atributos y los métodos que se usan para construir un objeto. El constructor asociado es *Fraccion(n,d)*.

Junto con el anterior está disponible el método *__post_init__* que se ejecuta detrás del anterior y donde se pueden acumular comprobaciópn d restricciones y normalizaciones de datos:

```
def __post_init__(self)->None:
	assert self.__denominador != 0,f'El denominador no puede ser cero y es {self.__denominador}'
	self.__normaliza()
```

Las propiedades son métodos públicos sin parámetros con la anotación *@property* como en:

```
@property
def numerador(self)->int:
    return self.__numerador
```

Los métodos pueden ser clasificados en observadores y modificadores. Los métodos obervadores no modifican los atributos, los modificadores si y se llaman *operaciones*. Si el tipo no tiene operaciones y sus atributos son privados o pretegidos el tipo es inmutable.

La igualdad se define con el método *__eq__*.

```
def __eq__(self, other)->bool:
	if isinstance(other, Fraccion):
		return self.numerador == other.numerador and self.denominador == other.denominador
    return False
```

El hashcode se cálcula con el método *__hash__*. Un tipo sin este método no puede ser la clace de un diccionario.

```
def __hash__(self)->int:
	return  hash(self.numerador)*31 + hash(self.denominador)
```

El orden natural del tipo se establece con los métodos *__lt__,__eq__*  y la etiqueta *@total_ordering*.

```
def __lt__(self, other)->bool:
	return self.numerador*other.denominador < self.denominador*other.numerador
```
La representación se hace con el método *__str__*.

En Python algunos métodos están predefinidos para que representen operadores. Una lista no completa es:

- __add__(self, other): Define el comportamiento de la suma (+).
- __sub__(self, other): Define el comportamiento de la resta (-).
- __mul__(self, other): Define el comportamiento de la multiplicación (*).
- __truediv__(self, other): Define el comportamiento de la división (/).
- __eq__(self, other): Define el comportamiento de la comparación de igualdad (==).
- __lt__(self, other): Define el comportamiento de la comparación "menor que" (<).
- __getitem__(self, key): Permite acceder a elementos de un objeto como si fuera una estructura de datos, usando corchetes (ej., objeto[key]).
- __setitem__(self, key, value): Permite modificar elementos de un objeto usando corchetes (ej., objeto[key] = value).
- __len__(self): Define el comportamiento del método len() para objetos de la clase.
- __str__(self): Define la representación en cadena del objeto (lo que se muestra al usar str()).
- __repr__(self): Define la representación formal del objeto (lo que se muestra al usar repr()).    

Las poblaciones de un tipo solemos diseñarlas mediante *class* porque usualmente son mutables.

Las factorías de las poblaciones las diseñaremos generalmente son el patrón de diseño *singleton*. Este es un mecanismo de factoría que nos permite obtener siempre el mismo valor en las sucesivas llamadas a la factoría. 

## Ejemplos

[Direccion](https://github.com/migueltoro/pyhton_v1/blob/master/Python_v1/us/lsi/ejemplos_types/Direccion.py)
[Persona](https://github.com/migueltoro/pyhton_v1/blob/master/Python_v1/enunciados/Persona/persona.md)
[Alumno](https://github.com/migueltoro/pyhton_v1/blob/master/Python_v1/enunciados/Persona/persona.md)
[Coordenadas](https://github.com/migueltoro/pyhton_v1/blob/master/Python_v1/enunciados/Coordenadas/coordenadas.md)
[Fracción](https://github.com/migueltoro/pyhton_v1/blob/master/Python_v1/us/lsi/ejemplos_types/Fraccion.py)


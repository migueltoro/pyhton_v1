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
		self.__normaliza()
```

Este método define el constructor, los atributos y los métodos que se usan para construir un objeto. El constructor asociado es *Fraccion(n,d)*.

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

### Persona (inmutable)

Propiedades:

- apellidos, de tipo String, básica. 
- nombre, de tipo String, básica. 
- dni, de tipo String, básica. 
- fechaDeNacimiento, de tipo LocalDateTime, básica. 
- edad, de tipo Integer, derivada. 

Invariante:

- Los apellidos no pueden estar en blanco.
- El nombre no puede estar en blanco.
- El dni debe estar compuesto de 8 números y una letra mayúscula al final, además, esa última letra debe corresponder al número. En la siguiente url puede observar cuál es la metodología que se usa en España para calcular la correspondencia entre número y letra del DNI.
- La fecha/hora de nacimiento debe estar en el pasado.
- La edad es el número de años transcurridos desde la fecha de nacimiento hasta la actualidad

Métodos de factoría: 

- of(String apellidos, String nombre, String dni, LocalDateTime fechaDeNacimiento) Construye un objeto a partir de un valor para cada una de las propiedades básicas del tipo. 
- parse(String text, String patron) Construye un objeto a partir de una cadena de caracteres con la información de las propiedades básicas. La cadena de caracteres tendrá el formato “apellidos,nombre,dni,fecha_de_nacimiento”. El parámetro patrón indica la forma textual de la  fecha de nacimiento.

Rerepresentación como cadena: 

nombre apellidos, de años, nacido el fecha nacimiento a las hora nacimiento.

Por ejemplo Ramiro Casares Amador, de 19, nacido el 14-06-2003 a las 10:02

## Alumno 

Propiedades: extiende a Persona  y es inmutable

- Nota, Double, básica. Indica la nota media de acceso al grado.

Invariante

 La nota debe ser positiva y estar comprendida entre 0 y 14.

Métodos de factoría: 

- of(Persona p, Double Nota): Construye un objeto a partir de una objeto de tipo Persona y una nota.
- parse(String text, String patron): Construye un objeto a partir de una cadena de texto con la información de las propiedades básicas del tipo. El parámetro patrón indica la forma textual de la  fecha de nacimiento.

Representación como cadena: 

La misma representación que el tipo del que hereda añadiéndole además la nota de entrada al grado.
Por ejemplo

## Alumnos

Es un tipo que representa una población de alumnos. Una población de objetos es un conjunto de objetos de un tipo donde cada uno tiene un identificador distinto de los demás. En este caso el identificador es el dni del alumno. Tiene otros métodos específicos para cada población.

Propiedades:

- Alumno alumno(String dni)
- Alumno get(Integer index)
- Integer size()
- Set\<Alumnos\> todos()

Invariante

- $size() == |todos()|$
- $alumno(dni) == a, dni \neq null, \exists \ a \in todos() | a.dni = dni$
- $get(index) == a, 0 \le index \lt size(), a \in todos()$

El invariante se puede escribir en lenguaje formal, como el anterior, o simplemente en lenguaje natural como en el caso del tipo Persona.

Operaciones:

- void addAlumno(Alumno a), Añade un alumno,  @pre $a \neq null$, @post $a \in todos()'$
- void removeAlumno(Alumno a), Elimina un alumno  @pre $a \neq null$, @post $a \notin todos()'$

Las pre y postcondiciones se puede escribir en lenguaje formal, como el anterior, o simplemente en lenguaje natural.

Representación:

- Lista de alumnos uno por línea

Métodos de Factoría:

- Alumnos of(String file)
- Alumnos of()

El método de factoría of se diseñarán con el patrón *singleton*.

Invariante

- los *dnis* de los alumnos deben ser diferentes

# Diseño de tipos

Antes de codificar es conveniente diseñar los tipos que usaremos en nuestro código. El diseño de un tipo es como un plano del mismo. En él se indica sus propiedades más relevantes y los mecanismos para crear valores de ese tipo. En la programación orientada a objetos los valores del tipo los llamaremos objetos.

Un tipo es un conjunto de valores, cada uno de esos valores tiene un conjunto de propiedades, adicionalmente un conjunto de operaciones para modificar el valor de las propiedades y mecanismos de factoría para crear los valores del tipo. Cada propiedad tiene un nombre de un tipo del conjunto de tipos previamente existente. Los valores de las propiedades pueden estar restringidos por expresiones lógicas que se indican en el _invariante_ del tipo.

Cada tipo tiene asociada una _dominio del tipo_. Este incluye el conjunto de todos los valores posibles del tipo. Este conjunto de valores se define por comprensión: el conjunto de valores que cumplen el invariante. 

Llamaremos _población de un tipo_ a un conjunto de finito de valores del tipo creado específicamente para un fin. En este caso el conjunto de valores será leído de un fichero o construido añadiendo objetos al conjunto. 

Un tipo puede ser inmutable, si no se pueden modificar sus propiedades una vez creado el valor, o mutables si se pueden cambiar. Por defecto un tipo será mutable.

Un tipo puede _extender_ a otro (diremos que hereda de o extiende a otro)

Cada propiedad puede ser:

- _Básica_: si su valor no depende del valor de otra propiedad
- _Derivada_: si su valor depende del valor de otras propiedades
- _Individual_: Si el valor de la propiedad es específico de cada valor del tipo
- _Compartida_: Si el valor de la propiedad es compartido por todos los valores del tipo

Las propiedades pueden tener parámetros para indicar un conjunto de propiedades del mismo tipo. En ese caso indicamos el rango permitido para los parámetros. Tambien pueden tener restricciones sobre el conjunto de valores que pueden tomar.

Las _operaciones_ indican la manera de modificar las propiedades del tipo. Si un tipo no tiene operaciones es inmutable. Las operaciones tienen parámetros de entrada. Las operaciones pueden tener restricciones. Restricciones en los parámetros de entrada que especificamos por un predicado que llamamos _precondición_ (@pre p(x)). Restricciones entre los vlores de los parámetros de entrada y el valor de las propiedades tras aplicar la operación que especificamos por un predicado llamamos _postcondición_ (@post p(x,v)).

Las factorías son mecanismos para construir valores de un tipo. Generalmente usaremos los siguientes:

- _of(propiedades)__: Crea un valor del tipo a partir de algunas propiedades del mismo
- _of()__: Crea un valor por defecto del tipo
- _parse(texto)__: Crea un valor del tipo a partir de una cadena de caracteres

_Representación_ es el mecanismo para convertir un valor del tipo en una cadena de caracteres que pueda ser presentada en la consola o grabada en un fichero.

_Igualdad_: Es una expresión booleana que indica cuando dos valores son iguales. Por defecto dos valores son iguales si tienen las propiedades básicas iguales.

_Orden natural_: En algunos tipos se puede definir un orden total sobre los valores del tipo que llamaremos orden natural.

_Restricciones_: Son predicados que deben cumplir los valores de un tipo o el conjunto de valores de la población de un tipo. Aqui podemos acumular las restricciones de las propiedades, de las operaciones de un tipo. Al conjunto de restricciones también se le suele llamar _Invariante_.


## Diseño de poblaciones

Una población de un tipo _E_ es un  nuevo tipo _P_ cuyos valores son conjuntos de valores del tipo _E_ anterior. En este conjunto suele existir una o varias propiedades que identifican de manera única a cada valor del tipo _E_ en la población.

Las factorías de las poblaciones las diseñaremos generalmente son el patrón de diseño _singleton_. Este es un mecanismo de factoría que nos permite obtener siempre el mismo valor en las sucesivas llamadas a la factoría. Las poblaciones suelen tener mecanismos para leer los valores de un fichero o de la red en general.

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

Representación como cadena: 

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
- $alumno(dni) = a, dni \neq null, \exists \ a \in todos() | a.dni = dni$
- $get(index) = a, 0 \le index \lt size(), a \in todos()$

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

Los métodos de factoría se diseñarán con el patrón _singleton_.

Invariante

- los _dnis_ de los alumnos deben ser diferentes

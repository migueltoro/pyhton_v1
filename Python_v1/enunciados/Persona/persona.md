# Persona 

Inmutable

Propiedades básicas:

- apellidos, de tipo String
- nombre, de tipo String
- dni, de tipo String 
- fechaDeNacimiento, de tipo LocalDateTime
- telefono: str
- direccion:Direccion 

Propiedades derivadas

- edad: Integer
- siguiente_cumple: date
- dia_semana_nacimiento: str
- dia_semana_siguiente_cumple:str
- horoscopo: Horoscopo

Métodos privados

- _check_dni(text:str): bool, comprueba si e dni es correcto

Explicación

Comprobar dni:

Asumiendo ls = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
para comprobar el dni los pasos son:

- Toma los 8 dígitos del número de DNI y divídelos entre 23.
- Anota el resto r de la división, que será un número entre 0 y 22.
- Comprueba que ls[r] == letra

Horóscopo
 
- Aries: 21 de marzo - 19 de abril
- Tauro: 20 de abril - 20 de mayo
- Géminis: 21 de mayo - 20 de junio
- Cáncer: 21 de junio - 22 de julio
- Leo: 23 de julio - 22 de agosto
- Virgo: 23 de agosto - 22 de septiembre
- Libra: 23 de septiembre - 22 de octubre
- Escorpio: 23 de octubre - 21 de noviembre
- Sagitario: 22 de noviembre - 21 de diciembre
- Capricornio: 22 de diciembre - 19 de enero
- Acuario: 20 de enero - 18 de febrero
- Piscis: 19 de febrero - 20 de marzo

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

Extiende a Persona  y es inmutable

Propiedades

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

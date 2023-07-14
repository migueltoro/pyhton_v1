# Centro

Se quiere hacer una pequeña aplicación que ayude en la gestión de un centro universitario. Un centro universitario tiene profesores, asignaturas y alumnos. Las asignaturas pueden tener varios grupos o ninguno. Los profesores son asignados para impartir grupos de asignaturas mientras que los alumnos se matriculan en grupos de algunas de las asignaturas. 

Los datos para gestionar este centro educativo provienen de 5 archivos diferentes:
1.	profesores.txt: datos de los profesores del centro educativo. Cada una de las líneas del fichero tienen el mismo formato con líneas de la forma: 
```
Badía Carretero,Felipa,53045701L,1998-10-26 18:31,+34722071515,Avenida de Leonardo Pont 26;Huelva;22501,Doctor
```
Con propiedades: apellidos, nombre, dni, fecha de nacimiento, teléfono, dirección y título 

2.	alumnos.txt: datos de los profesores del centro educativo. Cada una de las líneas del fichero tienen el mismo formato con líneas de la forma: 
```
Girona Gómez,Nieves,92521023G,1998-01-20 02:07,+34721158714,Paseo de Herminio Maestre 71;Ourense;16866,8.3
```
Con propiedades: apellidos, nombre, dni, fecha de nacimiento, teléfono, dirección y nota media de entrada al grado
3.	asignaturas.txt: datos de las asignaturas que se imparten en el centro universitario. Cada una de las líneas del fichero tienen el mismo formato con líneas de la forma: 
```
0,Fundamentos básicos de la informática,6,3
```
Con propiedades: id, nombre, número de créditos y número de grupos
4.	matriculas.txt: datos de las matrículas que han realizado cada uno de los alumnos en las distintas asignaturas del centro. Cada una de las líneas del fichero tienen el mismo formato con líneas de la forma: 
```
72842943B,0,0
```
Con propiedades: dni del alumno, identificador de asignatura, número de grupo
5.	asignaciones.txt: datos de las asignaciones entre los profesores y las asignaturas que imparten. Cada una de las líneas del fichero tienen el mismo formato con líneas de la forma: 
```
14218974Y,5,0
```
Con propiedades: dni del profesor, identificador de asignatura, número de grupo

# Tipos

## Direccion (inmutable)

Propiedades:
•	calle, de tipo String, básica, consultable. 
•	ciudad, de tipo String, básica, consultable. 
•	zip_code, de tipo Integer, básica, consultable. 

Métodos de factoría: 
•	parse(String text): Construye un objeto a partir de una cadena de caracteres con la información de las propiedades básicas. La cadena de caracteres tendrá el formato “calle;ciudad;zip_code”.

## Persona (inmutable)

Propiedades:

•	apellidos, de tipo String, básica, consultable. Los apellidos no pueden estar en blanco.
•	nombre, de tipo String, básica, consultable. El nombre no puede estar en blanco.
•	dni, de tipo String, básica, consultable. El dni debe estar compuesto de 8 números y una letra mayúscula al final, además, esa última letra debe corresponder al número. En la siguiente url puede observar cuál es la metodología que se usa en España para calcular la correspondencia entre número y letra del DNI. 
•	fechaDeNacimiento, de tipo LocalDateTime, básica, consultable. La fecha/hora de nacimiento debe estar en el pasado.
•	telefono, de tipo String, básica, consultable. 
•	direccion, de tipo Direccion, básica, consultable. 
•	edad, de tipo Integer, derivada, consultable. 
•	siguienteCumple, de tipo LocalDate, derivada, consultable. Devuelve cuándo sería el cumpleaños de dicha persona el año que viene.
•	diaSemanaSiguienteCumple, de tipo DayOfWeek, derivada, consultable. Devuelve el día de la semana (MONDAY, TUESDAY, WEDNESDAY, etc), del siguiente cumpleaños.
•	diaSemanaNacimiento, de tipo DayofWeek, derivada. Devuelve el día de la semana en el que nació la persona (MONDAY, TUESDAY, WEDNESDAY, etc). 
•	mesCumple, de tipo Integer, derivada, consultable. Devuelve el mes en el que nació la persona representado como un entero (1 a 12).
•	nombreCompleto, de tipo String, derivada, consultable. Devuelve el nombre completo de la persona en formato “nombre apellidos”.

Métodos de factoría: 

•	of(String apellidos, String nombre, String dni, LocalDateTime fechaDeNacimiento, String telefono, Direccion direccion) Construye un objeto a partir de un valor para cada una de las propiedades básicas del tipo. 
•	parse(String text, DateTimeFormatter ft) Construye un objeto a partir de una cadena de caracteres con la información de las propiedades básicas. La cadena de caracteres tendrá el formato “apellidos,nombre,dni,fecha_de_nacimiento,telefono,calle;ciudad;zip_code”. La variable ft nos indica el formato de la fecha de nacimiento.
•	parse(String text) Construye un objeto a partir de una cadena de caracteres con la información de las propiedades básicas. El patrón de fecha a utilizar para la fecha de nacimiento será "yyyy-MM-dd HH:mm".
•	parseList(List\\<String\> partes, DateTimeFormatter ft) Construye un objeto a partir de una lista de cadenas de caracteres con la información de las propiedades básicas. La lista de cadena de caracteres tendrá el formato:
```
[apellidos, nombre, dni, fechaDeNacimiento, telefono, calle;ciudad;zip_code]. 
```
La variable ft nos indica el formato de la fecha de nacimiento.
•	parseList(List\<String\> partes) Construye un objeto a partir de una lista de cadenas de caracteres con la información de las propiedades básicas. El patrón de fecha a utilizar para la fecha de nacimiento será _yyyy-MM-dd HH:mm_. 

Representación como cadena: 
nombre apellidos, de años, nacido el fecha nacimiento a las hora nacimiento.
Por ejemplo Ramiro Casares Amador, de 19, nacido el 14-06-2003 a las 10:02

Debemos realizar un test al final de la implementación del tipo Persona que dé como resultado la siguiente salida por consola: 

```
Ramiro Casares Amador, de 19, nacido el 14-06-2003 a las 10:02
- La fecha de nacimiento de Ramiro es 14-06-2003
- La edad de Ramiro es 19
- Su próximo cumpleaños será un WEDNESDAY
```
## Alumno 

Propiedades: extiende a Persona  y es inmutable

•	nota, de tipo Double, básica, consultable. Indica la nota media de acceso al grado. La nota debe ser positiva y estar comprendida entre 0 y 14.

Métodos de factoría: 

•	of(Persona p, Double Nota): Construye un objeto a partir de una objeto de tipo Persona y una nota.
•	parse(String text): Construye un objeto a partir de una cadena de texto con la información de las propiedades básicas del tipo. La cadena de caracteres tendrá el formato 
“apellidos,nombre,dni,fecha_de_nacimiento,telefono,calle;ciudad;zip_code,nota”. 

Representación como cadena: 

La misma representación que el tipo del que hereda añadiéndole además la nota de entrada al grado.
Por ejemplo
```
Ramiro Casares Amador, de 19, nacido el 14-06-2003 a las 10:02 con nota de entrada 10.5
```

## Alumnos

Es un tipo que representa una población de alumnos. Una población de objetos es un conjunto de objetos de un tipo donde cada uno tiene un identificador distinto de los demás. En este caso el identificador es el dni del alumno. Tiene otros métodos específicos para cada población.

Propiedades:

•	Alumno alumno(String dni)
- Alumno get(Integer index)
- Integer size()
- Set\<Alumnos\> todos()

Operaciones:

•	void addAlumno(Alumno a), Añade un alumno
•	void removeAlumno(Alumno a), Elimina un alumno

Representación:

- Lista de alumnos uno por línea

Métodos de Factoría:

- Alumnos of(String file)
- Alumnos of()

Invariante

- los dnis de los alumnos deben ser diferentes

## Profesor

Propiedades extiende a Persona  y es inmutable

•	titulo, de tipo Titulo(Enum), básica, consultable. Indica la titulación que posee, puede tomar los valores Diplomado, Master o Doctor.

Métodos de factoría: 

•	of(Persona p, Titulo titulo): Construye un objeto a partir de una objeto de tipo Persona y un título.
•	parse(String text): Construye un objeto a partir de una cadena de texto con la información de las propiedades básicas del tipo. La cadena de caracteres tendrá el formato “apellidos,nombre,dni,fecha_de_nacimiento,telefono,calle;ciudad;zip_code,titulo”. Pista: para su implementación deberá usar el método de factoría of del tipo Profesor y el método de factoría parseList del tipo Persona.

Representación como cadena: 

La misma representación que el tipo del que hereda añadiéndole además la titulación que posee.
Por ejemplo 
```
Felipa Badía Carretero, de 24, nacido el 25-06-1994 a las 12:45 con titulo Doctor
```

## Profesores

Es un tipo que representa una población de profesores. Una población de objetos es un conjunto de objetos de un tipo donde cada uno tiene un identificador distinto de los demás. En este caso el identificador es el dni del profesor. Tiene otros métodos específicos para cada población.

Propiedades:

• Profesor profesor(String dni)
- Profesor get(Integer index)
- Integer size()
- Set\<Profesor\> todos()

Operaciones:

•	void addProfesor(Profesor p), Añade un profesor
•	void removeProfesor(Profesor a), Elimina un profesor

Representación:

- Lista de profesores uno por línea

Métodos de Factoría:

- Profesores of(String file)
- Profesores of()

Invariante

- los dnis de los profesores deben ser diferentes

## Asignatura

Propiedades, inmutable

•	ida, de tipo Integer, básica, consultable. Indica el identificador de la asignatura.
•	nombre, de tipo String, básica, consultable. Indica el nombre de la asignatura.
•	creditos, de tipo Integer, básica, consultable. Indica el número de créditos de la asignatura. 
•	numGrupos, de tipo Integer, básica, consultable. Indica el número de grupos que tiene esa asignatura.

Métodos de factoría: 

•	parse(String text): Construye un objeto a partir de una cadena de texto con la información de las propiedades básicas del tipo. La cadena de caracteres tendrá el formato 

```
id,nombre,creditos,numMaxGrupos
```

Representación como cadena: nombre, créditos, numMaxGrupos

## Asignaturas

Es un tipo que representa una población de asignaturas. Una población de objetos es un conjunto de objetos de un tipo donde cada uno tiene un identificador distinto de los demás. En este caso el identificador es el ida de la asignatura. Tiene otros métodos específicos para cada población.

Propiedades:

• Asignatura asignatura(Integer ida)
- Asignatura get(Integer index)
- Integer size()
- Set\<Asignatura\> todas()

Operaciones:

•	void addAsignatura(Asignatura a), Añade una asignatura
•	void removeAsignatura(Asignatura a), Elimina una asignatura

Representación:

- Lista de asignaturas uno por línea

Métodos de Factoría:

- Asignaturas of(String file)
- Asignaturas of()

Invariante

- los ida de las asignaturas deben ser diferentes

## Asignacion

Indica una asignación de un profesor a un grupo

Propiedades, inmutable

•	dni, de tipo String, básica, consultable. Indica el dni del profesor.
•	ida, de tipo Integer, básica, consultable. Identificador de la asignatura.
•	idg, de tipo Integer, básica, consultable. Identificador del grupo que imparte el profesor. 

Métodos de factoría: 

•	parse(String text): Construye un objeto a partir de una cadena de texto con la información de las propiedades básicas del tipo. La cadena de caracteres tendrá el formato _dni,ida,idg_. 

## Asignaciones

Es un tipo que representa una población de asignaciones. 

Propiedades:

- Asignacion get(Integer index)
- Integer size()
- Set\<Asignacion\> todas()

Operaciones:

•	void addAsignacion(Asignacion a), Añade una asignacion
•	void removeAsignacionAsignacion a), Elimina una asignacion

Representación:

- Lista de asignaciones uno por línea

Métodos de Factoría:

- Asignaciones of(String file)
- Asignaciones of()

## Matricula 

Indica una asignación de un alumno a un grupo

Propiedades, inmutable

•	dni, de tipo String, básica, consultable. Indica el dni del profesor.
•	ida, de tipo Integer, básica, consultable. Identificador de la asignatura.
•	idg, de tipo Integer, básica, consultable. Identificador del subgrupo que se le ha asignado al alumno dentro de esa asignatura. 

Métodos de factoría: 

•	of(String dni,Integer ida,Integer idg): Construye un objeto a partir de una variable por cada propiedad básica del tipo.
•	parse(String text): Construye un objeto a partir de una cadena de texto con la información de las propiedades básicas del tipo. La cadena de caracteres tendrá el formato _dni,ida,idg_. 

Representación como cadena:  dni, ida, idg

## Matriculas

Es un tipo que representa una población de matriculas. 

Propiedades:

- Matricula get(Integer index)
- Integer size()
- Set\<Matricula\> todas()

Operaciones:

•	void addMatricula(Matricula a), Añade una matricula
•	void removeMatricula(Matricula a), Elimina una matricula

Representación:

- Lista de matriculas uno por línea

Métodos de Factoría:

- Matriculas of(String file)
- Matriculas of()

## Grupo

Propiedades: Inmutable

- ida, de tipo Integer: identificador de asignatura 
- idg, de tipo Integer identificador de grupo de una asignatura

Método de factoría

- Grupo of(Integer ida, Integer idg)

## Grupos

Es un tipo que representa una población de grupos. 

Propiedades

- Integer size() 
- Set\<Grupo\> todos() 

Métodos de factoría

- Grupos of(Centro centro)

## Centro

Representa un centro escolar

Propiedades:

•	alumnos, de tipo Alumnos, básica. Los alumnos que hay en el centro.
•	profesores, de tipo Profesores, básica. Los profesores del centro. 
•	asignaturas, Asignaturas, básica. Las asignaturas que se imparten en el centro. 
•	matriculas, de tipo Matriculas, básica. Las matrículas que se han hecho en ese centro.
•	asignaciones, de tipo Asignaciones, básica. Las asignaciones entre profesores y grupos que se han llevado a cabo en el centro. 

Métodos de factoría: 

•	Centro of(): Construye un objeto a partir de los ficheros por defecto
•	Centro of(String alumnos, String profesores, String asignaturas, String matriculas, String asignaciones): Construye un objeto a partir de los ficheros de texto indicados





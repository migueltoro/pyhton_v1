# Biblioteca

Se quiere hacer una pequeña aplicación que ayude en la gestión de una biblioteca. Una biblioteca tiene libros, ejemplares, usuarios y prestamos. 

Los datos para gestionar la biblioteca provienen de 5 archivos diferentes:

1. libros.txt: datos de los libros de la biblioteca. Cada una de las líneas del fichero tiene el mismo formato con líneas de la forma:

```
978-1-04-876475-8,Tempora dolor consequuntur consequuntur atque reiciendis voluptates minus.,Xiomara Brunilda MenÃ©ndez Cabeza,628,20.59,2002-07-05,7231
```

Con propiedades: isbn, titulo, autor, numeroDePaginas, precio, fechaPublicacion, estimacionDeVentas

2. ejemplares.txt: datos de ejemplares disponibles de cada libro. Cada una de las líneas del fichero tienen la forma:

```
978-1-04-876475-8,0,2015-08-13
```

Con propiedades: isbn, codigo, fechaDeAdquisicion

3. usuarios.txt: son personas que san los libros de la biblioteca. Cada una de las líneas del fichero tienen la forma:

```
Plaza Rivero,Apolinar,88819763L,1990-09-08 19:14,+34664759382,CallejÃ³n Virginia Collado 21;Lugo;37687,2010-05-21
```

Con propiedades: apellidos, nombre, fechaNacimiento, dni, telefono,direccion, fechaAlta

4. prestamos.txt: datos de los prestamos de la biblioteca. Cada una de las líneas del fichero tienen la forma:

```
978-1-04-876475-8,1,52240178W,2020-02-03,MENSUAL
```

Con propiedades:   codigo, isbn, codigoEjemplar, dni, fechaPrestamo, tipo



#  Tipos

##  ## Direccion (inmutable)

Propiedades:
- calle, de tipo String, básica, consultable. 
- ciudad, de tipo String, básica, consultable. 
- zip_code, de tipo Integer, básica, consultable. 

Métodos de factoría: 
- parse(String text): Construye un objeto a partir de una cadena de caracteres con la información de las propiedades básicas. La cadena de caracteres tendrá el formato “calle;ciudad;zip_code”.

## Persona (inmutable)

Propiedades:

- apellidos, de tipo String, básica, consultable. Los apellidos no pueden estar en blanco.
- nombre, de tipo String, básica, consultable. El nombre no puede estar en blanco.
- dni, de tipo String, básica, consultable. El dni debe estar compuesto de 8 números y una letra mayúscula al final, además, esa última letra debe corresponder al número. En la siguiente url puede observar cuál es la metodología que se usa en España para calcular la correspondencia entre número y letra del DNI. 
- fechaDeNacimiento, de tipo LocalDateTime, básica, consultable. La fecha/hora de nacimiento debe estar en el pasado.
- telefono, de tipo String, básica, consultable. 
- direccion, de tipo Direccion, básica, consultable. 
- edad, de tipo Integer, derivada, consultable. 
- siguienteCumple, de tipo LocalDate, derivada, consultable. Devuelve cuándo sería el cumpleaños de dicha persona el año que viene.
- diaSemanaSiguienteCumple, de tipo DayOfWeek, derivada, consultable. Devuelve el día de la semana (MONDAY, TUESDAY, WEDNESDAY, etc), del siguiente cumpleaños.
- diaSemanaNacimiento, de tipo DayofWeek, derivada. Devuelve el día de la semana en el que nació la persona (MONDAY, TUESDAY, WEDNESDAY, etc). 
- mesCumple, de tipo Integer, derivada, consultable. Devuelve el mes en el que nació la persona representado como un entero (1 a 12).
- nombreCompleto, de tipo String, derivada, consultable. Devuelve el nombre completo de la persona en formato “nombre apellidos”.

Métodos de factoría: 

- of(String apellidos, String nombre, String dni, LocalDateTime fechaDeNacimiento, String telefono, Direccion direccion) Construye un objeto a partir de un valor para cada una de las propiedades básicas del tipo. 
- parse(String text, DateTimeFormatter ft) Construye un objeto a partir de una cadena de caracteres con la información de las propiedades básicas. La cadena de caracteres tendrá el formato “apellidos,nombre,dni,fecha_de_nacimiento,telefono,calle;ciudad;zip_code”. La variable ft nos indica el formato de la fecha de nacimiento.
- parse(String text) Construye un objeto a partir de una cadena de caracteres con la información de las propiedades básicas. El patrón de fecha a utilizar para la fecha de nacimiento será "yyyy-MM-dd HH:mm". PISTA: debe llamar al método parse anterior.
- parseList(List\\<String\> partes, DateTimeFormatter ft) Construye un objeto a partir de una lista de cadenas de caracteres con la información de las propiedades básicas. La lista de cadena de caracteres tendrá el formato:
```
[apellidos, nombre, dni, fechaDeNacimiento, telefono, calle;ciudad;zip_code]. 
```
La variable ft nos indica el formato de la fecha de nacimiento.
- parseList(List\<String\> partes) Construye un objeto a partir de una lista de cadenas de caracteres con la información de las propiedades básicas. El patrón de fecha a utilizar para la fecha de nacimiento será _yyyy-MM-dd HH:mm_. 

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

## Usuario

Propiedades: extiende a Persona y es inmutable

• fechaAlta, de tipo LocalDate, básica, consultable. Indica la fecha de alta en la biblioteca

Métodos de factoría:

• Usuario of(Persona p,LocalDate fechaAlta): Construye un objeto a partir de una objeto de tipo Persona y una fecha de alta.  
• Usuario parse(String text): Construye un objeto a partir de una cadena de texto con la información de las propiedades básicas del tipo. La cadena de caracteres tendrá el formato 

```
apellidos,nombre,dni,fecha_de_nacimiento,telefono,calle;ciudad;zip_code,fechaAlta.
```
Representación como cadena: La misma representación que el tipo del que hereda añadiéndole además la nota de entrada al grado.  

## Usuarios

Es un tipo que representa una población de usuarios. Una población de objetos es un conjunto de objetos de un tipo donde cada uno tiene un identificador distinto de los demás. En este caso el identificador es el dni del usuario. 

Propiedades:

• Usuario usuario(String dni)
- Usuario get(Integer index)
- Integer size()
- Set\<Usuarios\> elementos()

Operaciones:

• void addUsuario(Usuario a), Añade un usuario  
• void removeUsuario(Usuario a), Elimina un usuario

Representación:

- Lista de usuarios uno por línea

Métodos de Factoría:

- Usuarios of(String file)
- Usuarios of()

Invariante

- los dnis de los alumnos deben ser diferentes

## Libro

Propiedades, inmutable

- String isbn
- String titulo
- String autor
- Integer numeroDePaginas
- Double precio
- LocalDate fechaPublicacion
- Integer estimacionDeVentas

Métodos de factoría:

- Libro of(String ISBN, String titulo, String autor, Integer numeroDePaginas, Double precio,
LocalDate fechaPublicacion, Integer estimacionDeVentas)
- Libro parse(String text)


## Libros

Es un tipo que representa una población de libros. Una población de objetos es un conjunto de objetos de un tipo donde cada uno tiene un identificador distinto de los demás. En este caso el identificador es el isbn del libro. 

Propiedades:

• Libro libro(String isbn)
- Libro get(Integer index)
- Integer size()
- Set\<Libro\> elementos()

Operaciones:

• void addLibro(Libro p), Añade un libro 
• void removeLibro(Libro a), Elimina un libro

Representación:

- Lista de libros uno por línea

Métodos de Factoría:

- Libros of(String file)
- Libros of()

Invariante

- los isbn de los libros deben ser diferentes

## Ejemplar

Cada uno de los ejemplares de los libros de la biblioteca

Propiedades, inmutable

- String isbn
- Integer codigo
- LocalDate fechaDeAdquisicion

Métodos de factoría:

• Ejemplar of(String isbn, Integer num, LocalDate fechaDeAdquisicion)
- Ejemplar parse(String text)


## Ejempalres

Es un tipo que representa una población de ejemplares. Una población de objetos es un conjunto de objetos de un tipo donde cada uno tiene un identificador distinto de los demás. En este caso el identificador es el par del isbn del libro y el número de ejemplar. 

Propiedades:

• Ejemplar ejemplar(String isbn, Integer codigo)
- Ejemplar get(Integer index)
- Integer size()
- Set\<Ejemplar\> elementos()

Operaciones:

• void addEjemplar(Ejemplar a), Añade un ejemplar  
• void removeEjemplar(Ejemplar a), Elimina un ejemplar

Representación:

- Lista de ejempalres uno por línea

Métodos de Factoría:

- Ejemplares of(String file)
- Ejemplares of()

Invariante

- los pares isbn, codigo deben ser diferentes para todos los ejemplares

## Prestamo

Indica un préstamo de un ejemplar

Propiedades, inmutable

- Integer codigo
- String isbn
- Integer codigoEjemplar
- String dni
- LocalDate fechaPrestamo
- TipoPrestamo tipo

Métodos de factoría:

• Prestamo of(Integer codigo,String isbn,Integer codigoEjemplar,String dni, LocalDate fecha,TipoPrestamo tipo)
- Prestamo parse(String text): 

## Prestamos

Es un tipo que representa una población de prestamos.

Propiedades:

- Prestamo prestamo(Integer codigo)
- Prestamo get(Integer index)
- Integer size()
- Set\<Prestamo\> elementos()

Operaciones:

• void addPrestamo(Prestamo a), Añade un préstamo  
• void removePrestamo(Prestamo a), Elimina un préstamo

Representación:

- Lista de prestamos uno por línea

Métodos de Factoría:

- Prestamos of(String file)
- Prestamos of()

## Biblioteca

Representa un centro escolar

Propiedades:

- String nombre
- String codigoPostal
- String email
- Usuarios usuarios
- Libros libros
- Ejemplares ejemplares
- Prestamos prestamos;

Métodos de factoría:

• Biblioteca of(String nombre, String codigoPostal, String email): Construye un objeto a partir de los ficheros por defecto  
• Biblioteca of(String nombre, String codigoPostal, String email, String usuarios, String libros, String ejemplares, String prestamos): Construye un objeto a partir de los ficheros dados  


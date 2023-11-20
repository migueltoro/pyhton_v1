# Bancos

Algunas de las entidades más comunes que pueden aparecer en un proyecto informático bancario incluyen:

- Banco: propiedades
	- personas: Personas
	- empleados: Empleados
	- cuentas: Cuentas
	- prestamos: Prestamos

- Cuenta: propiedades, mutable
	- iban: str
	- dni, str
	- fecha_de_creacion
	- saldo: double
	- operaciones:
		-ingresar(c:double)
		-retirar(c:double)
	 Invariante
	 - el iban debe ser correcto
	 - otras restricciones
		
- Prestamo:
	- nid: int
	- dni_cliente: str
	- cantidad: double
	- fecha_comienzo: Fecha
	- fecha_fin: Fecha
	- interes: double
	- dni_empleado: str
	 Invariante
	 - Añadir restricciones

- Persona: ya explicado

- Empleado: hereda de persona, inmutable
	- dni: str
	- fecha_de_contrado
	- salario_mensual
       

- Personas: población de personas
	- operaciones y factorías de población
- Empleados: población de empleado
	- operaciones y factorías de población
- Cuentas: población de cuenta
	- operaciones y factorías de población
- Prestamos: población de préstamo
	- operaciones y factorías de población
	
- Banco: 
	- Propiedades
		- persoas: Personas: población de personas
		- emplenados: Empleados: población de empleado
		- cuentas: Cuentas: población de cuentas
		- prestamos: Prestamos: población de préstamo
	- Métodos de factoría
		- of(): Banco
		
- Questions: conjunto de funciones

- TestBanco: conjunto de tests

	  


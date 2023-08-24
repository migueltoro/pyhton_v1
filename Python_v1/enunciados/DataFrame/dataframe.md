## DataFrame

- Es un agregado de datos compuesto de filas y una cabecera con los nombres de cada fila.  Los nombres en la cabecera puede servir como índices para acceder a las columnas. Algunas columnas tienen todos sus valores distintos y, en este caso, los valores pueden ser usados como índices de las filas. Una casilla puede sr identificada por el nombre de la columna y un valor de la fila correspondiente. Los nombres en columnas deben ser distintos. Filas y columnas pueden ser identificadas también por un índice. Un ejemplo es:

|  |Alumnos | Nombre | Apellido | Peso | Altura | FechaNacimiento |
|-------:|-------:|-------:| --------:| ----:| ------:|------:|
|0| A1     | Roberto| Alfaro   |   70 |   1.78 | 28/01/2005 |
|1| A2     | Laura  | Bustamante | 57 | 1.6 | 03/04/2006 |
|2| A3     | Erick  | Estrada | 65 | 1.74 | 13/02/2004 |
|3| A4     | Maria  | Domínez | 52 | 1.49 | 01/02/2003 |
|4| A5     | Jorge  | Jimenez | 60 | 1.7 | 04/04/2004 |
|5| A6     | Rosa   | Ortiz | 56 | 1.53 | 09/11/2007 |

- En el ejemplo de arriba la casilla (A3,Apellido) tiene valor estrada. La misma casilla también sería la (2,2). La casilla (0,1) tiene valor Roberto. El ejemplo tiene 6 filas y 6 columnas. 

Propiedades

```python
- rows_number()->int
- colums_number()-> int
- colums_names()->list[str]
- colums()->dict[str,list[Any]]
- rows(self)->list[tuple]
- head(n:int)->DataFrame
- tail(n:int)->DataFrame
- slice(n:int,m:int)->DataFrame
- filter(colum_name:str,p:Callable[[Any],bool])->DataFrame
- sort_by(colum_name:str)->DataFrame
- group_by(colums_names:list[str],ag_name:str,op:Callable[[E,E],E], 
	  value:Callable[[tuple],E])->DataFrame
- add_colum(colum_name:str,datos:list[E])->DataFrame
- add_calculated_colum(colum_name:str,f:Callable[[E],R],new_colum:str)->DataFrame
- remove_colum(colum_name:str)->DataFrame
```
Métodos de factoría

```python
- of(nombres_columnas:list[str],filas:list[tuple])->DataFrame
- of_dict(datos:dict[str,list[Any]])->DataFrame
- parse(file:str, fp:Callable[[str],tuple])->DataFrame
```
Invariante

- Se debe comprobar que los nombres de las columnas son distintos

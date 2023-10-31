## DataFrame

- Es un agregado de datos compuesto de filas y una cabecera con los nombres de cada fila.  Los nombres en la cabecera puede servir para acceder a las columnas. Las filas se numeran consecutivamente. En algunso casos los todos los valores de una columna son distintos y en ese caso los valores pueden ser usados como índices de las filas. Una casilla puede ser identificada por el nombre de la columna y el índice de la fila correspondiente. Los nombres en columnas deben ser distintos.  Un ejemplo de fichero csv:

```
Nombre,Apellido,Edad,Altura,Fecha
Roberto,Alfaro,70,1.78,28/01/2005
Laura,Bustamante,57,1.6,03/04/2006
Erick,Estrada,65,1.74,13/02/2004
Maria,Dominez,52,1.49,01/02/2003
Jorge,Jimenez,60,1.7,04/04/2004
Rosa,Ortiz,56,1.53,09/11/2007
Roberto1,Alfaro1,70,1.77,29/01/2005
Laura1,Bustamante1,57,1.7,04/04/2006
Erick1,Estrada1,65,1.7,13/03/2004
Maria1,Dominez1,52,1.5,02/01/2003
Jorge1,Jimenez1,60,1.9,03/04/2004
Rosa1,Ortiz1,56,1.6,10/11/2007
```
Que al visualizarse se vería como:

|  |Alumnos | Nombre | Apellido | Peso | Altura | FechaNacimiento |
|-------:|-------:|-------:| --------:| ----:| ------:|------:|
|0| A1     | Roberto| Alfaro   |   70 |   1.78 | 28/01/2005 |
|1| A2     | Laura  | Bustamante | 57 | 1.6 | 03/04/2006 |
|2| A3     | Erick  | Estrada | 65 | 1.74 | 13/02/2004 |
|3| A4     | Maria  | Domínez | 52 | 1.49 | 01/02/2003 |
|4| A5     | Jorge  | Jimenez | 60 | 1.7 | 04/04/2004 |
|5| A6     | Rosa   | Ortiz | 56 | 1.53 | 09/11/2007 |

- En el ejemplo la casilla (2,Apellido) tiene valor Estrada. Alternativamente la casilla puede identificarse (A3,Apellido) o también (2,2). La casilla (0,1) tiene valor Roberto. El ejemplo tiene 6 filas y 6 columnas. 

Propiedades


- colum_names->list[str]: Nombres de la columnas
- colum_number->int: Número de columnas
- column(name:str)->list[str]: La columna de nombre colum
- column_index(index:int)->list[str]: La columna de índice colum
- colum_all_different(name:str)->bool: Si la columna de nombre colum tiene todos sus valores diferentes
- cell(row:int,colum:str)->str: La celda de la fila row y la columna colum
- cell_index(row:int,colum:int)->str: La celda de la fila row y la columna colum
- cell_name(row:str,colum:str)->str: La celda de la fila row y la columna colum
- row_number->int: Número de filas
- row(n:int)->list[str]: La fila n
- row_name(colum:str,row:str)->list[str]: La fila n cuyo valor row aparece en la columna colum siempre que en esa 	columna todos los valores sean diferentes
- rows->list[list[str]]: La filas
- head(n:int)->DataFrame: El Dataframe con las n primeras filas
- tail(n:int)->DataFrame: El Dataframe con las n últimas filas
- slice(n:int,m:int)->DataFrame: El Dataframe con las filas de la n a a m
- filter(colum_name:str,p:Callable[[list[str]],bool])->DataFrame: El Dataframe con las filas que cumplen p
- sort_by(colum_name:str,f:Callable[[list[str]],E])->DataFrame: 
		El Dataframe con las filas ordenadas según el valor de f
- group_by(colums_names:list[str],ag_name:str,op:Callable[[E,E],E],value:Callable[[list[str]],E])->DataFrame:
		El Dataframe con las filas agrupadas según lo valores de la tupla especificada por los nombres de columnas 		_colums\_names_, y los resultados acumulados según _value_ y _op_.
- add_colum(colum_name:str,datos:list[list[str]])->DataFrame: El Dataframe con la columna adicional _colum_name_, 	_datos_.
- add_calculated_colum(colum_name:str,f:Callable[[E],R],new_colum:str)->DataFrame: El Dataframe con la columna 	adicional de nombre _new\_colum_ y cuyos valores se calculan a partir de los de la columna _colum\_name_, aplicando 	la función _f_.
- remove_colum(colum_name:str)->DataFrame: El Dataframe con la columna _colum\_name_ eliminada.


Métodos de factoría


- of_dict(datos:dict[str,list[str]])->DataFrame: El Dataframe obtenido del diccionario
- of(colum_names:list[str],rows:list[list[str]])->DataFrame:)->DataFrame: El Dataframe obtenido de combinar los  	nombres de las columnas dados con las filas
- parse(file:str])->DataFrame: El Dataframe leído del fichero

Métodos de utilidad

- all_different(values:Iterable[Any])->bool: Si todos los valores del iterable son diferentes

Invariante

- Los nombres de las columnas son distintos

Implementación:

- Una posibilidad es usar un atributo privado de tipo dict[str,list[str]]

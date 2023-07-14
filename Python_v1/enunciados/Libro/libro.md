
# Libro

El objetivo es leer un libro de un fichero y hacer cálculos sobre las palabras que contiene, en que líneas aparecen, ordenarlas por frecuencias, etc. Se usará el fichero Quijote.txt para hacer los cálculos.

Se supone que las palabras están separadas una de otras por separadores que podemos definir. Los separadores que usaremos son "[ ,;.\n()?¿!¡:\"]" aunque podemos añadir o eliminar separadores.
Queremos implementar las siguientes funciones: 

- Integer numeroDeLineas(String file)
- Integer numeroDePalabrasDistintasNoHuecas(String file); 
- Set\<String\> palabrasDistintasNoHuecas(String file); 
- Double longitudMediaDeLineas(String file); 
- Integer numeroDeLineasVacias(String file); 
- String lineaMasLarga(String file); 
- Integer primeraLineaConPalabra(String file, String palabra); 
- String lineaNumero(String file,Integer n); 
- SortedMap\<String,Integer\> frecuenciasDePalabras(String file), Frecuencia de cada palabra. Ordenadas por palabras
- SortedMap\<Integer,Set\<String\>\> palabrasPorFrecuencias(String file); Palabras agrupadas por sus frecuencias de aparición. Ordenadas por frecuencias
- SortedMap\<String,Set\<Integer\>º\> lineasDePalabra(String file); Grupos de líneas donde aparece cada palabra.

Notas:

Necesitamos emular los métodos _zip_ y _enumerate_ de Python. El código se puede encontrar en el repositorio en la clase Stream2.


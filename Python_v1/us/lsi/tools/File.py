'''
Created on 15 jul. 2020

@author: migueltoro
'''


from typing import Iterable, Optional
import csv
import chardet
from us.lsi.tools.Preconditions import check_argument
from os.path import abspath, join, isfile
from os import getcwd
import sys

def root_project():
    return sys.path[1]

def absolute_path(relative_path:str,root:str=root_project())->str:
    """
    This function takes a relative path and a root path as input and returns the absolute path.

    Args:
        relative_path (str): The relative path to a file or directory.
        root (str, optional): The root path. Defaults to the root of the project.

    Returns:
        str: The absolute path formed by joining the root and the relative path.

    Example:
        >>> absolute_path('data/file.txt')
        '/path/to/project/data/file.txt'
    """
    return abspath(join(root, relative_path))

def dir_path()->str:
    return getcwd()

def existe_fichero(filePath:str)->bool:
    """
    This function checks if a file exists at the given file path.

    Args:
        filePath (str): The path to the file. This should be an absolute path.

    Returns:
        bool: True if the file exists, False otherwise.

    Example:
        >>> existe_fichero('path/to/file.txt')
        True
    """
    return isfile(filePath)
    
def partes_de_linea(linea:str, delimiter:str=",")-> list[str]:
    """
    This function takes a string and a delimiter as input and returns a list of substrings.
    Each substring is a part of the input string that was separated by the delimiter.

    Args:
        linea (str): The input string to be split.
        delimiter (str, optional): The delimiter used to split the string. Defaults to ','.

    Returns:
        list[str]: A list of substrings that were separated by the delimiter in the input string.

    Example:
        >>> partes_de_linea('part1,part2,part3')
        ['part1', 'part2', 'part3']
    """
    partes = linea.split(delimiter)
    return partes

def iterable_de_fichero(file:str,encoding:str='utf-8') -> Iterable[str]:
    """
    This function takes a file path and an encoding as input and returns an iterable of strings.
    Each string in the iterable is a line from the file.

    Args:
        file (str): The path to the file. This should be an absolute path.
        encoding (str, optional): The encoding of the file. Defaults to 'utf-8'.

    Raises:
        Exception: If the file does not exist, an exception is raised.

    Yields:
        Iterable[str]: An iterable of strings. Each string is a line from the file.

    Example:
        >>> for line in iterable_de_fichero('path/to/file.txt'):
        ...     print(line)
    """
    check_argument(existe_fichero(file),'El fichero {} no existe'.format(file))
    with open(file, "r", encoding=encoding) as f:
        for linea in f:
            yield linea.strip()
    
def lineas_de_fichero(file:str,encoding:str='utf-8') -> list[str]:
    """
    This function takes a file path and an encoding as input and returns a list of strings.
    Each string in the list is a line from the file, with leading and trailing whitespace removed.

    Args:
        file (str): The path to the file. This should be an absolute path.
        encoding (str, optional): The encoding of the file. Defaults to 'utf-8'.

    Raises:
        Exception: If the file does not exist, an exception is raised.

    Returns:
        list[str]: A list of strings. Each string is a line from the file.

    Example:
        >>> lines = lineas_de_fichero('path/to/file.txt')
        >>> print(lines)
        ['line1', 'line2', 'line3']
    """
    check_argument(existe_fichero(file),f'El fichero {file} no existe')
    with open(file,"r",encoding=encoding) as f:
        return  [linea.strip() for linea in f]
       
def lineas_de_csv(file:str, delimiter:str=",", encoding:str='utf-8')-> list[list[str]]:
    """
    This function reads a CSV file and returns a list of lists where each inner list represents a row in the CSV file.

    Args:
        file (str): The path to the CSV file. This should be an absolute path.
        delimiter (str, optional): The delimiter used in the CSV file. Defaults to ','.
        encoding (str, optional): The encoding of the CSV file. Defaults to 'utf-8'.

    Raises:
        Exception: If the file does not exist, an exception is raised.

    Returns:
        list[list[str]]: A list of lists where each inner list represents a row in the CSV file.

    Example:
        >>> rows = lineas_de_csv('path/to/file.csv')
        >>> print(rows)
        [['header1', 'header2'], ['row1value1', 'row1value2'], ['row2value1', 'row2value2']]
    """
    check_argument(existe_fichero(file),f'El fichero {file} no existe')
    with open(file,"r",encoding= encoding) as f:
        lector = csv.reader(f, delimiter = delimiter)
        return  [linea for linea in lector]
    
def dict_de_csv(file:str, delimiter:str=",", encoding:str='utf-8')->dict[str,list[str]]:
    """
    This function reads a CSV file and returns a dictionary where each key is a column header and the value is a list of all the values in that column.

    Args:
        file (str): The path to the CSV file. This should be an absolute path.
        delimiter (str, optional): The delimiter used in the CSV file. Defaults to ','.
        encoding (str, optional): The encoding of the CSV file. Defaults to 'utf-8'.

    Raises:
        Exception: If the file does not exist, an exception is raised.

    Returns:
        dict[str,list[str]]: A dictionary where each key is a column header and the value is a list of all the values in that column.

    Example:
        >>> data = dict_de_csv('path/to/file.csv')
        >>> print(data)
        {'header1': ['row1value1', 'row2value1'], 'header2': ['row1value2', 'row2value2']}
    """
    check_argument(existe_fichero(file),f'El fichero {file} no existe')
    with open(file,"r",encoding=encoding) as f:
        lector = csv.DictReader(f, delimiter = delimiter)
        r:dict[str,list[str]] = {}
        for row in lector:
            for k,v in row.items():
                r[k] = r.get(k, [])+[v]
        return r

def iterable_de_csv(file:str, delimiter:str=",", encoding:str='utf-8')-> Iterable[list[str]]:
    """
    This function reads a CSV file and returns an iterable where each item is a list representing a row in the CSV file.

    Args:
        file (str): The path to the CSV file. This should be an absolute path.
        delimiter (str, optional): The delimiter used in the CSV file. Defaults to ','.
        encoding (str, optional): The encoding of the CSV file. Defaults to 'utf-8'.

    Raises:
        Exception: If the file does not exist, an exception is raised.

    Yields:
        Iterable[list[str]]: An iterable where each item is a list representing a row in the CSV file.

    Example:
        >>> for row in iterable_de_csv('path/to/file.csv'):
        ...     print(row)
        ['header1', 'header2']
        ['row1value1', 'row1value2']
        ['row2value1', 'row2value2']
    """
    check_argument(existe_fichero(file),f'El fichero {file} no existe')
    with open(file,"r",encoding= encoding) as f:
        lector = csv.reader(f, delimiter = delimiter)
        for linea in lector:
            yield linea

def iterable_de_csv_partes(file:str, delimiter:str=",", encoding='utf-8')-> Iterable[str]:
    """
    This function reads a CSV file and returns an iterable where each item is a cell value in the CSV file.

    Args:
        file (str): The path to the CSV file. This should be an absolute path.
        delimiter (str, optional): The delimiter used in the CSV file. Defaults to ','.
        encoding (str, optional): The encoding of the CSV file. Defaults to 'utf-8'.

    Raises:
        Exception: If the file does not exist, an exception is raised.

    Yields:
        Iterable[str]: An iterable where each item is a cell value in the CSV file.

    Example:
        >>> for cell in iterable_de_csv_partes('path/to/file.csv'):
        ...     print(cell)
        'header1'
        'header2'
        'row1value1'
        'row1value2'
        'row2value1'
        'row2value2'
    """
    check_argument(existe_fichero(file),f'El fichero {file} no existe')
    with open(file,"r",encoding= encoding) as f:
        lector = csv.reader(f, delimiter = delimiter)
        for linea in lector:
            for p in linea:
                yield p      

def read(file:str,encoding:str='utf-8') -> str:
    """
    This function reads the contents of a file and returns it as a string.

    Args:
        file (str): The path to the file. This should be an absolute path.
        encoding (str, optional): The encoding of the file. Defaults to 'utf-8'.

    Raises:
        Exception: If the file does not exist, an exception is raised.

    Returns:
        str: The contents of the file as a string.

    Example:
        >>> read('path/to/file.txt')
        'file content'
    """
    check_argument(existe_fichero(file),'El fichero {} no existe'.format(file))
    with open(file,"r", encoding=encoding) as f:
        return f.read()
    
def write(file:str,texto:str) -> None:
    """
    This function writes a string to a file.

    Args:
        file (str): The path to the file. This should be an absolute path.
        texto (str): The string to be written to the file.

    Example:
        >>> write('path/to/file.txt', 'Hello, World!')
        # This will write 'Hello, World!' to 'path/to/file.txt'.
    """
    with open(file,"w", encoding='utf-8') as f:
        f.write(texto)

def write_iterable(file:str,iterable:Iterable[str], encoding='utf-8') -> None:
    """
    This function writes the contents of an iterable to a file, with each item on a new line.

    Args:
        file (str): The path to the file. This should be an absolute path.
        iterable (Iterable[str]): An iterable of strings to be written to the file.
        encoding (str, optional): The encoding of the file. Defaults to 'utf-8'.

    Example:
        >>> write_iterable('path/to/file.txt', ['line1', 'line2', 'line3'])
        # This will write 'line1', 'line2', and 'line3' to 'path/to/file.txt', each on a new line.
    """
    with open(file,"w", encoding=encoding) as f:
        f.writelines(f"{ln}\n" for ln in iterable)

def encoding(file:str)->Optional[str]:
    """
    This function determines the encoding of a given file.

    Args:
        file (str): The path to the file. This should be an absolute path.

    Raises:
        Exception: If the file does not exist, an exception is raised.

    Returns:
        Optional[str]: The encoding of the file if it can be determined, None otherwise.

    Example:
        >>> encoding('path/to/file.txt')
        'utf-8'
    """
    check_argument(existe_fichero(file),'El fichero {0} no existe'.format(file))
    with open(file,"rb") as f:
        data = f.read()
        enc = chardet.detect(data)
        return enc['encoding']

if __name__ == '__main__':
    print(sys.path)
    print(getcwd())
    print(root_project())
    print(absolute_path("datos/datos_2.txt"))
    print(existe_fichero(absolute_path("datos/datos_2.txt")))
    print(existe_fichero("datos/datos_2.txt"))
    root= "C:/Users/migueltoro/WorkSpaces/python/DataFrame/"
    print(existe_fichero("ficheros/mascotas.csv"))
    print(root_project())
    print(dict_de_csv(absolute_path("datos/pp2.csv")))   
    print(lineas_de_csv(absolute_path("datos/pp2.csv"))) 
    print(sys.path)  
    help(iterable_de_fichero)
    help(lineas_de_csv)
    
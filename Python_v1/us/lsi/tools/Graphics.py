'''
Created on 26 jul. 2020

@author: migueltoro
'''

from us.lsi.tools import File
from us.lsi.tools import String
from us.lsi.tools.Iterable import str_iter
from us.lsi.tools import Preconditions
from typing import overload


num = int | float

def line_chart(file_out:str,title:str,nombres_de_ejes:list[str],datos:tuple[list[int],list[float]]) -> None:  
    Preconditions.check_argument(len(nombres_de_ejes) ==2,'Debe haber dos nombres de ejes y hay {0:d}'.format(len(nombres_de_ejes)))
    result = File.read('../../../resources/LineChartPattern.html')
    cl = ("'{0:s}'".format(x) for x in nombres_de_ejes)
    camposText = str_iter(cl, sep=",",prefix="[",suffix="]")
    dt = (file_line_chart(e,datos) for e in range(len(datos[0])))
    dataText = str_iter(dt,sep=",\n",prefix="",suffix="")
    reglas = {"title":"'"+title+"'", "campos":camposText, "data":dataText}
    result = String.transform(result,reglas);
    File.write(file_out,result);
    
def file_line_chart(e,datos):
    return '[{0}]'.format(','.join(str(datos[i][e]) for i in range(len(datos))))

@overload
def pie_chart(fileOut:str,title:str,nombres_de_datos:list[str],nombres:list[str],datos:list[int]) -> None: ...
@overload
def pie_chart(fileOut:str,title:str,nombres_de_datos:list[str],nombres:list[str],datos:list[float]) -> None: ...
   
def pie_chart(fileOut:str,title:str,nombres_de_datos:list[str],nombres:list[str],datos:list[int]|list[float]) -> None:
    result = File.read("../../../resources/PieChartPattern.html")
    dt = ("'{0}'".format(e) for e in nombres_de_datos)
    campos_text = str_iter(dt,sep=",",prefix="[",suffix="]")
    dt = (file_pie_chart(e,nombres,datos) for e in range(0,len(datos)))
    data_text =  str_iter(dt,sep=",\n",prefix="",suffix="\n")
    reglas = {"title":"'"+title+"'","campos":campos_text,"data":data_text}
    result = String.transform(result,reglas);
    File.write(fileOut,result);
    
def file_pie_chart(e,nombres,datos):
    return "['%s',%s]" % (nombres[e],str(datos[e]))

@overload
def columns_bar_chart(file_out:str,title:str,nombres_de_datos:list[str],columns_labels:list[str],datos:list[int]) -> None: ...
@overload
def columns_bar_chart(file_out:str,title:str,nombres_de_datos:list[str],columns_labels:list[str],datos:list[float]) -> None: ...

def columns_bar_chart(file_out:str,title:str,nombres_de_datos:list[str],columns_labels:list[str],datos:list[int]|list[float]) -> None:
    result = File.read("../../../resources/ColumnsBarPattern.html")
    dt = ("'{0}'".format(e) for e in nombres_de_datos)
    nombres_de_datos_text = str_iter(dt,sep=",",prefix="[",suffix="]")
    cl = (columna_columns_bar_chart(e,columns_labels,datos) for e in range(0,len(datos)))    
    columnas_text = str_iter(cl,sep=",\n",prefix="",suffix="\n")
    reglas = {"title":"'%s'" % title,"nombresDatos":nombres_de_datos_text,"columnas":columnas_text}
    print(nombres_de_datos_text)
    print(columnas_text)
    result = String.transform(result,reglas)
    File.write(file_out,result)
    
@overload
def columna_columns_bar_chart(e:int,columns_labels:list[str],datos:list[int]) -> str: ...
@overload
def columna_columns_bar_chart(e:int,columns_labels:list[str],datos:list[float]) -> str: ...

def columna_columns_bar_chart(e:int,columns_labels:list[str],datos:list[int]|list[float]) -> str:
    return "['%s',%s]" % (columns_labels[e],str(datos[e]))

def cartas_graphic(file_out,cartas,fuerza,tipo):       
    result = File.read("../../../resources/CartasPattern.html")
    ct = ("<img src=\"../{0}\" width=\"120px\" height=\"180px\">".format(c.name_of_file) for c in cartas)
    cartas_text = str_iter(ct,sep="\n",prefix = "\n",suffix ="\n")
    reglas = {"cartas":cartas_text,"fuerza":str(fuerza), "tipo": tipo}
    result = String.transform(result,reglas);
    File.write(file_out,result)
         

if __name__ == '__main__':
    pass
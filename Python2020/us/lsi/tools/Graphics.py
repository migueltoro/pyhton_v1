'''
Created on 26 jul. 2020

@author: migueltoro
'''

from us.lsi.tools import File
from us.lsi.tools import String
from us.lsi.tools.Iterable import joining
from typing import List, Tuple, Union
from us.lsi.tools import Preconditions

def lineChart(fileOut:str,title:str,nombres_de_ejes:List[str],datos:Tuple[List[int],List[float]]) -> None:  
    Preconditions.checkArgument(len(nombres_de_ejes) ==2,'Debe haber dos nombres de ejes y hay {0:d}'.format(len(nombres_de_ejes)))
    result = File.texto_de_fichero('../../../resources/LineChartPattern.html')
    cl = ("'{0:s}'".format(x) for x in nombres_de_ejes)
    camposText = joining(cl, separator=",",prefix="[",suffix="]")
    dt = (filaLineChart(e,datos) for e in range(len(datos[0])))
    dataText = joining(dt,separator=",\n",prefix="",suffix="")
    reglas = {"title":"'"+title+"'", "campos":camposText, "data":dataText}
    result = String.transform(result,reglas);
    File.write(fileOut,result);
    
def filaLineChart(e,datos):
    return '[{0}]'.format(','.join(str(datos[i][e]) for i in range(len(datos))))
    
def pieChart(fileOut:str,title:str,nombres_de_datos:List[str],nombres:List[str],datos:List[Union[int,float]]) -> None:
    result = File.texto_de_fichero("../../../resources/PieChartPattern.html")
    dt = ("'{0}'".format(e) for e in nombres_de_datos)
    campos_text = joining(dt,separator=",",prefix="[",suffix="]")
    dt = (filaPieChart(e,nombres,datos) for e in range(0,len(datos)))
    data_text =  joining(dt,separator=",\n",prefix="",suffix="\n")
    reglas = {"title":"'"+title+"'","campos":campos_text,"data":data_text}
    result = String.transform(result,reglas);
    File.write(fileOut,result);
    
def filaPieChart(e,nombres,datos):
    return "['%s',%s]" % (nombres[e],str(datos[e]))


def columnsBarChart(fileOut:str,title:str,nombres_de_datos:List[str],columns_labels:List[str],datos:List[Union[int,float]]) -> None:
    result = File.texto_de_fichero("../../../resources/ColumnsBarPattern.html")
    dt = ("'{0}'".format(e) for e in nombres_de_datos)
    nombres_de_datos_text = joining(dt,separator=",",prefix="[",suffix="]")
    cl = (columna_columns_bar_chart(e,columns_labels,datos) for e in range(0,len(datos)))    
    columnas_text = joining(cl,separator=",\n",prefix="",suffix="\n")
    reglas = {"title":"'%s'" % title,"nombresDatos":nombres_de_datos_text,"columnas":columnas_text}
    print(nombres_de_datos_text)
    print(columnas_text)
    result = String.transform(result,reglas)
    File.write(fileOut,result)
 
def columna_columns_bar_chart(e:int,columns_labels:str,datos:Union[int,float]) -> str:
    return "['%s',%s]" % (columns_labels[e],str(datos[e]))

def cartas_graphic(fileOut,cartas,fuerza,tipo):       
    result = File.texto_de_fichero("../../../resources/CartasPattern.html")
    ct = ("<img src=\"../{0}\" width=\"120px\" height=\"180px\">".format(c.name_of_file) for c in cartas)
    cartas_text = joining(ct,separator="\n",prefix = "\n",suffix ="\n")
    reglas = {"cartas":cartas_text,"fuerza":str(fuerza), "tipo": tipo}
    result = String.transform(result,reglas);
    File.write(fileOut,result)
         

if __name__ == '__main__':
    pass
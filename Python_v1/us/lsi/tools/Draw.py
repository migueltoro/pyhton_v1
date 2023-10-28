'''
Created on 27 oct. 2020

@author: migueltoro
'''

from typing import Callable
import matplotlib.pyplot as plt # type: ignore
from  matplotlib.patches import Patch # type: ignore
from math import sin
from us.lsi.tools.Preconditions import check_argument

color:str='r'

def shape_circle(center:tuple[float,float],radio:float,fill=None)->Patch:
    return plt.Circle(center,radio, fill=fill, color=color)

def shape_polygon(datos:list[tuple[float,float]],closed=None, fill=None)->Patch:
    return plt.Polygon(datos, closed=closed, fill=fill, edgecolor=color)
    
def draw_shapes(shapes:list[Patch]): 
    plt.axes()
    for f in shapes:
        plt.gca().add_patch(f)
    plt.axis('scaled')
    plt.show()

def draw_function(function:Callable[[float],float],a:float,b:float,inc:float)->None: 
    plt.axes()
    n = int((b-a)/inc)
    x = [a+i*inc for i in range(0,n)]
    y = [function(v) for v in x]
    plt.plot(x, y)
    plt.show()
    
def draw_piechar(labels:list[str],sizes:list[int]):
    plt.pie(sizes, labels=labels)
    plt.axis('equal')
    plt.show()

def draw_barchart(labels:list[str],sizes:list[int],title:str,y_label:str):
    y_pos = list(range(len(sizes)))
    plt.bar(y_pos,sizes, align='center', alpha=0.5)
    plt.xticks(y_pos,labels)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
   
def draw_multiline(dx:list[float], dy:list[float],y_label:str='eje y',x_label:str='eje_x',title:str='Grafico'):
    check_argument(len(dx)==len(dy),'Las listas deben ser iguales')
    plt.ylabel(y_label)
    plt.xlabel(x_label) 
    plt.title(title) 
    plt.plot(dx,dy)
    plt.show()
   
if __name__ == '__main__':
    draw_piechar(['Python', 'C++', 'Ruby', 'Java'],[215, 130, 245, 210])
    draw_barchart(['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp'],[10,8,6,4,2,1],'Titulo','Prueba')
    circle = shape_circle((0, 0), 1.)
    draw_shapes([circle])
    draw_multiline([1,2,3,7,-1,5,6],[1,2,3,7,-1,5,6])
    draw_function(lambda x:sin(x),-25.,25,1.)
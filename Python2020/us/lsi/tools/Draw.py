'''
Created on 27 oct. 2020

@author: migueltoro
'''
from typing import List,Tuple
import matplotlib.pyplot as plt
import numpy as np

def shape_polygon(points:List[Tuple[float,float]]):
    return plt.Polygon(points, closed=True, fill=None, edgecolor='r')
    
def shape_segment(points:List[float]):
    
    return plt.Polygon(points, closed=None, fill=None, edgecolor='r')

def shape_circle(center:Tuple[float],radio:float,color:str='r'):
    return plt.Circle(center,radio, fill=None, color=color)

def shape_point(center:Tuple[float],size:float=0.05,color:str='r'):
    return plt.Circle(center,size,fill=True,color=color,fc=color)
    
def draw_piechar(labels:List[str],sizes:List[int]):
    plt.pie(sizes, labels=labels)
    plt.axis('equal')
    plt.show()

def draw_barchart(labels:List[str],sizes:List[int],title:str,y_label:str):
    y_pos = np.arange(len(sizes))
    plt.bar(y_pos,sizes, align='center', alpha=0.5)
    plt.xticks(y_pos,labels)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
   
def draw(figures:List): 
    plt.axes()
    for f in figures:
        plt.gca().add_patch(f)
    plt.axis('scaled')
    plt.show()

if __name__ == '__main__':
#    draw_piechar(['Python', 'C++', 'Ruby', 'Java'],[215, 130, 245, 210])
#    draw_barchart(['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp'],[10,8,6,4,2,1],'Titulo','Prueba')
#    draw_circle((0.5, 0.5), 0.2, color='r')
    circle = shape_circle((0, 0), 1.)
    polygon = shape_polygon([[2, 1], [8, 1], [8, 4]])
    line = shape_segment([[-40, 1], [9, -1]])
    punto = shape_point([-30, 2])
    draw([circle,line,polygon,punto])
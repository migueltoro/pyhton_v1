'''
Created on 30 nov 2022

@author: migueltoro
'''

from us.lsi.universo.CuerpoCeleste import CuerpoCeleste
from us.lsi.universo.Location import Location
from us.lsi.tools.Preconditions import check_argument, check_state
from tkinter import Canvas, Tk
from us.lsi.geometria.Punto2D import Punto2D
import random

xMaxDeFault: int = 600
yMaxDeFault: int  = 600
colorDeFondoDefault:str = 'white'
   
class Marco:
    
    def __init__(self, nombre:str,xMax:int,yMax:int,color_fondo:str):
        check_argument(xMax > 300, "La anchura de un universo debe ser al menos 300");
        check_argument(yMax > 300, "La altura de un universo debe ser al menos 300");
        self.__xMax:int=xMax
        self.__yMax:int=yMax
        t=Tk()
        t.title(nombre)
        self.__canvas:Canvas = Canvas(t, width=xMax, height=yMax, bg=color_fondo)
      
    @staticmethod
    def of(nombre:str,xMax:int=xMaxDeFault, yMax:int=yMaxDeFault, color_fondo:str=colorDeFondoDefault):
        return Marco(nombre, xMax, yMax, color_fondo)
        
    @property
    def xMax(self) -> int:
        return self.__xMax
    @property
    def yMax(self) -> int:
        return self.__yMax  
    @property
    def canvas(self) -> Canvas:
        return self.__canvas
    
    def punto_aleatorio(self, xmin:int, ymin:int) -> Punto2D:
        return Punto2D.of(random.randint(xmin, self.xMax), random.randint(ymin, self.yMax))
        
    def location(self, cuerpo:CuerpoCeleste) -> Location:

        minimoX=int(cuerpo.coordenadas().x) - (cuerpo.diametro / 2)
        maximoX=int(cuerpo.coordenadas().x) + (cuerpo.diametro / 2)
        minimoY=int(cuerpo.coordenadas().y) - (cuerpo.diametro / 2)
        maximoY=int(cuerpo.coordenadas().y) + (cuerpo.diametro / 2)
        r = None
        if minimoX > 0 and maximoX < self.__xMax and minimoY > 0 and maximoY < self.__yMax:
            r=Location.INSIDE
        elif minimoX < 0 and minimoY > 0 and maximoY < self.__yMax:
            r=Location.LEFT
        elif maximoX > self.__xMax and minimoY > 0 and maximoY < self.__yMax:
            r=Location.RIGHT
        elif minimoX > 0 and maximoX < self.__xMax and minimoY < 0:
            r=Location.UP
        elif minimoX > 0 and maximoX < self.__xMax and maximoY > self.__yMax:
            r=Location.DOWN
        else:
            r=Location.OUTSIDE
        return r
    
    def comprobar_posicion(self, cuerpo:CuerpoCeleste) -> None:
        p = self.location(cuerpo)   
        check_state(p==Location.INSIDE, "El cuerpo celeste está fuera de la ventana")
        
    def es_visible(self, cuerpo:CuerpoCeleste) -> bool:
        return self.location(cuerpo)==Location.INSIDE
    
    def mostrar_cuerpo_celeste(self, c:CuerpoCeleste) -> None:
        c.id=self.canvas.create_oval(c.coordenadas().x - c.diametro/2, c.coordenadas().y - c.diametro/2, c.coordenadas().x + c.diametro/2, c.coordenadas().y + c.diametro/2, fill=c.color)
    
    def ocultar_cuerpo_celeste(self, c:CuerpoCeleste) -> None:
        self.canvas.delete(c.id)
    
    def mover(self, cuerpo:CuerpoCeleste) -> None: 
        if self.es_visible(cuerpo):
            self.ocultar_cuerpo_celeste(cuerpo)
                       
        cuerpo.un_paso()
        cuerpo.cambiar_propiedades(self.location(cuerpo))
        
        if self.es_visible(cuerpo):
            self.mostrar_cuerpo_celeste(cuerpo) 
            

if __name__ == '__main__':
    pass
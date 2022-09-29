# -*- coding: utf-8 -*-
'''
Created on 11 ago 2022

@author: mateosg
'''

from __future__ import annotations
from us.lsi.geometria.Punto2D import Punto2D
import random
from us.lsi.universo.CuerpoCeleste import CuerpoCeleste
from tkinter import Canvas, Tk
from us.lsi.tools.Preconditions import check_argument, check_state
from us.lsi.universo.Location import Location


xMaxDeFault: int = 600
yMaxDeFault: int  = 600
colorDeFondoDefault:str = 'white'
umbralRiesgo: int = 10

incrTiempo:float = 0.05

    
class Universo2D:
    def __init__(self:Universo2D, nombre:str, xMax:int, yMax:int, color_fondo:str):
        check_argument(xMax > 300, "La anchura de un universo debe ser al menos 300");
        check_argument(yMax > 300, "La altura de un universo debe ser al menos 300");
        self._xMax:int=xMax
        self._yMax:int=yMax
        self._cuerpos_celestes:list[CuerpoCeleste]=list()
        t=Tk()
        t.title(nombre)
        self._ventana:Canvas = Canvas(t, width=xMax, height=yMax, bg=color_fondo)
        
    @property
    def ventana(self:Universo2D) -> Canvas:
        return self._ventana
    @property
    def xMax(self:Universo2D) -> int:
        return self._xMax
    @property
    def yMax(self:Universo2D) -> int:
        return self._yMax
    @property
    def cuerpos_celestes(self:Universo2D) -> list[CuerpoCeleste]:
        return self._cuerpos_celestes
    
    def punto_aleatorio(self:Universo2D, xmin:int, ymin:int) -> Punto2D:
        return Punto2D.of(random.randint(xmin, self.xMax), random.randint(ymin, self.yMax))
    
    @staticmethod
    def empty() -> Universo2D:
        return Universo2D("Universo vacio", xMaxDeFault, yMaxDeFault, colorDeFondoDefault)
    
    @staticmethod
    def of(nombre:str, longitudX:int, longitudY:int, colorFondo:str) -> Universo2D:
        return Universo2D(nombre, longitudX, longitudY, colorFondo)
    
    #este método no estaba
    def agregar(self:Universo2D, c:CuerpoCeleste) -> None:
        self._cuerpos_celestes.append(c)
        
    def mostrar_cuerpo_celeste(self:Universo2D, c:CuerpoCeleste) -> None:
        c._id_canvas=self.ventana.create_oval(c.coordenadas().x - c.diametro/2, c.coordenadas().y - c.diametro/2, c.coordenadas().x + c.diametro/2, c.coordenadas().y + c.diametro/2, fill=c.color)
    
    def ocultar_cuerpo_celeste(self:Universo2D, c:CuerpoCeleste) -> None:
        self.ventana.delete(c._id_canvas)
    
    def distancia_minima(self:Universo2D) -> tuple[float, CuerpoCeleste,  CuerpoCeleste]: #(dist. mín., c. celestes más cercanos)
        distancias=[(c1.distancia_a(c2),c1,c2) for c1,c2 in zip(self.cuerpos_celestes, self.cuerpos_celestes[1:])]
        return min(distancias, key=lambda x:x[0])
        
    ################### Los métodos location, esVisible etc. estaban antes en cuerpoCeleste ######
    def location(self:Universo2D, cuerpo:CuerpoCeleste) -> Location:

        minimoX=int(cuerpo.coordenadas().x) - (cuerpo.diametro / 2)
        maximoX=int(cuerpo.coordenadas().x) + (cuerpo.diametro / 2)
        minimoY=int(cuerpo.coordenadas().y) - (cuerpo.diametro / 2)
        maximoY=int(cuerpo.coordenadas().y) + (cuerpo.diametro / 2)
        r = None
        if minimoX > 0 and maximoX < self.xMax and minimoY > 0 and maximoY < self.yMax:
            r=Location.INSIDE
        elif minimoX < 0 and minimoY > 0 and maximoY < self.yMax:
            r=Location.LEFT
        elif maximoX > self.xMax and minimoY > 0 and maximoY < self.yMax:
            r=Location.RIGHT
        elif minimoX > 0 and maximoX < self.xMax and minimoY < 0:
            r=Location.UP
        elif minimoX > 0 and maximoX < self.xMax and maximoY > self.yMax:
            r=Location.DOWN
        else:
            r=Location.OUTSIDE
        return r
    
    def comprobar_posicion(self:Universo2D, cuerpo:CuerpoCeleste) -> None:
        p = self.location(cuerpo)   
        check_state(p==Location.INSIDE, "El cuerpo celeste está fuera de la ventana")
        
    def es_visible(self:Universo2D, cuerpo:CuerpoCeleste) -> bool:
        return self.location(cuerpo)==Location.INSIDE
    
    def mover(self:Universo2D, cuerpo:CuerpoCeleste) -> None: 
        if self.es_visible(cuerpo):
            self.ocultar_cuerpo_celeste(cuerpo)
            
        cuerpo.un_paso()
        cuerpo.cambiar_propiedades(self.location(cuerpo))
        
        if self.es_visible(cuerpo):
            self.mostrar_cuerpo_celeste(cuerpo)
    #####################################################################################
    def simular(self:Universo2D) -> None:
        self.loop(0.,self.distancia_minima(),0)
        self.ventana.pack()
        self.ventana.mainloop()

    def loop(self, tiempo:float, d_min:tuple[float,CuerpoCeleste,CuerpoCeleste], veces_en_riesgo:int) -> None:   
        
        id1=self.ventana.create_text(37,11,text="Tiempo: {0:.2f}".format(tiempo), fill='white')
        id2=self.ventana.create_text(57, self.yMax - 20,text="Veces en riesgo: {0}".format(veces_en_riesgo), fill='white')
        id3=self.ventana.create_text(67, self.yMax - 5,text="Distancia mínima: {0:.2f}".format(d_min[0]), fill='white')
        
        d_min=self.distancia_minima()
        
        if d_min[0]<=0:
           
            p1 = d_min[1].coordenadas()
            p2 = d_min[2].coordenadas()
            pm = Punto2D.of((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
            
            self.cuerpos_celestes.remove(d_min[1]) 
            self.ventana.delete(d_min[1]._id_canvas)
            
            self.cuerpos_celestes.remove(d_min[2])  
            self.ventana.delete(d_min[2]._id_canvas) 
    
            x=int(pm.x)
            y=int(pm.y)
            choque=self.ventana.create_oval(x-25,y-25,x+25,y+25,fill='white')
            self.ventana.after(1500, self.ventana.delete,choque)
            self.ventana.after(5000, exit)

        for c in self.cuerpos_celestes:
            self.mover(c)
        
        
        
        if d_min[0] <  umbralRiesgo:
            veces_en_riesgo += 1
            
        tiempo += incrTiempo
        
        self.ventana.after(100, self.ventana.delete,id1)
        self.ventana.after(100, self.ventana.delete,id2)
        self.ventana.after(100, self.ventana.delete,id3)
        
        self.ventana.after(100, self.loop,tiempo, d_min, veces_en_riesgo)
        
        
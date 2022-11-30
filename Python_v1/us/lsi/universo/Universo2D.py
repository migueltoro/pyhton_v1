# -*- coding: utf-8 -*-
'''
Created on 11 ago 2022

@author: mateosg
'''

from __future__ import annotations
from us.lsi.universo.CuerpoCeleste import CuerpoCeleste
from us.lsi.universo.Marco import Marco
from us.lsi.geometria.Punto2D import Punto2D

umbralRiesgo: int = 10

incrTiempo:float = 0.05

    
class Universo2D:
    
    def __init__(self, marco:Marco):
        self.__marco = marco
        self.__cuerpos_celestes:list[CuerpoCeleste]=list()
        
    @property
    def marco(self) -> Marco:
        return self.__marco   
       
    @property
    def cuerpos_celestes(self) -> list[CuerpoCeleste]:
        return self.__cuerpos_celestes
    
    @staticmethod
    def empty(m:Marco) -> Universo2D:
        return Universo2D(m)
    
    #este método no estaba
    def agregar(self, c:CuerpoCeleste) -> None:
        self.__cuerpos_celestes.append(c)
    
    def distancia_minima(self) -> tuple[float, CuerpoCeleste,  CuerpoCeleste]: #(dist. mín., c. celestes más cercanos)
        distancias=[(c1.distancia_a(c2),c1,c2) for c1,c2 in zip(self.cuerpos_celestes, self.cuerpos_celestes[1:])]
        return min(distancias, key=lambda x:x[0])
    
    #####################################################################################
    def simular(self) -> None:
        self.loop(0.,self.distancia_minima(),0)
        self.marco.canvas.pack()
        self.marco.canvas.mainloop()

    def loop(self, tiempo:float, d_min:tuple[float,CuerpoCeleste,CuerpoCeleste], veces_en_riesgo:int) -> None:   
        
        id1=self.marco.canvas.create_text(37,11,text="Tiempo: {0:.2f}".format(tiempo))
        id2=self.marco.canvas.create_text(57, self.marco.yMax - 20,text="Veces en riesgo: {0}".format(veces_en_riesgo))
        id3=self.marco.canvas.create_text(67, self.marco.yMax - 5,text="Distancia mínima: {0:.2f}".format(d_min[0]))
        
        d_min=self.distancia_minima()
        
        if d_min[0]<=0:
           
            p1 = d_min[1].coordenadas()
            p2 = d_min[2].coordenadas()
            pm = Punto2D.of((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
            
            self.cuerpos_celestes.remove(d_min[1]) 
            self.marco.canvas.delete(d_min[1].id)
            
            self.cuerpos_celestes.remove(d_min[2])  
            self.marco.canvas.delete(d_min[2].id) 
    
            x=int(pm.x)
            y=int(pm.y)
            choque:int=self.marco.canvas.create_oval(x-25,y-25,x+25,y+25,fill='white')
            self.marco.canvas.after(1500, self.__marco.canvas.delete,choque)
            self.marco.canvas.after(5000, exit)

        for c in self.cuerpos_celestes:
            self.marco.mover(c)
        
        if d_min[0] <  umbralRiesgo:
            veces_en_riesgo += 1
            
        tiempo += incrTiempo
       
        self.marco.canvas.after(100, self.marco.canvas.delete,id1)
        self.marco.canvas.after(100, self.marco.canvas.delete,id2)
        self.marco.canvas.after(100, self.marco.canvas.delete,id3)
        
        self.marco.canvas.after(100, self.loop,tiempo,d_min,veces_en_riesgo)
        
        
# -*- coding: utf-8 -*-
'''
Created on 11 ago 2022

@author: mateosg
'''

from __future__ import annotations
from us.lsi.universo.CuerpoCeleste import CuerpoCeleste
from us.lsi.universo.Marco import Marco
from us.lsi.geometria.Punto2D import Punto2D
import  tkinter as tk

umbral_de_riesgo: int = 5

incr_tiempo:float = 0.05

tiempo_maximo: float = 10.

    
class Universo2D:
    
    def __init__(self, marco:Marco):
        self.__marco = marco
        self.__cuerpos_celestes:list[CuerpoCeleste]=list()
        self.__dmin: tuple[float, CuerpoCeleste,  CuerpoCeleste]
        
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
        distancias=[(c1.distancia(c2),c1,c2) for c1,c2 in zip(self.cuerpos_celestes, self.cuerpos_celestes[1:])]
        return min(distancias, key=lambda x:x[0])
    
    #####################################################################################
    def simular(self) -> None:
        self.loop(0.,self.distancia_minima(),0)
        self.marco.canvas.pack()
        self.marco.canvas.mainloop()
        
    def mostrar_choque(self)-> None:
        p1:Punto2D = self.__dmin[1].coordenadas()
        p2:Punto2D = self.__dmin[2].coordenadas()
        pm = Punto2D.of((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
            
        self.cuerpos_celestes.remove(self.__dmin[1]) 
        self.marco.canvas.delete(self.marco.cuerpo_celeste_id(self.__dmin[1]))
            
        self.cuerpos_celestes.remove(self.__dmin[2])  
        self.marco.canvas.delete(self.marco.cuerpo_celeste_id(self.__dmin[2]))
    
        x=int(pm.x)
        y=int(pm.y)
        choque:int=self.marco.canvas.create_oval(x-25,y-25,x+25,y+25,fill='red')
        self.marco.canvas.after(1500, self.__marco.canvas.delete,choque)
        self.marco.canvas.after(5000, exit)
        
    def mostar_texto(self,x:int,y:int, text:str)-> int:
        return self.marco.canvas.create_text(x,y,
                text=text,fill="white", font='Helvetica 10 bold',justify=tk.RIGHT)

    def loop(self, tiempo:float, dmin:tuple[float,CuerpoCeleste,CuerpoCeleste], veces_en_riesgo:int) -> None:   
        
        id1=self.mostar_texto(60,20,f"Tiempo: {tiempo:.2f}")
        id2=self.mostar_texto(60,self.marco.yMax - 40,f"Veces en riesgo: {veces_en_riesgo}")
        id3=self.mostar_texto(60,self.marco.yMax - 20,f"Distancia mínima: {dmin[0]:.2f}")
        
        dmin=self.distancia_minima()
        self.__dmin = dmin
        
        if dmin[0]<=0:
            self.mostrar_choque()
            
        for c in self.cuerpos_celestes:
            self.marco.mover(c)
        
        if dmin[0] <  umbral_de_riesgo:
            veces_en_riesgo += 1
            
        tiempo += incr_tiempo
        
        if tiempo > tiempo_maximo:
            self.marco.canvas.after(1, exit)
       
        self.marco.canvas.after(100, self.marco.canvas.delete,id1)
        self.marco.canvas.after(100, self.marco.canvas.delete,id2)
        self.marco.canvas.after(100, self.marco.canvas.delete,id3)
        
        self.marco.canvas.after(100, self.loop,tiempo,dmin,veces_en_riesgo)
        
        
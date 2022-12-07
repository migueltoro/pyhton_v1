# -*- coding: utf-8 -*-
'''
Created on 12 ago 2022

@author: mateosg
'''
from __future__ import annotations
from us.lsi.universo.CuerpoCeleste import CuerpoCeleste
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.universo.Location import Location
import random
from math import pi

class Cometa(CuerpoCeleste):
    def __init__(self:Cometa, nombre:str, diametro:int, direccion:Vector2D, velocidad:float, posicion:Punto2D)->None:
        super().__init__(nombre,diametro,'black')
        self._direccion:Vector2D = direccion.unitario
        self._velocidad:float = velocidad
        self._coordenadas:Punto2D = posicion
        
    @staticmethod
    def of( nombre:str, diametro:int, direccion:Vector2D, velocidad:float, posicion:Punto2D)->Cometa:
        return Cometa(nombre, diametro, direccion, velocidad, posicion)
    
    @staticmethod
    def random(nombre:str, posicion: Punto2D):
        return Cometa.of(nombre, 10, Vector2D.of_radianes(1, random.uniform(0, pi/2)), 5, posicion)
        
    def coordenadas(self:Cometa)->Punto2D:
        return self._coordenadas
    
    def un_paso(self:Cometa)->None:
        pass
    
    def cambia_propiedades(self:Cometa, l:Location)->None:
        
        match l:
            case Location.DOWN:
                self._direccion=Vector2D.of(self._direccion.x, -self._direccion.y)
            case Location.LEFT:
                self._direccion=Vector2D.of(-self._direccion.x, self._direccion.y)
            case Location.RIGHT:
                self._direccion=Vector2D.of(-self._direccion.x, self._direccion.y)
            case Location.UP:
                self._direccion=Vector2D.of(self._direccion.x, -self._direccion.y)
            case __:
                pass
        
       
        #El producto vector/escalar está sobreescrito por Miguel en Vector2D
        #La suma Punto/Vector está sobreescrito en Punto2D    
        self._coordenadas =  self._coordenadas + self._direccion * self._velocidad 
            
        
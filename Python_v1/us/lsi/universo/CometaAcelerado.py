# -*- coding: utf-8 -*-
'''
Created on 12 ago 2022

@author: mateosg
'''
from __future__ import annotations
from us.lsi.universo.Cometa import Cometa
from us.lsi.geometria.Vector2D import Vector2D
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.universo.Location import Location
import random
from math import pi

class CometaAcelerado(Cometa):
    
    def __init__(self:CometaAcelerado, nombre:str, diametro:int, direccion:Vector2D, velocidad:float, posicion:Punto2D, aceleracion:float):
        super().__init__(nombre, diametro, direccion, velocidad, posicion)
        self.__aceleracion:float = aceleracion
              
    @staticmethod
    def of_acelerado(nombre:str, diametro:int, direccion:Vector2D, velocidad:float, posicion:Punto2D, aceleracion:float)->CometaAcelerado:
        return CometaAcelerado(nombre, diametro, direccion, velocidad, posicion, aceleracion)
    
    @staticmethod
    def random(nombre:str, posicion:Punto2D)->CometaAcelerado:
        return CometaAcelerado.of_acelerado(nombre, 10, Vector2D.of_radianes(1, random.uniform(0, pi/2)), 5, posicion, 0.25)
    
    def un_paso(self:CometaAcelerado)->None:
        pass
    
    def cambia_propiedades(self:CometaAcelerado, l:Location)->None:
        '''
        if (!this.location().equals(CuerpoCeleste.Location.Inside)) {
            this.velocidad = this.velocidad * (1 + this.aceleracion);
        } 
        this.coordenadas = this.coordenadas.traslada(this.direccion.multiply(this.velocidad));
        '''
        if l==Location.INSIDE:
            self._velocidad= self._velocidad * (1 + self.__aceleracion)
            
        self._coordenadas = self._coordenadas + self._direccion * self._velocidad
        
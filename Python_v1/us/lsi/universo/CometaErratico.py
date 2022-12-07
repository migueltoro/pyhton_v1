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

class CometaErratico(Cometa):
    def __init__(self:CometaErratico, nombre:str, diametro:int, direccion:Vector2D, velocidad:float, posicion:Punto2D):
        super().__init__(nombre, diametro, direccion, velocidad, posicion)
        
    @staticmethod
    def of(nombre:str, diametro:int, direccion:Vector2D, velocidad:float, posicion:Punto2D):
        return CometaErratico(nombre, diametro, direccion, velocidad, posicion)
    
    @staticmethod
    def random(nombre:str, posicion:Punto2D):
        return CometaErratico.of(nombre, 10, Vector2D.of_radianes(1, random.uniform(0, pi/2)), 5, posicion)
    
    def un_paso(self:CometaErratico)->None:
        '''
        Double angulo = Universo2D.valorAleatorioEntre(0., Math.PI);
        this.direccion = Vector2D.ofRadianes(1., angulo);        
        this.coordenadas = this.coordenadas.traslada(this.direccion.multiply(this.velocidad));
        '''
        self.__angulo=random.uniform(0, pi)
        self._direccion=Vector2D.of_radianes(1., self.__angulo)
        self._coordenadas = self._coordenadas + self._direccion * self._velocidad
        
    def cambia_propiedades(self:CometaErratico, l:Location)->None:
        pass
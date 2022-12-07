# -*- coding: utf-8 -*-
'''
Created on 12 ago 2022

@author: mateosg
'''
from __future__ import annotations
from us.lsi.universo.CuerpoCeleste import CuerpoCeleste
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.universo.Location import Location


class Estrella(CuerpoCeleste):
    def __init__(self: Estrella, nombre:str, diametro:int, posicion:Punto2D):
        super().__init__(nombre,diametro,'yellow')
        self._coordenadas: Punto2D = posicion
        
    @staticmethod   
    def of(nombre:str, diametro:int, posicion:Punto2D):
        return Estrella(nombre,diametro,posicion)
  
    def coordenadas(self:Estrella)->Punto2D:
        return self._coordenadas
    
    def un_paso(self:Estrella)->None:
        pass
    
    def cambia_propiedades(self:Estrella, l:Location)->None:
        pass
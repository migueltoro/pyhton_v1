# -*- coding: utf-8 -*-
'''
Created on 11 ago 2022

@author: mateosg
'''
from __future__ import annotations
from abc import ABC, abstractmethod

from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.universo.Location import Location


    
class CuerpoCeleste(ABC):
    
    def __init__(self:CuerpoCeleste, nombre:str, diametro:int, color:str):
        self._nombre:str=nombre
        self._diametro:int=diametro
        self._color:str=color
        self._id_canvas:int=0 #se modifica en Universo2D
       
     
    @property
    def nombre(self:CuerpoCeleste) -> str:
        return self._nombre
    @property   
    def diametro(self:CuerpoCeleste) -> int:
        return self._diametro
    @property
    def color(self:CuerpoCeleste) -> str:
        return self._color
    @property
    def id_canvas(self:CuerpoCeleste) -> int:
        return self._id_canvas
    
    
    #################### Métodos abstractos ############################
    @abstractmethod
    def coordenadas(self:CuerpoCeleste) -> Punto2D:
        pass
    @abstractmethod
    def un_paso(self:CuerpoCeleste) -> None:
        pass
    @abstractmethod
    def cambiar_propiedades(self:CuerpoCeleste, l:Location) -> None:
        pass
    
    #####################################################################
    def distancia_a(self:CuerpoCeleste, cuerpo:CuerpoCeleste):
        distanciaCentros=self.coordenadas().distancia_a(cuerpo.coordenadas())
        d = distanciaCentros - self.diametro / 2 - cuerpo.diametro / 2
        return d
    
    #quitamos mostrar/ocultar_cuerpo_celeste, location, comprobar_posicion, es visible y mover. Lo ponemos todo en Universo2D
   
   
        
        
        
           
    
        
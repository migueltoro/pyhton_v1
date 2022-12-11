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
        self.__nombre:str=nombre
        self.__diametro:int=diametro
        self.__color:str=color
       
    @property
    def nombre(self:CuerpoCeleste) -> str:
        return self.__nombre
    @property   
    def diametro(self:CuerpoCeleste) -> int:
        return self.__diametro
    @property
    def color(self:CuerpoCeleste) -> str:
        return self.__color
    
    def __hash__(self)->int:
        return  hash(self.__nombre)
    
    def __eq__(self, other)->bool:
        if isinstance(other, CuerpoCeleste):
            return self.__nombre == other.__nombre
        return False
    
    def __str__(self)->str:
        return self.__nombre
    
    #################### Métodos abstractos ############################
    @abstractmethod
    def coordenadas(self) -> Punto2D:
        pass
    @abstractmethod
    def un_paso(self) -> None:
        pass
    @abstractmethod
    def cambia_propiedades(self, location:Location) -> None:
        pass
    
    #####################################################################
    def distancia_a(self, cuerpo:CuerpoCeleste):
        distanciaCentros=self.coordenadas().distancia_a(cuerpo.coordenadas())
        d = distanciaCentros - self.diametro / 2 - cuerpo.diametro / 2
        return d  
    
        
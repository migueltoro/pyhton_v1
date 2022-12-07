# -*- coding: utf-8 -*-
'''
Created on 12 ago 2022

@author: mateosg
'''
from __future__ import annotations
from us.lsi.universo.CuerpoCeleste import CuerpoCeleste
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.universo.Orbita2D import Orbita2D
from us.lsi.universo.Estrella import Estrella
from us.lsi.universo.Location import Location

class Planeta(CuerpoCeleste):
    
    def __init__(self: Planeta, nombre:str, diametro:int, color:str, centro_orbita:CuerpoCeleste, angulo:float, orbita:Orbita2D):
        super().__init__(nombre,diametro,color)
        self.__angulo:float=angulo
        self.__orbita:Orbita2D=orbita
        self.__centro_orbita:CuerpoCeleste=centro_orbita
        self._coordenadas:Punto2D = centro_orbita.coordenadas() + orbita.r(angulo) #suma del punto central y un radio-vector de la órbita
        
    @staticmethod  
    def of(nombre:str, diametro:int, color:str, centro_orbita:CuerpoCeleste, angulo:float, orbita:Orbita2D) -> Planeta:
        return Planeta(nombre,diametro,color,centro_orbita,angulo, orbita)
    
    @staticmethod  
    def of_estrella(nombre:str, estrella:Estrella):
        return Planeta.of(nombre, 15, 'magenta', estrella, 0., Orbita2D.random())
    
    @staticmethod
    def satelite(nombre:str,planeta:Planeta):
        return Planeta.of(nombre, 10, 'green', planeta, 0., planeta.orbita_menor())
    
    def orbita_menor(self) -> Orbita2D:
        return Orbita2D.of(self.__orbita.a/3, self.__orbita.b/3, self.__orbita.alfa, self.__orbita.T/3)
    
    def coordenadas(self)->Punto2D:
        return self._coordenadas
    
    def un_paso(self:Planeta)->None:
        '''
        this.angulo = this.angulo + this.orbita.velocidadAngular(angulo);
        Vector2D v = this.orbita.radioVector(this.angulo);
        this.coordenadas =  this.centroOrbita.coordenadas().add(v);
        '''
        self.__angulo += self.__orbita.w(self.__angulo)
        v = self.__orbita.r(self.__angulo)
        self._coordenadas = self.__centro_orbita.coordenadas() + v
    
    def cambia_propiedades(self:Planeta, l:Location)->None:
        pass
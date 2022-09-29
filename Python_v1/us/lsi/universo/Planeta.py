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
        self._angulo:float=angulo
        self._orbita:Orbita2D=orbita
        self._centro_orbita:CuerpoCeleste=centro_orbita
        #poner en enunciado que hay que añadir en el tipo Punto2D, la suma punto/vector
        self._coordenadas:Punto2D = centro_orbita.coordenadas() + orbita.r(angulo) #suma del punto central y un radio-vector de la órbita
        
    @staticmethod  
    def of(nombre:str, diametro:int, color:str, centro_orbita:CuerpoCeleste, angulo:float, orbita:Orbita2D) -> Planeta:
        return Planeta(nombre,diametro,color,centro_orbita,angulo, orbita)
    
    @staticmethod  
    def of_estrella(nombre:str, estrella:Estrella):
        return Planeta.of(nombre, 15, 'magenta', estrella, 0., Orbita2D.random())
    
    def satelite(self:Planeta, nombre:str):
        return Planeta.of(nombre, 10, 'green', self, 0., self.orbita_menor())
    
    def orbita_menor(self:Planeta) -> Orbita2D:
        return Orbita2D.of(self._orbita.a/3, self._orbita.b/3, self._orbita.alfa, self._orbita.T/3)
    
    def coordenadas(self:Planeta)->Punto2D:
        return self._coordenadas
    
    def un_paso(self:Planeta)->None:
        '''
        this.angulo = this.angulo + this.orbita.velocidadAngular(angulo);
        Vector2D v = this.orbita.radioVector(this.angulo);
        this.coordenadas =  this.centroOrbita.coordenadas().add(v);
        '''
        self._angulo += self._orbita.w(self._angulo)
        v = self._orbita.r(self._angulo)
        self._coordenadas = self._centro_orbita.coordenadas() + v
    
    def cambiar_propiedades(self:Planeta, l:Location)->None:
        pass
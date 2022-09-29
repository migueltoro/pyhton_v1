# -*- coding: utf-8 -*-
'''
Created on 2 ago 2022

@author: mateosg

a: Double, semieje mayor, a>0
b: Double, semieje menor, b>0
c: Double, semidistancia focal
α: Double, angulo del eje mayor con el eje X, 0 ≤ α ≤ π/2
e: Double, excentricidad, 0 ≤ e < 1
d: Double,
d1: Double, mínima distancia al foco
d2: Double, máxima distancia al foco
T: Double, período, T > 0
r(θ:Double):Vector2D, vector desde un foco a un punto de la elipse. El vector resultante
forma un angulo de θ con el eje mayor.
ω(θ:Double):Double, velocidad angular
'''

from __future__ import annotations
from dataclasses import dataclass
from us.lsi.geometria.Vector2D import Vector2D
from math import cos, pi, sqrt
from us.lsi.tools import Preconditions
import random 

@dataclass(frozen=True,order=True)
class Orbita2D:
    a: float 
    b: float
    alfa: float
    T: float

    @staticmethod
    def of(a:float, b:float, alfa:float, T:float) -> Orbita2D:
        Preconditions.check_argument(a>0 and b>0, 'No es una elipse válida')
        Preconditions.check_argument(0<=alfa<=pi/2, 'El ángulo de inclinación no es correcto')
        Preconditions.check_argument(T>0, 'Periodo incorrecto')
        return Orbita2D(a,b,alfa,T)
    
    @staticmethod
    def random() -> Orbita2D:

        a=random.uniform(100., 200.)
        b=random.uniform(100., 200.)
        while a<b:
            a=random.uniform(100., 200.)
            b=random.uniform(100., 200.)  
        alfa=random.uniform(0, pi/2)
        T=random.uniform(62.,125.)
        return Orbita2D.of(a, b, alfa, T)
        
        
    @property 
    def c(self:Orbita2D) -> float:   
        return sqrt(self.a*self.a - self.b*self.b) 
    @property    
    def e(self:Orbita2D) -> float:    
        e=self.c/self.a
        Preconditions.check_argument(0<=e<=1, 'Excentricidad incorrecta: {}'.format(e))
        return e
    @property
    def d(self:Orbita2D) -> float:
        return self.a*(1-self.e*self.e);
    @property
    def d1(self:Orbita2D) -> float:
        return self.a - self.c
    @property
    def d2(self:Orbita2D) -> float:
        return self.a + self.c
    
    def r(self:Orbita2D, theta:float) -> Vector2D:
        r=self.d/(1+self.e*cos(theta))
        return Vector2D.of_radianes(r, theta+self.alfa)
        
        
    
    def w(self:Orbita2D, theta:float) -> float:
        v=self.r(theta).modulo #desde foco 1
        #2*Math.PI*this.a()/(this.periodo()*rm)*Math.sqrt(2*this.a()/rm-1);
        return 2*pi*self.a/(self.T*v)*sqrt(2*self.a/v-1)

        
        
if __name__ == '__main__':
    #o=Orbita2D.of(4, 2*sqrt(3), pi/7, 0.5)
    o=Orbita2D.random()
    print("a:",o.a)
    print("b:",o.b)
    print("alfa:",o.alfa)
    print("T:",o.T)
    print("c:",o.c)
    print("e:",o.e)
    print("d:",o.d)
    print("d1:",o.d1)
    print("d2: ",o.d2)
    print("vector con ángulo pi/7:",o.r(pi/7))
    print("velocidad angular con pi/7:",o.w(pi/7))
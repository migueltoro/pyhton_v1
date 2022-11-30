# -*- coding: utf-8 -*-
'''
Created on 12 ago 2022

@author: mateosg
'''
from us.lsi.universo.Universo2D import Universo2D
from us.lsi.universo.Marco import Marco
from us.lsi.universo.Estrella import Estrella
from us.lsi.universo.Planeta import Planeta
from us.lsi.geometria.Punto2D import Punto2D
from us.lsi.universo.Cometa import Cometa
from us.lsi.universo.CometaAcelerado import CometaAcelerado
from us.lsi.universo.CometaErratico import CometaErratico

if __name__ == '__main__':
    
    m:Marco = Marco.of("Universo", 1200, 600, 'blue')
    universo= Universo2D.empty(m)
    
    sol = Estrella.of("Sol", 20, Punto2D.of(500., 300.))
    universo.agregar(sol)

    
    polar = Estrella.of("Polar", 20, Punto2D.of(800., 300.))
    universo.agregar(polar)
    
    tierra = Planeta.of_estrella("Tierra", sol)
    universo.agregar(tierra)
    
    luna=tierra.satelite("Luna")
    universo.agregar(luna)
    
    marte =Planeta.of_estrella("Marte", sol)
    universo.agregar(marte)
    
    zeus=Planeta.of_estrella("Zeus", polar)
    universo.agregar(zeus)
    
    cometa1=Cometa.random("cometa1", m.punto_aleatorio(0, 0))
    universo.agregar(cometa1)
    
    cometa_acel=CometaAcelerado.random("cometa2", m.punto_aleatorio(0, 0))
    universo.agregar(cometa_acel)
    
    cometa_err=CometaErratico.random("cometa3", m.punto_aleatorio(0, 0))
    universo.agregar(cometa_err)
    
    universo.simular()
    

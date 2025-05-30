'''
Created on 25 ago 2024

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.tipos_agregados.Grafo import Graph_type, Traverse_type
from us.lsi.tipos_agregados.Grafo import Grafo
from us.lsi.tipos_agregados.Ciudad import Ciudad
from us.lsi.tipos_agregados.Carretera import Carretera
from us.lsi.tools.File import lineas_de_fichero, absolute_path

class Mapa(Grafo[Ciudad,Carretera]):
    
    def __init__(self,graph_type:Graph_type,traverse_type:Traverse_type)->None:
        super().__init__(graph_type,lambda x: x.km,traverse_type)
        self.__ciudades_id:dict[str,Ciudad] = {}
               
    @staticmethod 
    def of(graph_type:Graph_type=Graph_type.UNDIRECTED,traverse_type:Traverse_type=Traverse_type.BACK)->Mapa:
        return Mapa(graph_type,traverse_type)
    
    @staticmethod
    def parse(f1:str,f2:str,graph_type:Graph_type=Graph_type.UNDIRECTED,traverse_type:Traverse_type=Traverse_type.BACK) -> Mapa: 
        m:Mapa = Mapa.of(graph_type,traverse_type)
        ciudades:set[Ciudad] = {Ciudad.parse(x) for x in lineas_de_fichero(absolute_path(f1))}
        for c in ciudades:
            assert c.nombre not in m.ciudades_id, f'Ciudad {c.nombre} repetida'
            m.ciudades_id[c.nombre] = c
            m.add_vertex(c)
        for linea in lineas_de_fichero(absolute_path(f2)):
            source,target,nombre,km = linea.split(',')
            sc:Ciudad = m.ciudades_id[source]
            tg:Ciudad = m.ciudades_id[target]
            cr:Carretera = Carretera.of(nombre,float(km))
            m.add_edge(sc,tg,cr)
        return m  
    
    @property
    def ciudades_id(self)->dict[str,Ciudad]:
        return self.__ciudades_id
    

if __name__ == '__main__':
    m:Mapa = Mapa.parse('ficheros/ciudades.txt','ficheros/carreteras.txt')
    print(m.vertex_set())  
#    print([c.nombre for c in m.neighbors(m.ciudades_id['Sevilla'])])
    m.plot_graph('Nuevo Grafo',vertex_label=lambda v:v.nombre[0:2],edge_label=lambda e:e.nombre,vertex_size=20,size_x=60,size_y=30) 
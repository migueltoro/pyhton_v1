'''
Created on 25 ago 2024

@author: migueltoro
'''


from __future__ import annotations
from typing import TypeVar, Callable
from enum import Enum
from us.lsi.tipos_agregados.Grafo_abstracto import Grafo_abstracto
import matplotlib.pyplot as plt
from networkx import Graph, DiGraph, spring_layout, draw, draw_networkx_edge_labels # type: ignore

V = TypeVar('V')
E = TypeVar('E')

class Graph_type(Enum):
    UNDIRECTED = 1
    DIRECTED = 2
    
class Traverse_type(Enum):
    FORWARD = 1
    BACK = 2

class Grafo(Grafo_abstracto[V,E]):
    
    def __init__(self,graph_type:Graph_type,weight:Callable[[E],float],traverse_type:Traverse_type=Traverse_type.FORWARD)->None:
        self._vertex_set:set[V] = set()
        self._edge_set:set[E] = set()
        self._edges_dict:dict[tuple[V,V],E] = {}
        self._neighbors:dict[V,set[V]] = {}
        self._predecessors:dict[V,set[V]] = {}
        self._sources:dict[E,V] = {}
        self._targets:dict[E,V] = {}
        self._graph_type = graph_type
        self._weight = weight
        self._traverse_type = traverse_type
     
    def __add_neighbors(self, source:V, target:V)->None:
        if source in self._neighbors:
            self._neighbors[source].add(target)
        else:
            self._neighbors[source] = {target}
            
    def __add_predecessors(self, source:V, target:V)->None:
        if source in self._predecessors:
            self._predecessors[source].add(target)
        else:
            self._predecessors[source] = {target}

    def add_edge(self,source:V,target:V,e:E)->None:
        assert source in self._vertex_set, f'Vertice {source} no esta en el grafo'
        assert target in self._vertex_set, f'Vertice {target} no esta en el grafo'
        assert source != target, f'No se pueden añadir bucles {source} - {target}'
        assert (source, target) not in self._edges_dict, f'La arista ya existe'
        self._edge_set.add(e)
        self._edges_dict[(source,target)] = e
        self.__add_neighbors(source,target)       
        self._sources[e] = source
        self._targets[e] = target 
        if self._graph_type == Graph_type.UNDIRECTED:
            self._edges_dict[(target,source)] = e 
            self.__add_neighbors(target,source)
        if self._graph_type == Graph_type.DIRECTED:
            self.__add_predecessors(target,source)
        
    
    def edge_weight(self,sourceVertex:V, targetVertex:V) -> float:
        return self._weight(self.edge(sourceVertex, targetVertex))
    
    def add_vertex(self,vertex:V)->bool:
        if vertex not in self._vertex_set:
            self._vertex_set.add(vertex)
            return True
        else:
            return False
    
    def edge_source(self,e:E)->V:
        return self._sources[e]
    
    def edge_target(self,e:E)->V:
        return self._targets[e]
    
    def vertex_set(self)->set[V]:
        return self._vertex_set
     
    def edge_set(self)->set[E]:
        return self._edge_set
    
    def contains_edge(self,sourceVertex:V, targetVertex:V)->bool:
        return (sourceVertex,targetVertex) in self._edges_dict   
     
    def neighbors(self,vertex:V)->set[V]:
        return self._neighbors.get(vertex,set())
    
    def predecessors(self,vertex:V)->set[V]:
        if self._graph_type == Graph_type.DIRECTED:
            return self._predecessors.get(vertex,set())
        else:
            return self._neighbors.get(vertex,set())
        
    def successors(self,vertex:V)->set[V]:
        return self.neighbors(vertex) if self._traverse_type == Traverse_type.FORWARD else self.predecessors(vertex)
    
    def edge(self,sourceVertex:V, targetVertex:V) -> E:
        return self._edges_dict[(sourceVertex,targetVertex)]
            
    def vertex_list(self)->list[V]:
        return list(self._vertex_set)
    
    def graph_type(self)->Graph_type:
        return self._graph_type
    
    def traverse_type(self)->Traverse_type:
        return self._traverse_type
    
    def weight(self)->Callable[[E],float]:
        return self._weight
    
    def inverse_graph(self)->Grafo[V,E]:
        if self._graph_type == Graph_type.DIRECTED:
            return self
        g:Grafo[V,E] = Grafo(self.graph_type(),self.weight())
        for v in self.vertex_set():
            g.add_vertex(v)
        for e in self.edge_set():
            source = self.edge_source(e)
            target = self.edge_target(e)
            g.add_edge(target,source,e)
        return g
    
    def subgraph(self,vertices:set[V]) -> Grafo[V,E]:
        g:Grafo[V,E] = Grafo(self.graph_type(),self.weight(),self.traverse_type())
        for v in vertices:
            g.add_vertex(v)
        for e in self.edge_set():
            s = self.edge_source(e)
            t = self.edge_target(e)
            if s in vertices and t in vertices:
                g.add_edge(s,t,e)
        return g
    
    def plot_graph(self,titulo: str = "Grafo",
                   vertex_label: Callable[[V], str] = str, 
                   edge_label: Callable[[E], str] = str,
                   vertex_size:int=300,
                   size_x:int=10,
                   size_y:int=10) -> None:
        # Create an empty networkx graph
        g:Graph = DiGraph() if self._graph_type == Graph_type.DIRECTED else Graph()

    
        # Add vertices to the graph
        labels = {}
        for vertex in self._vertex_set:
            g.add_node(vertex)
            labels[vertex] = vertex_label(vertex)
    
        # Add edges to the graph
        edge_labels: dict = {}
        for edge in self._edge_set:
            source = self.edge_source(edge)
            target = self.edge_target(edge)
            g.add_edge(source, target)
            edge_labels[(source, target)] = edge_label(edge)
    
        # Plot the graph using matplotlib
        plt.figure(figsize=(size_x, size_y))  # You can adjust the size
        pos = spring_layout(g)  # Layout for node positioning
        draw(g, pos, with_labels=True, labels=labels, node_size=vertex_size, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray")
        draw_networkx_edge_labels(g, pos,  edge_labels=edge_labels, font_size=8, font_color="red")
        # Show the plot
        plt.title(titulo)
        plt.show()
            
    def __str__(self):
        sep = '\n'
        return f'Vertices: \n{sep.join(str(x) for x in self._vertex_set)} \nAristas: \n{sep.join(str(x) for x in self._edge_set)}'

if __name__ == '__main__':
    pass
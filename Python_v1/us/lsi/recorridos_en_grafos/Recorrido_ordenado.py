'''
Created on 25 ago 2024

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar
from us.lsi.tipos_agregados.Grafo import Grafo
from us.lsi.tipos_agregados.Cola_de_prioridad import Cola_de_prioridad
from us.lsi.recorridos_en_grafos.Recorrido import Recorrido

V = TypeVar('V')
E = TypeVar('E')


class Recorrido_ordenado(Recorrido[V,E]):
    
    @staticmethod
    def of(grafo:Grafo[V,E])->Recorrido_ordenado[V,E]:
        return Recorrido_ordenado(grafo)
    
    def __init__(self,grafo:Grafo[V,E])->None:
        super().__init__(grafo)
 
   
    def traverse(self,source:V)->None:
        v:V = source
        q:Cola_de_prioridad[V,float] = Cola_de_prioridad.of()
        q.add(v,0.)
        self._tree[v] = (None,0)
        while not q.is_empty():
            v = q.remove()
            self._path.append(v)
            w = self._tree[v][1]
            for neighbor in self._grafo.successors(v):
                nbw = w + self._grafo.edge_weight(v, neighbor) 
                if neighbor not in self._tree:
                    self._tree[neighbor] = (v, nbw) 
                    q.add(neighbor,nbw)                    
                else:
                    if nbw < self._tree[neighbor][1]:
                        self._tree[neighbor] = (v, nbw)
                        q.decrease_priority(neighbor, nbw)

if __name__ == '__main__':
    pass
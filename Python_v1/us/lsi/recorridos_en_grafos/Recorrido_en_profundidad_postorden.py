'''
Created on 8 sept 2024

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar
from us.lsi.tipos_agregados.Grafo import Grafo
from us.lsi.tipos_agregados.Pila import Pila
from us.lsi.recorridos_en_grafos.Recorrido import Recorrido

V = TypeVar('V')
E = TypeVar('E')


class Recorrido_en_profundidad_postorden(Recorrido[V,E]):
    
    @staticmethod
    def of(grafo:Grafo[V,E])->Recorrido_en_profundidad_postorden[V,E]:
        return Recorrido_en_profundidad_postorden(grafo)
    
    def __init__(self,grafo:Grafo[V,E])->None:
        super().__init__(grafo)
    
    
    def traverse(self,source:V)->None:
        v:V = source
        q:Pila[V] = Pila.of()
        q.add(v)
        q2:Pila[V] = Pila.of()
        self._tree[v] = (None,0)
        while not q.is_empty():
            v = q.remove()
            q2.add(v)           
            for neighbor in self._grafo.successors(v):
                if neighbor not in self._tree:
                    q.add(neighbor)
                    self._tree[neighbor] = (v, self._tree[v][1] + 1)         
        while not q2.is_empty():
            v = q2.remove()
            self._path.append(v)

if __name__ == '__main__':
    pass
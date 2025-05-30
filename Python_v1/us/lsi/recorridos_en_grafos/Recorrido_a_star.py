'''
Created on 8 sept 2024

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar, Callable
from us.lsi.recorridos_en_grafos.Recorrido import Recorrido
from us.lsi.tipos_agregados.Grafo import Grafo
from us.lsi.tipos_agregados.Cola_de_prioridad import Cola_de_prioridad

V = TypeVar('V')
E = TypeVar('E')


class Recorrido_a_star(Recorrido[V,E]):
    
    @staticmethod
    def of(grafo:Grafo[V,E],end:V,p:Callable[[V],bool],heuristic:Callable[[V,V,Callable[[V],bool]],float])->Recorrido_a_star[V,E]:
        return Recorrido_a_star(grafo,end,p,heuristic)
    
    def __init__(self,grafo:Grafo[V,E],end:V,p:Callable[[V],bool],heuristic:Callable[[V,V,Callable[[V],bool]],float])->None:
        super().__init__(grafo)
        self._heuristic:Callable[[V,V,Callable[[V],bool]],float] = heuristic
        self._end = end
        self._p = p
   
    def __estimated_weight_to_end(self,actual:V,actual_weight:float)->float:
        return actual_weight+self._heuristic(actual,self._end,self._p)
   
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
                ewe:float = self.__estimated_weight_to_end(neighbor,nbw)
                if neighbor not in self._tree:
                    self._tree[neighbor] = (v, nbw) 
                    q.add(neighbor,ewe)                    
                else:
                    if nbw < self._tree[neighbor][1]:
                        self._tree[neighbor] = (v, nbw)
                        q.decrease_priority(neighbor, ewe)
                if self._p(neighbor):
                    break

if __name__ == '__main__':
    pass
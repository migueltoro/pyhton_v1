'''
Created on 25 ago 2024

@author: migueltoro
'''

from __future__ import annotations
from typing import Generic, TypeVar, Optional
from abc import ABC, abstractmethod
from us.lsi.tipos_agregados.Grafo import Grafo

V = TypeVar('V')
E = TypeVar('E')

class Recorrido(ABC,Generic[V,E]):
    
    def __init__(self,grafo:Grafo[V,E])->None:
        self._tree:dict[V,tuple[Optional[V],float]] = {}
        self._path:list[V] = []
        self._grafo = grafo        
           
    def path(self)->list[V]:
        return self._path
    
    def tree(self)->dict[V,tuple[Optional[V],float]]:
        return self._tree
    
    def path_to_origin(self,source:V)->list[V]:
        ls:list[V] = []
        v:V = source
        ls.append(v)
        nxt:tuple[Optional[V],float] = self._tree[v]
        while nxt[0] is not None:
            v = nxt[0]
            ls.append(v)
            nxt = self._tree[v]
        return ls
    
    def path_from_origin(self,source:V)->list[V]:
        ls:list[V] = []
        v:V = source
        ls.append(v)
        nxt:tuple[Optional[V],float] = self._tree[v]
        while nxt[0] is not None:
            v = nxt[0]
            ls.insert(0,v)
            nxt = self._tree[v]
        return ls 
    
    def path_weight(self,source:V)->float:
        return self._tree[source][1] 
    
    
    def origin(self,source:V)->V:
        v:V = source
        nxt:tuple[Optional[V],float] = self._tree[v]
        while nxt[0] is not None:
            v = nxt[0]
            nxt = self._tree[v]
        return  v
    
    def path_edges(self,source:V)->list[E]:
        path:list[V] = self.path_from_origin(source)
        ls:list[E] = []
        for i in range(len(path)-1):
            ls.append(self._grafo.edge(path[i], path[i+1]))
        return ls
    
    @abstractmethod
    def traverse(self,source:V)->None:
        pass
    
    def traverse_all(self)->None:
        all_elements:set[V] = {v for v in self._grafo.vertex_set()}
        while len(all_elements) > 0:
            v:V = all_elements.pop()
            self.traverse(v)
            all_elements = all_elements - self._tree.keys()
            
    def groups(self)->dict[V,set[V]]:
        all_elements:set[V] = self._grafo.vertex_set()
        r:dict[V,set[V]] = {}
        for v in all_elements:
            org:V = self.origin(v)
            if org in r:
                r[org].add(v)
            else:
                r[org] = {v}
        return r
    
    def groups_list(self)->list[set[V]]:
        return list(self.groups().values())
    
    def path_exist(self,source:V,target:V)->bool:
        return self.origin(source) == self.origin(target)

if __name__ == '__main__':
    pass
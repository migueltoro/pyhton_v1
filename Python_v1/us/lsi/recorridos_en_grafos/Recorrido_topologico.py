'''
Created on 8 sept 2024

@author: migueltoro
'''

from __future__ import annotations
from typing import TypeVar 
from us.lsi.tipos_agregados.Grafo import Grafo
from us.lsi.recorridos_en_grafos.Recorrido_en_profundidad_postorden import Recorrido_en_profundidad_postorden

V = TypeVar('V')
E = TypeVar('E')


class Recorrido_topologico(Recorrido_en_profundidad_postorden[V,E]):
    
    @staticmethod
    def of(grafo:Grafo[V,E])->Recorrido_topologico[V,E]:
        return Recorrido_topologico(grafo)
    
    def __init__(self,grafo:Grafo[V,E])->None:
        super().__init__(grafo)
      
    def traverse(self,source:V)->None:
        super().traverse(source)
        self._path.reverse()

if __name__ == '__main__':
    pass
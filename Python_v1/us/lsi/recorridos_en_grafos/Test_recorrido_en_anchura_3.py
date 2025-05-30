'''
Created on 31 ago 2024

@author: migueltoro
'''

from us.lsi.tipos_agregados.Carretera import Carretera
from us.lsi.tipos_agregados.Ciudad import Ciudad
from us.lsi.tipos_agregados.Mapa import Mapa
from us.lsi.recorridos_en_grafos.Recorrido_en_anchura import Recorrido_en_anchura
from us.lsi.tipos_agregados.Grafo import Graph_type, Traverse_type


if __name__ == '__main__':
    m:Mapa = Mapa.parse('ficheros/ciudades.txt','ficheros/carreteras.txt',Graph_type.DIRECTED, Traverse_type.BACK)
    r:Recorrido_en_anchura[Ciudad,Carretera] = Recorrido_en_anchura.of(m)
#    rm:Ciudad = m.ciudades_id['Roma']
#    print(m)
    r.traverse(m.ciudades_id['Almeria'], )
    print(r.path())
    '''
    sep = '\n'
    print(sep.join(f'{v} -- {m.predecessors(v)}'  for v in m.vertex_set()))
    print(len([c.nombre for c in r.path()]))
    print(sep.join(f'{v} -- {m.neighbors(v)}'  for v in m.vertex_set()))
    '''
'''
Created on 29 ago 2024

@author: migueltoro
'''

from us.lsi.tipos_agregados.Carretera import Carretera
from us.lsi.tipos_agregados.Ciudad import Ciudad
from us.lsi.tipos_agregados.Mapa import Mapa
from us.lsi.recorridos_en_grafos.Recorrido_en_anchura import Recorrido_en_anchura


if __name__ == '__main__':
    m:Mapa = Mapa.parse('ficheros/ciudades_2.txt','ficheros/carreteras_2.txt')
    r:Recorrido_en_anchura[Ciudad,Carretera] = Recorrido_en_anchura.of(m)
#    rm:Ciudad = m.ciudades_id['Roma']
#    print(m)
    r.traverse_all() 
#    print([c.nombre for c in r.path()])
    d = r.groups()
    print(len(d))
    print([(k.nombre,len(d[k])) for k in d.keys()])
    print(len(r.groups()))
    print(m.subgraph(d[m.ciudades_id['KHSAm']]))
    print({v.nombre for v in m.vertex_set() if len(m.predecessors(v))==0})
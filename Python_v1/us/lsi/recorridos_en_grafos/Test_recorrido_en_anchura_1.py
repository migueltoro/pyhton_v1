'''
Created on 26 ago 2024

@author: migueltoro
'''

from us.lsi.tipos_agregados.Carretera import Carretera
from us.lsi.tipos_agregados.Ciudad import Ciudad
from us.lsi.tipos_agregados.Mapa import Mapa
from us.lsi.recorridos_en_grafos.Recorrido_en_anchura import Recorrido_en_anchura

if __name__ == '__main__':
    m:Mapa = Mapa.parse('ficheros/ciudades.txt','ficheros/carreteras.txt')
#    print(m)
    r:Recorrido_en_anchura[Ciudad,Carretera] = Recorrido_en_anchura.of(m)
    r.traverse_all( )
    print(len(r.groups()))
    print([x.nombre for x in r.groups().keys()])
    print(r.path())
    print(r.path())
    h:Ciudad = m.ciudades_id['Huelva']
    print(r.origin(h))
    c:Ciudad = m.ciudades_id['Cordoba']
    print(r.origin(c))
    a:Ciudad = m.ciudades_id['Almeria']
    print(r.origin(c))
#    print(r.path_weight(c))
#    print([x.nombre for x in r.path_from_origin(c)])
    ln:Ciudad = m.ciudades_id['Londres']
    print(r.origin(ln))
    rm:Ciudad = m.ciudades_id['Roma']
    print(r.origin(rm))
    pr:Ciudad = m.ciudades_id['Paris']
    print(r.origin(pr))
    print(r.path_exist(h, c ))
    print(r.path_exist(h, ln ))
    print(r.path_exist(h, a ))
    g = r.groups_list()
    print('Group 0  ______________')
    print(g[0])
    print('Group 1 ______________')
    print(g[1])
    print('Subgraph ______________')
    sg = m.subgraph(g[1])
    print(sg)
    r2:Recorrido_en_anchura[Ciudad,Carretera]  = Recorrido_en_anchura.of(sg)
    r2.traverse_all()
    print('______________')
#    print(r2.origin(ln))
    print(r2.origin(ln))
    print(r2.origin(pr))
    print('______________')
    print(r2.groups())
    print(r2.path())
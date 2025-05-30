'''
Created on 8 sept 2024

@author: migueltoro
'''

from us.lsi.tipos_agregados.Carretera import Carretera
from us.lsi.tipos_agregados.Ciudad import Ciudad
from us.lsi.tipos_agregados.Mapa import Mapa
from us.lsi.recorridos_en_grafos.Recorrido_a_star import Recorrido_a_star

if __name__ == '__main__':
    m:Mapa = Mapa.parse('ficheros/ciudades.txt','ficheros/carreteras.txt')
    ce:Ciudad = m.ciudades_id['Almeria']
    p = lambda x: x == ce
    r:Recorrido_a_star[Ciudad,Carretera] = Recorrido_a_star.of(m,ce,p,lambda x,y,z: 0.)
    r.traverse(m.ciudades_id['Sevilla'])
    print([x.nombre for x in r.path_from_origin(ce)])
    print([x.nombre for x in r.path_edges(ce)])
    print(r.path_weight(ce))

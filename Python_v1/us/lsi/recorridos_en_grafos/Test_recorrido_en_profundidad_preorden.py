'''
Created on 26 ago 2024

@author: migueltoro
'''

from us.lsi.tipos_agregados.Carretera import Carretera
from us.lsi.tipos_agregados.Ciudad import Ciudad
from us.lsi.tipos_agregados.Mapa import Mapa
from us.lsi.recorridos_en_grafos.Recorrido_en_profundidad_preorden import Recorrido_en_profundidad_preorden

if __name__ == '__main__':
    m:Mapa = Mapa.parse('ficheros/ciudades.txt','ficheros/carreteras.txt')
    r:Recorrido_en_profundidad_preorden[Ciudad,Carretera] = Recorrido_en_profundidad_preorden.of(m)
    r.traverse(m.ciudades_id['Sevilla'])
    print([x.nombre for x in r.path()])
    c:Ciudad = m.ciudades_id['Huelva']
    print(r.origin(c))
    c = m.ciudades_id['Cordoba']
    print(r.origin(c))
    c = m.ciudades_id['Almeria']
    print(r.origin(c))
    '''
    print(r.path_weight(c))
    print([x.nombre for x in r.path_from_origin(c)])
    print([x.nombre for x in r.path()])
    '''

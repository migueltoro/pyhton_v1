'''
Created on 16 sept 2022

@author: migueltoro
'''

from us.lsi.tools.Iterable import strfiter
from us.lsi.tools.Dict import strfdict

jugador: tuple[str,str,int] = ("Mark", "Lenders", 15) 
rango = range(10,20)
temperaturas:list[int] = [32, 36, 35, 36, 32, 33] 
temperaturas_conjunto: set[int] = {32,36,35,36,32,33,34} 
temperaturas_por_provincias:dict[str,float] = {"Almeria":19.9, "Cadiz": 19.1, "Cordoba": 19.1, 
                                               "Granada": 16.6, "Jaen": 18.2, "Huelva": 19.0,  "Malaga": 19.8, "Sevilla": 20.0} 
kt:set[str]= set(temperaturas_por_provincias.keys())
kv:set[float]= set(temperaturas_por_provincias.values()) 
tp:set[tuple[str,float]] = set(temperaturas_por_provincias.items())


if __name__ == '__main__':
    print("Nombre:", jugador[0]) 
    print("Apellidos:", jugador[1]) 
    print("Edad:", jugador[2])
#    jugador[2] = 16
    print('---------------')
    print(rango)
    print(rango[2])
    print(list(rango))
    print('---------------')
    print(temperaturas)
    print("Temperatura lunes:", temperaturas[0])
    temperaturas[1] = 35 
    print(temperaturas)
    print(temperaturas_conjunto)
    print(strfiter(temperaturas,sep=';'))
    print('---------------')
    print(temperaturas_por_provincias)
    print("Temperatura en Sevilla:", temperaturas_por_provincias["Sevilla"]) 
    temperaturas_por_provincias["Sevilla"] = 21.0 
    print(temperaturas_por_provincias)
    print(strfdict(temperaturas_por_provincias,sep='\n'))
    print('---------------')
    print(kt)
    print(kv)
    print(tp)
    print('---------------')
    temperaturas.append(29) 
    temperaturas_conjunto.add(29) 
    temperaturas_por_provincias["Badajoz"] = 15.8
    print(temperaturas)
    print(temperaturas_conjunto)
    print(temperaturas_por_provincias) 
    
    
    
    
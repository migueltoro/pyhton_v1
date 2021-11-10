'''
Created on 10 nov 2021

@author: migueltoro
'''

from us.lsi.tools.Iterable import str_iterable
from us.lsi.coordenadas.Coordenadas2D import Coordenadas2D
from us.lsi.tools import File
from us.lsi.tools import String
from enum import Enum

class TipoMapa(Enum):
    Google = 1
    Bing = 2
    
def tipoMapa()->TipoMapa:
    return TipoMapa.Google

def toPointGoogle(coordenadas:Coordenadas2D)->str:
    r = "lat: {0:11.6f}, lng: {1:11.6f}".format(coordenadas.latitud,coordenadas.longitud)
    return '{'+r+'}'

def n()->int:
    n = 0
    yield n
    n = n+1

def toMarkerGoogle(n:int,color:str, text:str,coordenadas:Coordenadas2D)->str:
        url = "\"http://maps.google.com/mapfiles/ms/icons/"+color+"-dot.png\""
        lat = coordenadas.latitud
        lng = coordenadas.longitud
        position_text = '{{lat: {0:11.6f}, lng: {1:11.6f}}}'.format(lat,lng)
        return "marker{0:d} = new google.maps.Marker({{ \r\
                       map: map, \r\
                       position: {1:s}, \r\
                       title: '{2:s}' , \r\
                       icon: {{ url: {3:s} }} \r\
                       }});".format(n,position_text,text,url)

def getKeyGoogle()->str:
    return File.lineas_de_fichero(
        "C:/Users/migueltoro/OneDrive - UNIVERSIDAD DE SEVILLA/Escritorio/Jars/Keys/privateGoogle.txt")[0]
    
def getPolylinePatternGoogle()->str:
    return File.texto_de_fichero("../../../resources/GooglePolylinePattern.html")
    
def getMarkersPatternGoogle()->str:
    return File.texto_de_fichero("../../../resources/GoogleMarkersPattern.html")

def toPoint(coordenadas: Coordenadas2D)->str:
    if tipoMapa() == TipoMapa.Google:
        return toPointGoogle(coordenadas)
    else:
        pass
        
def toMarker(n:int,color:str, text:str, coordenadas:Coordenadas2D)->str:
    if tipoMapa() == TipoMapa.Google:
        return toMarkerGoogle(n,color,text,coordenadas)
    else:
        pass

def getKey()->str:
    if tipoMapa() == TipoMapa.Google:
        return getKeyGoogle()
    else:
        pass

def getPolylinePattern()->str:
    if tipoMapa() == TipoMapa.Google:
        return getPolylinePatternGoogle()
    else:
        pass

def getMarkersPattern()->str:
    if tipoMapa() == TipoMapa.Google:
        return getMarkersPatternGoogle()
    else:
        pass
    
def polyline(fileOut:str, ubicaciones:list[Coordenadas2D])-> None:
        center = Coordenadas2D.center(ubicaciones)
        result = getPolylinePattern()
        ub = (toPoint(x) for x in ubicaciones)
        polylineText = str_iterable(ub,",\n","\n[", "]\n")
        centerText = toPoint(center);
        markerCenterText = toMarker(0,"red","C",center);
        markerBeginText = toMarker(1,"red","S",ubicaciones[0])
        markerEndText = toMarker(2,"red","E",ubicaciones[-1])
        keyText = getKey()
        reglas = {}
        reglas["center"] = centerText
        reglas["markerbegin"] = markerBeginText
        reglas["markerend"] = markerEndText
        reglas["markercenter"] = markerCenterText
        reglas["polyline"] = polylineText
        reglas["key"] = keyText
        result = String.transform(result,reglas);
        File.write(fileOut,result);


def markers(fileOut:str, markerColor:str, ubicaciones:list[Coordenadas2D])->None:
        center = Coordenadas2D.center(ubicaciones)
        result = getMarkersPattern();
        ub = (toMarker(markerColor,"E",x) for x in ubicaciones)
        markersText = str_iterable(ub,"\n","\n", "\n")
        centerMarkerText = toMarker("red","C",center)
        centerText = toPoint(center)
        keyText = getKey()
        reglas = {}
        reglas["center"] = centerText
        reglas["markercenter"] = centerMarkerText
        reglas["markers"] = markersText
        reglas["key"] = keyText
        result = String.transform(result,reglas)
        File.write(fileOut,result)

    

if __name__ == '__main__':
    pass
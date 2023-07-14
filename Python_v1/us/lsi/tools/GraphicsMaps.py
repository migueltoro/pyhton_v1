'''
Created on 10 nov 2021

@author: migueltoro
'''

from us.lsi.tools.Iterable import str_iter
from us.lsi.coordenadas.Coordenadas2D import Coordenadas2D
from us.lsi.tools import File
from us.lsi.tools import String
from enum import Enum


class TipoMapa(Enum):
    Google = 1
    Bing = 2
    
tipo: TipoMapa = TipoMapa.Google

def set_tipo(ntipo:TipoMapa)->None:
    global tipo
    tipo = ntipo
    
def get_tipo()->TipoMapa:
    global tipo
    return tipo

n:int = 0

def nv():
    global n
    n = n +1
    return n

def toPointGoogle(coordenadas:Coordenadas2D)->str:
    return  "{{ lat: {0:11.6f}, lng: {1:11.6f} }}".format(coordenadas.latitud,coordenadas.longitud)

def toMarkerGoogle(color:str, text:str,coordenadas:Coordenadas2D)->str:
        url = "\"http://maps.google.com/mapfiles/ms/icons/"+color+"-dot.png\""
        lat = coordenadas.latitud
        lng = coordenadas.longitud
        position_text = '{{lat: {0:11.6f}, lng: {1:11.6f}}}'.format(lat,lng)
        return "marker{0:d} = new google.maps.Marker({{ \r\
                       map: map, \r\
                       position: {1:s}, \r\
                       title: '{2:s}' , \r\
                       icon: {{ url: {3:s} }} \r\
                       }});".format(nv(),position_text,text,url)

def getKeyGoogle()->str:
    return File.lineas_de_fichero(
        "C:/Users/migueltoro/OneDrive - UNIVERSIDAD DE SEVILLA/Escritorio/Jars/Keys/privateGoogle.txt")[0]
    
def getPolylinePatternGoogle()->str:
    return File.read("../../../resources/GooglePolylinePattern.html")
    
def getMarkersPatternGoogle()->str:
    return File.read("../../../resources/GoogleMarkersPattern.html")

def toPointBing(coordenadas:Coordenadas2D)->str:
    return "new Microsoft.Maps.Location({0:11.6f},{1:11.6f})".format(coordenadas.latitud,coordenadas.longitud)

def toMarkerBing(color:str, text:str, coordenadas:Coordenadas2D)->str:
        lat = coordenadas.latitud
        lng = coordenadas.longitud
        n = nv()
        return "var pin{0:d} = new Microsoft.Maps.Pushpin(new Microsoft.Maps.Location({1:11.6f},{2:11.6f},{{\
        color:'{3:s}',\
        text:'{4:s}'}});\n\
        map.entities.push(pin{0:d});".format(n,lat,lng,color,text)

def getKeyBing()->str:
    return File.lineas_de_fichero("C:/Users/migueltoro/OneDrive - UNIVERSIDAD DE SEVILLA/Escritorio/Jars/Keys/privateBing.txt")[0]

def getPolylinePatternBing()->str:
    return File.read("../../../resources/BingPolylinePattern.html")

def getMarkersPatternBing()->str:
    return File.read("../../../resources/BingMarkersPattern.html")


def toPoint(coordenadas: Coordenadas2D)->str:
    if get_tipo() == TipoMapa.Google:
        return toPointGoogle(coordenadas)
    else:
        return toPointBing(coordenadas)
        
def toMarker(color:str, text:str, coordenadas:Coordenadas2D)->str:
    if get_tipo() == TipoMapa.Google:
        return toMarkerGoogle(color,text,coordenadas)
    else:
        return toMarkerBing(color,text,coordenadas)

def getKey()->str:
    if get_tipo() == TipoMapa.Google:
        return getKeyGoogle()
    else:
        return getKeyBing()

def getPolylinePattern()->str:
    if get_tipo() == TipoMapa.Google:
        return getPolylinePatternGoogle()
    else:
        return getPolylinePatternBing()

def getMarkersPattern()->str:
    if get_tipo() == TipoMapa.Google:
        return getMarkersPatternGoogle()
    else:
        return getMarkersPatternBing()
    
def polyline(fileOut:str, ubicaciones:list[Coordenadas2D])-> None:
        center = Coordenadas2D.center(ubicaciones)
        result = getPolylinePattern()
        ub = (toPoint(x) for x in ubicaciones)
        polylineText = str_iter(ub,",\n","\n[", "]\n")
        centerText = toPoint(center);
        markerCenterText = toMarker("red","C",center);
        markerBeginText = toMarker("red","S",ubicaciones[0])
        markerEndText = toMarker("red","E",ubicaciones[-1])
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
        markersText = str_iter(ub,"\n","\n", "\n")
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
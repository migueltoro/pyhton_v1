'''
Created on 10 nov 2021

@author: migueltoro
'''

from us.lsi.tools.GraphicsMaps import n

if __name__ == '__main__':
    n = 5
    position_text = '0000'
    text = 'titulo'
    url = 'http://miguel'
    print('''marker{0:d} = new google.maps.Marker({{\r\
                       map: map, \r\
                       position: {1:s}, \r\
                       title: '{2:s}' , \r\
                       icon: {{ url: {3:s} }} \r\
                       }});'''.format(n,position_text,text,url,'{','}'))
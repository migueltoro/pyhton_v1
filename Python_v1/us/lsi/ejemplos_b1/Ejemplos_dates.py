'''
Created on 16 sept 2022

@author: migueltoro
'''

from datetime import datetime, date, time, timedelta 
import locale

actual:datetime = datetime.now() 
otro: datetime = datetime(2022,3,27)
anyo:int = actual.year
hora: int = actual.hour 
mes:int = actual.month 

d1:datetime = datetime.now() 
t:timedelta = timedelta(days=43,hours=23,seconds=5) 
d2:datetime = d1+t 
 
d3: date = actual.date() 
d4: time = actual.time() 

dt_str = '2018-06-29 17:08:00' 
dt:datetime = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S') 

d3 = datetime.strptime('2/2/2002','%d/%m/%Y').date() 
t1:time = datetime.strptime('00:00:30','%H:%M:%S').time()
t2:time = datetime.strptime('00:00:40','%H:%M:%S').time()

if __name__ == '__main__':
    print(actual)
    print(mes)  
    print(anyo)  
    print(otro) 
    print(otro > actual)
    
    print(d1.year) 
    print(d1.month) 
    print(d1.hour) 
    print(d1.second) 
    print((d2-d1).seconds)
    print(d3) 
    print(d4)
    
    print(dt.strftime('%d/%m/%Y -- %H:%M:%S')) 
    print(dt.strftime('%A %d de %B del %Y -- %H:%M:%S'))  
    locale.setlocale(locale.LC_TIME, 'es_ES') 
    print(dt.strftime('%A %d de %B del %Y -- %H:%M:%S')) 
    print(datetime.strftime(d1,'%A %d de %B del %Y -- %H:%M:%S')) 
    print(t1.strftime('%H:%M:%S'))
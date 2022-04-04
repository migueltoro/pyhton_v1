'''
Created on 15 jul. 2020

@author: migueltoro
'''

from datetime import datetime, timedelta, time, date

def parse_date(s:str,ft = "%d/%m/%Y") -> date:
    return datetime.strptime(s, ft).date()

def str_date(s:datetime,ft = "%d/%m/%Y") -> str:
    return date.strftime(s, ft)

def parse_time(s:str,ft = '%H:%M:%S') -> time:
    return datetime.strptime(s, ft).time()

def str_time(s:datetime,ft = '%H:%M:%S') -> str:
    return time.strftime(s, ft)

def to_datetime(t:time) -> datetime:
    return datetime.combine(date.min,t)

if __name__ == '__main__':
    d1 = datetime.now()
    t = timedelta(days=43,hours=23,seconds=5)
    d2 = d1+t
    print(d1)
    print(d1.year)
    print(d1.month)
#    print(d1.hour)
#    print(d1.second)
    print(d2)
    print(d2.year)
    print(d2.month)
#    print(d2.hour)
#    print(d2.second)
    print(str_date(d1))
    print(str_date(parse_date('2/2/2002')))
    t1 = parse_time('00:00:30','%H:%M:%S')
    print(str_time(t1))
    t2 = parse_time('00:00:40','%H:%M:%S')
    print(str_time(t2))
    print((to_datetime(t2)-to_datetime(t1)).seconds)
    print((d2-d1).seconds)
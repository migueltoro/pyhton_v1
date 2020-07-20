'''
Created on 15 jul. 2020

@author: migueltoro
'''

from datetime import datetime
from datetime import timedelta

def parse_date(s:str,ft = "%d/%m/%Y") -> datetime:
    return datetime.strptime(s, ft).date()

def str_date(s:datetime,ft = "%d/%m/%Y") -> str:
    return datetime.strftime(s, ft)

if __name__ == '__main__':
    d = datetime.now()
    t = timedelta(days=43,hours=23,seconds=5)
    d2 = d+t
    print(d)
    print(d.year)
    print(d.month)
    print(d.hour)
    print(d.second)
    print(d2)
    print(d2.year)
    print(d2.month)
    print(d2.hour)
    print(d2.second)
    print(str_date(d.date()))
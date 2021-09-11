'''
Created on 25 jul. 2020

@author: migueltoro
'''

from typing import TypeVar, Dict, List, Union, Iterable
from us.lsi.tools.Iterable import flat,grouping_list


K = TypeVar('K')
V = TypeVar('V')



def invert_dict(d:Dict[K,Union[V,Iterable[V]]]) -> Dict[V,List[K]]:
    fl = ((k,nv)  for k,v in d.items()  for nv in flat(v))
    return grouping_list(fl,fkey=lambda e:e[1],fvalue=lambda e:e[0])

if __name__ == '__main__':
    d = {2:'a',3:['a','b'],5:'b'}
    print(d)
    print(invert_dict(d))
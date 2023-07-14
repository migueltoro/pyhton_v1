'''
Created on 18 sept 2022

@author: migueltoro
'''

import random
from us.lsi.tools.Dict import str_dict
from us.lsi.tools.Iterable import grouping_set,grouping_reduce, grouping_list,groups_size

it: list[int] = [random.randint(0,100) for _ in range(0,200)]
g1:dict[int,set[int]]=grouping_set(it,key=lambda x:x%7)
g2:dict[int,list[int]]=grouping_list(it,key=lambda x:x%7)
g3:dict[int,int]=groups_size(it,key=lambda x:x%7)
g4:dict[int,int] = grouping_reduce(it,key=lambda x:x%7,op=lambda x,y:x+y)
g5:dict[int,int] = grouping_reduce(it,key = lambda x: x%7, op = lambda x,y: min(x,y))


if __name__ == '__main__':
    print(str_dict(g1))
    print('_____')
    print(str_dict(g2))
    print('_____')
    print(str_dict(g3))
    print('_____')
    print(str_dict(g4))
    print('_____')
    print(str_dict(g5))


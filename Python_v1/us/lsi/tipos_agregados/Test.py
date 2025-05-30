'''
Created on 23 ago 2024

@author: migueltoro
'''

from __future__ import annotations
from us.lsi.tipos_agregados.Cola import Cola

if __name__ == '__main__':
    cl:Cola[int] = Cola.of()
    cl.add_all([1,2,3,4,5])
#    print(cl.remove_all())
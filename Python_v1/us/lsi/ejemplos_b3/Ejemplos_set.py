'''
Created on 6 nov 2022

@author: migueltoro
'''

a = {1, 2, 3, 4, 5, 6}
b = {4, 5, 6, 7, 8}

if __name__ == '__main__':
    print("Unión:", a | b)
    print("Intersección:", a & b)
    print("Diferencia:", a - b)
    print("Diferencia simétrica:", a ^ b)
    print({7,8,1,2,3} == a ^ b)
    print(2 in b-a)
    print(a & b >= a | b)
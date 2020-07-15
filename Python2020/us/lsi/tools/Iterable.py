'''
Created on 15 jul. 2020

@author: migueltoro
'''

def str_iterable(iterable,ft=str,sep=',',pf='{',sf='}'):
    return '{}{}{}'.format(pf,sep.join(ft(x) for x in iterable),sf)

def average(iterable):
        s = 0
        n = 0
        for x in iterable:
            s = s + x 
            n = n+1
        return s/n

def unique_values(iterable):
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item 
            
def limit(iterable,n):
        s = zip(iterable,range(n))
        return (x for x,_ in s)
    
def flat_map(iterable):
        return (y for x in iterable for y in x)
    
def joining(iterable,tostring=str,separator='\n',prefix='',suffix=''):
        return '{0}{1}{2}'.format(prefix,separator.join(tostring(x) for x in  iterable),suffix)
    

if __name__ == '__main__':
    print(str_iterable(flat_map([[0,1],[2,3,4],[5,6],[9]])))
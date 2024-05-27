'''
Created on 27 oct 2023

@author: migueltoro
'''

from __future__ import annotations
from typing import Callable, TypeVar, Iterable, Any
from us.lsi.tools.File import absolute_path, dict_de_csv
from us.lsi.tools.Iterable import grouping_reduce
from us.lsi.tools.Types import Comparable
import operator
from datetime import date, datetime
from us.lsi.tools.Preconditions import check_argument
from us.lsi.dataframe.Persona import Persona
from dataclasses import asdict

E = TypeVar('E', bound=Comparable)
R = TypeVar('R')


class DataFrame():
    
    def __init__(self, data:dict[str,list[str]])->None:
        self.__data:dict[str,list[str]] = data
        
    @staticmethod
    def of(colum_names:list[str],rows:list[list[str]])->DataFrame:
        data:dict[str,list[str]] = {colum_names[i]:[rows[j][i] for j in range(0,len(rows))] for i in range(0,len(colum_names))}
        return DataFrame(data)
        
    @staticmethod
    def of_dict(data:dict[str,list[str]])->DataFrame:
        return DataFrame(data)
    
    @staticmethod
    def parse(file:str)->DataFrame:
        data:dict[str,list[str]] = dict_de_csv(absolute_path(file))
        return DataFrame(data)
    
    @staticmethod
    def all_different(values:Iterable[Any])->bool:
        return len(set(values)) == len(list(values))
    
    @property
    def colum_names(self)->list[str]:
        return list(self.__data.keys()) 
    @property
    def colum_number(self)->int:
        return len(self.colum_names)
    def colum(self,name:str)->list[str]:
        return self.__data[name]
    def column_index(self,index:int)->list[str]:
        name:str = self.colum_names[index]
        return self.__data[name]
    def colum_all_different(self,name:str)->bool:
        return DataFrame.all_different(self.colum(name))
    def cell(self,row:int,colum:str)->str:
        return self.__data[colum][row]
    def cell_index(self,row:int,colum:int)->str:
        return self.__data[self.colum_names[colum]][row]
    def cell_name(self,row:str,colum:str)->str:
        check_argument(self.colum_all_different(colum),f'La columna {colum} no tiene los valores todos diferentes')
        index: int = self.colum(colum).index(row)
        return self.__data[colum][index]
    @property
    def row_number(self)->int:
        return len(self.__data[self.colum_names[0]]) 
    def row(self,n:int)->list[str]:
        return list(self.__data[k][n] for k in self.__data.keys())
    def row_name(self,colum:str,row:str)->list[str]:
        check_argument(self.colum_all_different(colum),f'{len(set(self.colum(colum)))} ,  {len(list(self.colum(colum)))})')
        index: int = self.colum(colum).index(row)
        return self.row(index)
    @property
    def rows(self)->list[list[str]]:
        return list(self.row(i) for i in range(0,self.row_number))

    # Mostrar los primeros n registros (por defecto, n=5)
    def head(self,n:int=5)->DataFrame:  # Muestra los dos primeros registros
        return DataFrame.of_dict({k:v[0:n] for k,v in self.__data.items()})
    
    # Mostrar los últimos n registros (por defecto, n=5)
    def tail(self,n:int=5)->DataFrame:
        return DataFrame.of_dict({k:v[-n:self.row_number] for k,v in self.__data.items()})
    
    def slice(self,n:int,m:int)->DataFrame:
        return DataFrame.of_dict({k:v[n:m] for k,v in self.__data.items()})
    
    def filter(self,p:Callable[[list[str]],bool])->DataFrame:
        rows:list[list[str]] = [r for r in self.rows]
        rs = [x for x in rows if p(x)]
        return DataFrame.of(self.colum_names,rs)
    
    def sort_by(self,f:Callable[[list[str]],E])->DataFrame:
        rows:list[list[str]] = [r for r in self.rows]
        rs = sorted(rows, key=f)
        return DataFrame.of(self.colum_names,rs)   
    
    def group_by(self,colum_names:list[str],ag_name:str,op:Callable[[R,R],R],value:Callable[[list[str]],R])->DataFrame:
        key = lambda ls:tuple(ls[i] for i in range(0,self.colum_number) if (self.colum_names[i] in set(colum_names)))
        gr:dict[tuple,R] = grouping_reduce(self.rows,key,op,value)
        rows:list[list[str]] = [list(t)+[str(gr[t])] for t in gr.keys()]
        colum_names = colum_names + [ag_name]
        return DataFrame.of(colum_names,rows)
    
    def add_colum(self,colum_name:str,datos:list[str])->DataFrame:
        data:dict[str,list[str]] = {k:v  for k,v in self.__data.items()}
        data[colum_name] = datos
        return DataFrame.of_dict(data)
    
    def add_calculated_colum(self,colum_name:str,f:Callable[[str],str],new_colum:str)->DataFrame:
        data:dict[str,list[str]] = {k:v  for k,v in self.__data.items()}
        datos:list[str] = [f(x) for x in data[colum_name]]
        data[new_colum] = datos
        return self.add_colum(new_colum,datos)
    
    def remove_colum(self,colum_name:str)->DataFrame:
        data:dict[str,list[str]] = {k:v  for k,v in self.__data.items()}
        del data[colum_name]
        return DataFrame.of_dict(data)
    
    def __list_format(self,ls:list[str])->str:
        r = '|'.join(f'{e:>15s}' for e in ls)
        return f'{r}|'  
    
    def __list_format_enum(self,ls:list[list[str]])->Iterable[str]:
        return (f'{i:>5d}|{self.__list_format(f)}' for i,f in enumerate(ls))
    
    def __str__(self):
        line = '_'*(5+(self.colum_number)*18)
        prefix = f'{line}\n{"|":>6s}{self.__list_format(self.colum_names)}\n{line}'
        r = '\n'.join(self.__list_format_enum(self.rows))
        return f'{prefix}\n{r}'

if __name__ == '__main__':
    '''
    d: DataFrame = DataFrame.parse('/dataframe/personas.csv')
    print(d)
    print(d.head(3))
    print(d.remove_colum('Nombre'))
    print(d)
    print(d.filter(lambda ls:int(ls[2].strip()) >30))
    print(d.sort_by(lambda ls: ls[1].strip()))
    print(d.add_calculated_colum('Nombre',lambda s: s[0],'Nueva'))
    '''
    d2: DataFrame = DataFrame.parse('/dataframe/mascotas.csv')
    opm:Callable[[int,int],int] = lambda x,y:x+y
    print(d2.group_by(['Especie','Sexo'],'Cantidad',operator.add,lambda _:1))
    d3: DataFrame = DataFrame.parse('/dataframe/personas.csv')
    opm2:Callable[[float,float],float] = lambda x,y:round(min(x,y),2)
    print(d3.group_by(['Edad'],'Altura',opm2,lambda ls:float(ls[3])))
    opm3:Callable[[date,date],date] = lambda x,y:min(x,y)
    print(d3.group_by(['Edad'],'Edad',opm3,lambda ls:datetime.strptime(ls[4],'%d/%m/%Y').date()))
    print(d3.group_by(['Edad'],'Edad',opm3,lambda ls:Persona.val(ls,'fecha')))
    print(d3.cell(3,'Apellido'))
    print(d3.cell_index(3,1))
    print(d3.colum('Nombre'))
    print(d3.row_name('Nombre','Jorge'))
    print(asdict(Persona.parse(d3.row(4)))['edad'])
    
    
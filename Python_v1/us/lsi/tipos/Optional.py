'''
Created on 14 sept 2022

@author: migueltoro
'''


from __future__ import annotations
from dataclasses import dataclass
import typing
from us.lsi.tools.Preconditions import checkArgument

E = typing.TypeVar('E')

@dataclass(frozen=True)
class Optional(typing.Generic[E]):
    value:typing.Optional[E]
        
    @staticmethod
    def of(e:E) -> Optional[E]:
        return Optional(e)
    
    @staticmethod
    def of_nullable(e:typing.Optional[E]) -> Optional[E]:
        return Optional(e)
    
    @staticmethod
    def empty() -> Optional[E]:
        return Optional(None)
    
    @property
    def is_present(self) -> bool: 
        return self.value is not None 
    
    @property
    def is_empty(self) -> bool:  
        return self.value is None 
    
    def get(self) -> E: 
        checkArgument(self.value is not None,f'El valor opcional es None')
        if self.value is not None:
            return self.value
        else:
            raise Exception(f"Es nulo el valor opcional")
            
    def or_else(self,d:E) -> E:       
        if self.value is not None:
            return self.value
        else:
            return d
    
    def __str__(self) -> str:
        return f'{self.value}'
    
if __name__ == '__main__':
    op:Optional[int] = Optional.of_nullable(None)
    op2:Optional[int] = Optional.empty()
    print(op.get())
    print(op2.get())
    
    
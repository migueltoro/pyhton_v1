'''
Created on 15 jul 2025

@author: migueltoro
'''

def all_not_None(*args)->bool:
    """
    Check if all arguments are not None.
    
    Args:
        *args: Variable length argument list.
        
    Returns:
        bool: True if all arguments are not None, False otherwise.
    """
    return all(arg is not None for arg in args)

if __name__ == '__main__':
    pass
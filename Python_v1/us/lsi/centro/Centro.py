'''
Created on 22 nov 2022

@author: belen
'''
from __future__ import annotations
from us.lsi.centro.Alumno import Alumno
from us.lsi.centro.Profesor import Profesor
from us.lsi.centro.Asignatura import Asignatura
from us.lsi.centro.Matricula import Matricula
from us.lsi.centro.Asignacion import Asignacion
from typing import Iterable, Optional
from us.lsi.tools.File import absolute_path, lineas_de_fichero
from us.lsi.tools.Iterable import strfiter, grouping_list, grouping_reduce
from us.lsi.tools.Preconditions import check_argument
from collections import Counter
from us.lsi.tools.Dict import strfdict

class Centro:
    
    centro = None

    def __init__(self, alumnos:list[Alumno], profesores:list[Profesor],asignaturas:list[Asignatura],\
            matriculas:set[Matricula], \
            asignacion_de_profesores:set[Asignacion])->None:
        self.alumnos = alumnos
        self.profesores = profesores
        self.asignaturas = asignaturas
        self.matriculas = matriculas
        self.asignacion_de_profesores = asignacion_de_profesores 
        
        self.alumnos_dni:dict[str,Alumno] = {a.dni : a for a in self.alumnos}
        self.profesores_dni:dict[str,Profesor] = {p.dni : p for p in self.profesores}
        

    @staticmethod
    def of()->Centro:
        if Centro.centro is None:
            Centro.centro = Centro.of_files()
        return Centro.centro

        
    @staticmethod
    def of_files(fichero_alumnos:str=absolute_path('/centro/alumnos.txt'),
           fichero_profesores:str=absolute_path('/centro/profesores.txt'),
           fichero_asignaturas:str=absolute_path('/centro/asignaturas.txt'))->Centro:
        alumnos:list[Alumno] = [Alumno.parse_alumno(ln) for ln in 
                                lineas_de_fichero(fichero_alumnos,encoding='utf-8')]
        profesores:list[Profesor] = [Profesor.parse_profesor(ln) for ln in lineas_de_fichero(fichero_profesores,encoding='utf-8')]
        asignaturas:list[Asignatura] = [Asignatura.parse(ln) for ln in lineas_de_fichero(fichero_asignaturas,encoding='utf-8')]
        Centro.centro = Centro(alumnos,profesores,asignaturas,set(),set())
        return Centro.centro
    
    def add_asignaciones(self,fichero:str=absolute_path('/centro/asignaciones.txt'))->None:
        r:Iterable[Asignacion] = (Asignacion.parse(ln)  
                                  for ln in lineas_de_fichero(fichero))       
        for a in r:
            self.asignacion_de_profesores.add(a)
               
    def add_asignacion(self,profesor:Profesor,asignatura:Asignatura,grupo:int)->None:
        self.asignacion_de_profesores.add(Asignacion.of(profesor.dni,asignatura.id,grupo))      
    
    def add_matriculas(self,fichero:str=absolute_path('/centro/matriculas.txt'))->None:
        r:Iterable[Matricula] = (Matricula.parse(ln)  for ln in lineas_de_fichero(fichero))       
        for a in r:
            self.matriculas.add(a)
            
    def add_matricula(self,alumno:Alumno,asignatura:Asignatura,grupo:int)->None:
        self.matriculas.add(Matricula.of(alumno.dni,asignatura.id,grupo))
    
    @property
    def numero_profesores(self)->int: 
        return len(self.profesores)
    
    @property
    def numero_alumnos(self)->int: 
        return len(self.alumnos)
    
    @property
    def numero_asignaturas(self)->int: 
        return len(self.asignaturas)
    
    @property
    def numero_grupos(self)->int: 
        return sum(a.num_grupos for a in self.asignaturas)
    
    def profesor(self,i:int)->Profesor: 
        return self.profesores[i]
    
    def profesor_de_dni(self,dni:str)->Profesor: 
        return self.profesores_dni[dni]
    
    def alumno_de_dni(self,dni:str)->Alumno: 
        return self.alumnos_dni[dni]
    
    def asignatura(self,i:int)->Asignatura: 
        return self.asignaturas[i]
    
    def alumno(self,i:int)->Alumno: 
        return self.alumnos[i]
    
    def asignaturas_impartidas(self,profesor:Profesor)->set[Asignatura]: 
        return {self.asignatura(asg.ida) 
                for asg in Centro.of().asignacion_de_profesores if asg.dni == profesor.dni}
    
    def asignaturas_cursadas(self,alumno:Alumno)->set[Asignatura]: 
        return {self.asignatura(m.ida) for m in Centro.of().matriculas if m.dni == alumno.dni}
    
    #===========================================================================
    # DEFENSA
    #===========================================================================
    
    '''
    Lista de alumnos cuya letra de dni es lt
    '''
    def alumnos_con_letra_dni(self, lt:str)->list[Alumno]:
        return [a for a in self.alumnos if lt in a.dni]
    
    '''
    Asignaturas no impartidas por un profesor
    '''
    def asignaturas_no_impartidas(self, pr:Profesor)->set[Asignatura]:
        return set(a for a in self.asignaturas if a not in self.asignaturas_impartidas(pr))
    
    '''
    Número de asignaturas cursadas por un  alumno
    '''
    def numero_asignaturas_alumno(self, al:Alumno)->int:
        return len(self.asignaturas_cursadas(al))
    
    '''
    Edad media de los alumnos
    '''
    @property
    def edad_media_alumnos(self)->Optional[int]:
        if self.numero_alumnos>0:
            al_mayores:list[int] = [a.edad for a in self.alumnos if a.edad >=18]
            return int(sum(al_mayores)/len(al_mayores))
        else:
            return None

    '''
    Implementar el método numero_de_creditos_de_profesor. Devuelve el total de créditos del profesor p, 
    siendo p un parámetro de entrada del método. 
    PISTA: Para realizar este ejercicio puede diseñar previamente el método asignaturas_id 
    que devuelve un diccionario cuyas claves son los identificadores y los valores sus respectivas asignaturas
    '''
    @property   
    def asignaturas_id(self)->dict[int,Asignatura]:
        return {a.id:a for a in self.asignaturas}
    
    def asignaturas_id_2(self)->dict[int,Asignatura]:
        d: dict[int,Asignatura] = {}
        for a in self.asignaturas:
            d[a.id] = a
        return d
          
    def numero_de_creditos_de_profesor(self,p:Profesor)->int:
        return sum(self.asignaturas_id[a.ida].creditos for a in self.asignacion_de_profesores if a.dni == p.dni)
    
    def numero_de_creditos_de_profesor_2(self,p:Profesor)->int:
        r:int = 0
        for a in self.asignacion_de_profesores:
            if a.dni == p.dni:
                r = r + self.asignaturas_id[a.ida].creditos
        return r
    
    '''
    Implementar el método alumnos_mismo_distrito_postal. Devuelve un conjunto con los alumnos cuyo 
    código postal coincida con el código postal del profesor p (p es un parámetro de entrada al método).
    '''
    
    def alumnos_mismo_distrito_postal(self,p:Profesor)->set[Alumno]:
        return {a for a in self.alumnos if a.direccion.zip_code == p.direccion.zip_code}
    
    '''
    Implementar el método alumnos_por_grupo. Devuelve un diccionario con los alumnos que cursan 
    la asignatura cuyo código es ida (ida es un parámetro de entrada al método). 
    En dicho diccionario las claves serán los identificadores de los grupos y los valores son las listas de alumnos que cursan la asignatura en ese grupo.
    '''
   
    def alumnos_por_grupo(self,ida:int)->dict[int,list[Alumno]]:
        mat_f: Iterable[Matricula] = (m for m in self.matriculas if m.ida == ida)
        return grouping_list(mat_f,key=lambda m:m.idg,value=lambda m:self.alumno_de_dni(m.dni))
    
    def alumnos_por_grupo_2(self,ida:int)->dict[int,list[Alumno]]:
        d:dict[int,list[Alumno]] = {}
        for m in self.matriculas:
            if m.ida == ida:
                key: int = m.idg
                if key in d:
                    d[key].append(self.alumno_de_dni(m.dni))
                else:
                    d[key]= [self.alumno_de_dni(m.dni)]
        return d    
    
    '''
    Implementar el método elimina_profesor. Elimina el profesor p del centro 
    (p es un parámetro de entrada al método). El profesor solo puede eliminado si no imparte ninguna asignatura. 
    Si no puede ser eliminado se disparará una excepción y si se elimina debe desaparecer su información del centro.
    '''    
    def elimina_profesor(self,p_Profesor)->None:  
        check_argument(len(self.asignaturas_impartidas(p)) != 0, 
                       f'No se puede eliminar el profesor porque imparte asignaturas')  
        self.profesores.remove(p)
        del self.profesores_dni[p.dni] 
        
    '''
    Implementar el método total_grupos_profesor. Devuelve un diccionario que asocia cada edad de los profesores 
    con el total de grupos que dan los profesores de dicha edad. 
    Por ejemplo, si el diccionario resultante es {28: 50, 49: 70} significaría que los profesores que tienen 28 años 
    imparten en total 50 grupos y que los de 49 imparten 70.
    ''' 
        
    def total_grupos_profesor(self)->dict[int,int]:
        return grouping_reduce(self.asignacion_de_profesores,      
                               key=lambda a:self.profesor_de_dni(a.dni).edad,
                               op=lambda x,y:x+y,
                               value=lambda a:1)
    
        
    def total_grupos_profesor_2(self)->dict[int,int]:
        d: dict[int,int] = {}
        for a in self.asignacion_de_profesores:
            key= self.profesor_de_dni(a.dni).edad
            if key in d:
                d[key] = d[key] +1
            else:
                d[key] = 1
        return d
    
    def total_grupos_profesor_3(self)->dict[int,int]:
        d: Iterable[int] = (self.profesor_de_dni(a.dni).edad for a in self.asignacion_de_profesores)
        return Counter(d)
        

if __name__ == '__main__':
    c:Centro = Centro.of()
    print(f'- Hay {Centro.of().numero_alumnos} alumnos en el centro')
    print(f'- Hay {Centro.of().numero_profesores} profesores en el centro')
    print(f'- Hay {Centro.of().numero_asignaturas} asignaturas en el centro')
    print(f'- Hay {Centro.of().numero_grupos} grupos en el centro')
    
    print('___________')
    print(">> Añadiendo asignaciones")
    c.add_asignaciones()
    print('- El número de asignaciones es:')    
    print(len(c.asignacion_de_profesores))
    
    print('___________')
    print(">> Añadiendo matrículas")
    c.add_matriculas()
    print('- El número de matrículas es:')
    print(len(Centro.of().matriculas))
    print('___________')
    
    
    p = Centro.of().profesor_de_dni('53045701L')
    print(f'- El profesor con dni 53045701L es {p}')
    print('___________')
    
    
    print(f'- Las asignaturas impartidas por {p.nombre} son:')
    print(strfiter((a.nombre for a in Centro.of().asignaturas_impartidas(p)),sep='\n',prefix='',suffix=''))
    print('___________')
    
    al = Centro.of().alumno(200)
    print(f'- El alumno que se encuentra en la posición 200 es {al}')
    print('___________')

    print(f'- Las asignaturas cursadas por {al.nombre} son:')
    print(strfiter((a.nombre for a in Centro.of().asignaturas_cursadas(al)),sep='\n',prefix='',suffix=''))
    print('___________')   
    
    print(f'- Hay un total de {Centro.of().numero_grupos} grupos.')
    print('___________')
    
    print(f' {c.numero_de_creditos_de_profesor(p)}') 
    print(f' {c.numero_de_creditos_de_profesor_2(p)}')
    print(c.total_grupos_profesor()) 
    print(c.total_grupos_profesor_2())
    print(c.total_grupos_profesor_3())
    ida:int = c.asignatura(45).id
    print(ida)
    print(strfdict(c.alumnos_por_grupo(ida)))
    print('___________')
    print(strfdict(c.alumnos_por_grupo_2(ida)))
    

    
    
    

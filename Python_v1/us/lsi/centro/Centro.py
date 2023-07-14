'''
Created on 22 nov 2022

@author: belen
'''
from __future__ import annotations
from us.lsi.ejemplos_types.Alumno import Alumno
from us.lsi.centro.Alumnos import Alumnos
from us.lsi.centro.Profesor import Profesor
from us.lsi.centro.Profesores import Profesores
from us.lsi.centro.Asignaturas import Asignaturas
from us.lsi.centro.Matriculas import Matriculas
from us.lsi.centro.Asignaciones import Asignaciones
from us.lsi.centro.Grupo import Grupo
from us.lsi.tools.File import absolute_path

class Centro:
    
    centro = None

    def __init__(self, alumnos:Alumnos,profesores:Profesores,asignaturas:Asignaturas,\
            matriculas:Matriculas, \
            asignaciones:Asignaciones)->None:
        self.alumnos = alumnos
        self.profesores = profesores
        self.asignaturas = asignaturas
        self.matriculas = matriculas
        self.asignaciones = asignaciones 
        
        self.alumnos_dni:dict[str,Alumno] = {a.dni : a for a in self.alumnos.todos}
        self.profesores_dni:dict[str,Profesor] = {p.dni : p for p in self.profesores.todos}
        self.grupos:set[Grupo] = {Grupo.of(a.ida,a.idg) for a in self.asignaciones.todas}
        

    @staticmethod
    def of()->Centro:
        if Centro.centro is None:
            Centro.centro = Centro.of_files()
        return Centro.centro

        
    @staticmethod
    def of_files(fichero_alumnos:str=absolute_path('/centro/alumnos.txt'),
           fichero_profesores:str=absolute_path('/centro/profesores.txt'),
           fichero_asignaturas:str=absolute_path('/centro/asignaturas.txt'),
           fichero_matriculas:str=absolute_path('/centro/matriculas.txt'),
           fichero_asignaciones:str=absolute_path('/centro/asignaciones.txt'))->Centro:
        alumnos:Alumnos = Alumnos.of_file(fichero_alumnos)
        profesores:Profesores = Profesores.of_file(fichero_profesores)
        asignaturas:Asignaturas = Asignaturas.of_file(fichero_asignaturas)
        matriculas:Matriculas = Matriculas.of_file(fichero_matriculas)
        asignaciones: Asignaciones = Asignaciones.of_file(fichero_asignaciones)
        return Centro(alumnos,profesores,asignaturas,matriculas,asignaciones)

   
    @property
    def grupos_size(self):
        return len(self.grupos)

if __name__ == '__main__':
    c:Centro = Centro.of()
    print(f'- Hay {Centro.of().alumnos.size} alumnos en el centro')
    print(f'- Hay {Centro.of().profesores.size} profesores en el centro')
    print(f'- Hay {Centro.of().asignaturas.size} asignaturas en el centro')
    print(f'- Hay {Centro.of().grupos_size} grupos en el centro')
    print(f'- Hay {Centro.of().matriculas.size} matriculas en el centro')
    p = Centro.of().profesores.profesor_dni('53045701L')
    print(f'- El profesor con dni 53045701L es {p}')
    print('___________')
    

    
    
    

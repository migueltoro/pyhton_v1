'''
Created on 26 ago 2023

@author: migueltoro
'''
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, date, timedelta
import calendar
import locale

@dataclass(order=True, frozen=True)
class Fecha:
    año: int
    mes: int
    dia: int

    @staticmethod
    def of(año: int, mes: int, dia: int) -> Fecha:
        return Fecha(año, mes, dia)
    
    @staticmethod
    def parse(fecha_str: str) -> Fecha:
        año, mes, dia = map(int, fecha_str.split('-'))
        return Fecha(año, mes, dia)

    @staticmethod
    def dias_en_mes(año: int, mes: int) -> int:
        mes -= 1
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if mes == 2 and (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
            return 29
        return dias_por_mes[mes]

    @staticmethod
    def es_año_bisiesto(año: int) -> bool:
        return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)
    
    @staticmethod
    def zeller_congruence(año: int, mes: int, dia: int) -> int:
        if mes < 3:
            año -= 1
            mes += 12

        K = año % 100
        J = año // 100
        h = (dia + 13 * (mes + 1) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
        return h
    
    @staticmethod
    def meses():
        return ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", 
                "Noviembre","Diciembre"]
    
    @property
    def nombre_mes(self):
        return Fecha.meses()[self.mes-1]
    
    @property
    def dia_semana(self) -> str:
        dias_semana = ["Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        dia_semana_numero = self.zeller_congruence(self.año, self.mes, self.dia)
        return dias_semana[dia_semana_numero]
    
    def sumar_dias(self, cantidad_dias: int) -> Fecha:
        dia_actual = self.dia
        mes_actual = self.mes
        año_actual = self.año

        while cantidad_dias > 0:
            dias_mes_actual = Fecha.dias_en_mes(año_actual, mes_actual)
            dias_restantes_mes = dias_mes_actual - dia_actual + 1

            if cantidad_dias >= dias_restantes_mes:
                cantidad_dias -= dias_restantes_mes
                dia_actual = 1
                mes_actual += 1

                if mes_actual > 12:
                    mes_actual = 1
                    año_actual += 1
            else:
                dia_actual += cantidad_dias
                cantidad_dias = 0

        return Fecha(año_actual, mes_actual, dia_actual)
    
    def restar_dias(self, cantidad_dias: int) -> Fecha:
        dia_actual = self.dia
        mes_actual = self.mes
        año_actual = self.año

        while cantidad_dias > 0:
            dias_mes_actual = Fecha.dias_en_mes(año_actual, mes_actual)

            if cantidad_dias >= dia_actual:
                cantidad_dias -= dia_actual
                dia_actual = dias_mes_actual
                mes_actual -= 1

                if mes_actual < 1:
                    mes_actual = 12
                    año_actual -= 1
            else:
                dia_actual -= cantidad_dias
                cantidad_dias = 0

        return Fecha(año_actual, mes_actual, dia_actual)
    
    def diferencia_en_dias(self, otra_fecha: Fecha) -> int:
        d:int
        if self == otra_fecha:
            return 0
        
        if self > otra_fecha:
            d = 1
            fecha_menor, fecha_mayor = otra_fecha, self
        else:
            d = -1
            fecha_menor, fecha_mayor = self, otra_fecha

        dias_diferencia = 0
        while fecha_menor < fecha_mayor:
            dias_diferencia += 1
            fecha_menor = fecha_menor.sumar_dias(1)
        
        return d*dias_diferencia
    
    def __str__(self)->str: 
        old_code, _ = locale.getlocale()
        locale.setlocale(locale.LC_TIME, 'es_ES')
        r:str = f'{self.dia_semana} {self.dia} de {self.nombre_mes} del {self.año}'
        locale.setlocale(locale.LC_TIME, f"{old_code}")
        return r
        

if __name__ == '__main__':
    # Ejemplo de uso
    fecha = Fecha.of(2023, 8, 15)
    print("Fecha creada con método of:", fecha)
    fd:date = datetime(2023, 8, 15).date()

    fecha_desde_str = Fecha.parse("2023-08-25")
    print("Fecha desde cadena:", fecha_desde_str)

    dias_en_agosto = Fecha.dias_en_mes(2023, 8)
    print("Días en agosto:", dias_en_agosto)

    es_bisiesto = Fecha.es_año_bisiesto(2024)
    print("¿2024 es bisiesto?:", es_bisiesto)
    
    print(fecha.sumar_dias(121))
    print(fd+timedelta(days=121))
    
    print('==============')
    print(Fecha.dias_en_mes(2023, 6))
    print('==============')
#    print(fd+timedelta(days=121))
    
    
    print(Fecha.of(2023,9,28).dia_semana)
    print(calendar.day_name[datetime(2023, 9, 28).date().weekday()])
    
    print(fecha.restar_dias(155))
    print(fd-timedelta(days=155))
    
    print(fecha.diferencia_en_dias(Fecha.of(2024, 1, 3)))
    print((fd-datetime(2024, 1, 3).date()).days)
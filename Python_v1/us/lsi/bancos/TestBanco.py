'''
Created on 19 nov 2023

@author: migueltoro
'''
from us.lsi.bancos.Cuentas import Cuentas
from us.lsi.bancos.Empleados import Empleados
from us.lsi.bancos.Prestamos import Prestamos
from us.lsi.bancos.Personas import Personas
from us.lsi.bancos.Banco import Banco
from us.lsi.tools.Iterable import str_iter
from us.lsi.tools.Dict import str_dict
import calendar
from us.lsi.bancos.Questions import vencimiento_de_prestamos_de_cliente, cliente_con_mas_prestamos, cantidad_prestamos_empledado, \
    empleado_mas_longevo, rango_de_intereses_de_prestamos, prestamos_a_empleados, num_prestamos_por_mes_año

if __name__ == '__main__':
    banco:Banco = Banco.of()
    print(banco.empleados.empleado_dni('52184462S'))
    print({f.strftime('%Y-%m-%d') for f in vencimiento_de_prestamos_de_cliente(banco,'35529655Z')})
    print(vencimiento_de_prestamos_de_cliente(banco,'35529655Z'))
    print(cliente_con_mas_prestamos(banco))
    print(cantidad_prestamos_empledado(banco,'52184462S'))
    print(empleado_mas_longevo(banco))
    print(rango_de_intereses_de_prestamos(banco))
    print(str_iter(prestamos_a_empleados(banco),sep='\n'))
    print(str_dict(num_prestamos_por_mes_año(banco),sep='\n',key=lambda t:f'({calendar.month_name[t[0]]},{t[1]})'))
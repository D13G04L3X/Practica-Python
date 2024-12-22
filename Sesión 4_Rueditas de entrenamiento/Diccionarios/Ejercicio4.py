'''
Ejercicio 4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd
de <mes> de aaaa donde <mes> es el nombre del mes.
'''

# 01/10/2018                Clave del mes = 10
# 01 de octubre del 2018    Valor del mes = octubre
# Clave: valor

meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
fecha = input('Por favor, escriba una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'del', fecha[2])

# Recomendación: Hacer las validaciones en caso de una entrada falsa, por ejemplo un mes que no existe o mayor a 12, 
# también puede validar el día, que esté entre 1 y 31 y validar el año sea mayor a 2000 y menor a 9999

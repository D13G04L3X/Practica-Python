'''
Ejercicio 6: Imprimir el mes correspondiente al número
Escribe un programa que reciba un número del 1 al 12 y devuelva el nombre del mes correspondiente.
'''

# Hecho por: Lorena

def numero_mes(mes):
    meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
    } 
    return meses.get(mes, "Mes inválido, ingrese nuevamente un número")

mes = int(input("Por favor ingresa el número del mes: "))
print(numero_mes(mes))
'''
Ejercicio 2

Imprimir el día de la semana.
Escribe un programa que imprima el nombre del día basado en un número. Si el número es del 1 al 7, el programa
debe mostrar el día correspondiente.

'''

def dia_semana(numero):
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return dias.get(numero, "Número inválido")

print(dia_semana(3))    # Miércoles
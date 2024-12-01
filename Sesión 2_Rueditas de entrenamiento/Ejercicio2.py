# Ejercicios

'''
Ejercicio 2: Construir un programa que simule el funcionamiento de una calculadora que puede realizar 
las cuatro operaciones aritméticas básicas (suma, resta, multiplicación y división). El usuario debe especificar la 
operación con el primer carácter del nombre de la operación. 

➤ S, s - Suma 
➤ R, r - Resta 
➤ P, p, M, m - Multiplicación 
➤ D, d - División

'''

num1 = float(input("Digita un número: "))
num2 = float(input("Digita un número: "))

operacion = input("Digita la operación a realizar: ").upper()       #.upper = función para convertir en mayúscula cadena de texto, #.lower = función para convertir en mayúscula cadena de texto

if operacion == 'S':
    suma = num1 + num2
    print(f"\nLa suma es: {suma}")
elif operacion == 'R':
    resta = num1 - num2
    print(f"\nLa resta es: {resta}")
elif operacion == 'P' or operacion == 'M':
    multiplicacion = num1 * num2
    print(f"\nLa multiplicación es: {multiplicacion}")
elif operacion == 'D':
    division = num1 / num2
    print(f"\nLa divisón es: {division}") 
else:
    print("\nSe equivocó de operación")
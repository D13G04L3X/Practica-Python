'''
Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares 
desde 1 hasta ese número separado por comas.

'''
# rango = numero / rango(numero) i++
# numero = 9
# 1, 2, 3, 4, 5 = i+1
# 1, 3, 5, 7, 9 = i+2

numero = int(input("Señor usuario, por favor digite un número: "))
for i in range(1, numero+1, 2):
    print(i, end=", ")

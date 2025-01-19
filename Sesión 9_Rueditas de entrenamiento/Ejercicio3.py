'''
Ejercicio 3
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

'''

# Pedir al usuario por medio del input, un número entero
# Definir la variable
# Bucle para que se repita la condición
# Condicional if para validar si es primo o no

numero_entero = int(input("Por favor escriba un número entero: "))
i = 2
while numero_entero % i != 0:
    i += 1                          # Iterador aumente de 1 en 1
if i == numero_entero:
    print(str(numero_entero) + " es un número primo")
else:
    print(str(numero_entero) + " no es un número primo")
'''
Ejercicio 2
Escribir un programa que almacene la cadena de caracteres "contraseña" en una variable, pregunte al usuario por la 
contraseña hasta que introduzca la contraseña correcta.

'''

# Definir la variable para preguntar la contraseña
# Desarrollar el ejercicio
# Imprimir un mensaje que diga "Introduzca la contraseña correcta"

llave = "contraseña"        # Variable estática o Valores quemados
contrasena = ""
while contrasena != llave:
    contrasena = input("Introduzca la contraseña correcta: ")
print("Contraseña correcta")


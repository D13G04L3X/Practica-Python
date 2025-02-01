'''
Ejercicio 12

Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba "salir" 
que terminará

'''

while True:
    frase = input("Introduzca una frase: ")
    if frase == "salir":
        break
    print(frase)
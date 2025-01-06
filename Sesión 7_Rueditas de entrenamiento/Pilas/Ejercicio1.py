'''
Ejercicio 1.
Escribe un programa que use una pila para invertir una cadena. Por ejemplo, dada la cadena "Hola", el programa debe
devolver "aloh".

'''

# 1. Crear la pila
# 2. Insertarle valores
# 3. Validar los caracteres e invertirlos

def invertir_cadena(cadena):
    pila = []
    # Apilar cada carácter
    for char in cadena:
        pila.append(char)
    # Sacar los caracteres de la pila para formar la cadena invertida
    cadena_invertida = ""
    while pila:
        cadena_invertida += pila.pop()
    return cadena_invertida

cadena = input("Por favor, ingrese una palabra: ")
print(invertir_cadena(cadena))
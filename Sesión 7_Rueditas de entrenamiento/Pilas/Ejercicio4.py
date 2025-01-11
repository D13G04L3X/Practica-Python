'''
Ejercicio 4.
Validar una expresión de palíndromo



'''

# Solución

def invertir_palabra (palabras):
    pila = []
    #palabras = palabra.split()
    for palabra in palabras:
        pila.append(palabra)
        palabra_invertida = ""
# Comparar palabra original con la invertida
    if palabra.replace(" ", "").lower() == palabra_invertida.replace(" ", "").lower():
        return palabra_invertida + "\nEs un palíndromo"
    else:
        return palabra_invertida + "\nNo es un palíndromo"
    
palabras = input("Por favor, escriba una frase o palabra: ")
print(invertir_palabra(palabras))
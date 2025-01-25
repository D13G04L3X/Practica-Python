# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de 
# la palabra introducida empezando por la última 

# Hecho por Lorena

palabra = input ("Por favor, escriba una palabra: ")

for letra in reversed(palabra):
    print(letra)
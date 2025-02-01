'''
Ejercicio 5.

Categorizar edades
Escribe un programa que reciba una edad y diga a qué categoria pertenece:
"Niño" (0-12), "Adolescente" (13-17), "Adulto" (18-64), "Anciano" (65+).

'''

# Lógica.
'''
- Primero creamos un def edad_categoria(edad)
- Desarrollar el ejercicio
- if, elif y else
- Pedir por medio un input("Por favor, escribe que edad tienes: ")
- Print(edad_categoria(edad))

'''

# Solución.

def edad_categoria(edad):
    if edad <= 12:
        return "Es niño"
    elif edad <= 17:
        return "Es adolescente"
    elif edad <= 64:
        return "Es adulto"
    else:
        return "Es adulto mayor"
    
edad = int(input("Por favor, escribe que edad tienes: "))
print(edad_categoria(edad))




'''
Ejercicio 2.
Según el ejercicio anterior, vamos a revertir el orden de palabras en una oración

Ejemplo: "La pila es genial"
Salida: "genial es pila La"
'''

# 1. Pedimos la oración
# 2. Crear la pila
# 3. Validar, con la división de la oración en palabras
# 4. Insertar cada palabra en una pila

def invertir_palabras(oracion):
    pila = []
    palabras = oracion.split()
    for palabra in palabras:
        pila.append(palabra)
    oracion_invertida = ""
    while pila:
        oracion_invertida += pila.pop() + " "
    return oracion_invertida                # return oracion_invertida.strip()

oracion = input("Por favor, ingrese una frase: ")
print(invertir_palabras(oracion))
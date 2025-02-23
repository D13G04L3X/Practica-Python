'''
Ejercicio 4: Tamaño de la cola
Crear una función que reciba una cola y devuelva su tamaño
'''

# Lógica
# 1. Definir una variable: tamaño_cola
# 2. Hacer una función, reciba y luego retorne el tamaño de la cola
# 3. Mostrar el tamaño

# Solución

from collections import deque

def tamaño_cola(cola):
    return len(cola)

cola = deque([9, 10, 13, 3, 2, 15])
print("El tamaño de la cola es: ", tamaño_cola(cola))   # El tamaño es 6
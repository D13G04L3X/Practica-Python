'''
Ejercicios

Ejercicio 1: Crear una cola que realice operaciones básicas
Crear una cola, que añada elementos, elimina el primero y luego muestre la cola
'''

# Lógica
# 1. Realizar operaciones básicas.
# 2. Crear la cola, luego añade elementos.
# 3. Eliminar el primero.
# 4. Mostrar la cola.

# Solución

from collections import deque

# 1. Crear cola
cola = deque([8, 5, 6, 9, 4])
print("Cola inicial: ", cola)

# 2. Añadir elementos
cola.append(1)
cola.append(3)
print("Después de Enqueue: ", cola)

# 3. Eliminar el primer elemento y mostrar
cola.popleft()
print("Después del Dequeue: ", cola)

# 4. Mostrar el tamaño de la cola
print("El nuevo tamaño de la cola es: ", len(cola))
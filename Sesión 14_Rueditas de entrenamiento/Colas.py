'''
Deque, "double-ended queue" (cola de doble extremo)
Que los elementos pueden ser añadidos o eliminados desde el inicio como desde el final de la cola. 
FIFO (First in - First out) Primero en entrar, primero en salir

En python, el deque, se encuentra en el módulo collections y se usa para implementar colas de manera eficiente.
'''

from collections import deque

'''
1. Deque → Crear una cola vacía.
2. Enqueue → Anade un elemento al final de la cola.
3. Peek → Ver el primer elemento de la cola, pero sin eliminarlo
4. Dequeue → Eliminar el primer elemento de la cola.
5. Size → Ver el número de elementos que están en la cola.
6. IsEmpty → Verificar si la cola está vacía.
'''

# Crear una cola
cola = deque()

# Enqueue: Añadir elementos
cola.append(5)
cola.append(10)
cola.append(15)

# Peek: Ver el primer elemento
print("primer elemento: ", cola[0]) # 5

# Dequeue: Eliminar el primer elemento
eliminado = cola.popleft()
print("Elemento eliminado: ", eliminado) # 5

# Size: El tamaño de la cola.
print("Tamaño de la cola: ", len(cola)) # 2

# IsEmpty: Verificar si la cola está vacía
print("¿Está vacía la cola?: ", len(cola) == 0) # False


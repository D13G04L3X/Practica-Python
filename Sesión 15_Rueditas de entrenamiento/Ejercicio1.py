from collections import deque

'''
Deque() → Crear una cola vacía.
Enqueue → Añade un elemento al final de la cola.
Peek → Ver el primer elemento de la cola, sin eliminarlo.
Dequeue →  Eliminar el primer elemento de la cola.
Size → Ver el número de elementos que están en la cola.
IsEmpty → Verificar si la cola está vacía.
'''

'''
Ejercicio 1: Sistema de tareas pendientes
Simula un sistema de tareas pendientes donde las tareas se agregan a una cola. Cada tarea tiene un identificador. 
El sistema procesa las tareas en el orden en que se agregaron.

Tarea 1
Tarea 2
Tarea 3
'''

# Lógica
# 1. Crear una variable
# 2. Hacer un sistema de tareas, para eso hay que crear la cola vacía con deque()
# 3. Agregar las tareas
# 4. Imprimir el resultado, usando un while que procese las tareas en el orden de llegada

# Solución

impresion_Tareas = deque()

impresion_Tareas.append("Tarea 1")
impresion_Tareas.append("Tarea 2")
impresion_Tareas.append("Tarea 3")

while impresion_Tareas:
    tarea = impresion_Tareas.popleft()
    print(f"Procesando: {tarea}")

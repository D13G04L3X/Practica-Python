'''
Ejercicio 2: Simulación de una cola en espera
Simula una cola de atención al cliente, en un banco. Donde las personas son atendidas en el orden de llegada.
Cada persona se representa con su nombre.
'''

# Lógica
# 1. Definir la variable
# 2. Hacer una cola
# 3. Añadir los nombres
# 4. Bucle para la atención de las personas

# Solución

from collections import deque

cliente = deque()

# Personas que llegan a la fila
cliente.append("Juliana")
cliente.append("Roberto")
cliente.append("María Camila")
cliente.append("Camilo")

# Atención de las personas
while cliente:
    persona_atendida = cliente.popleft()
    print(f"Atendiendo a: {persona_atendida}")
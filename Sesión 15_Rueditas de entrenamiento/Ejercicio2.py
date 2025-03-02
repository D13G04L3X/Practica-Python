'''
Ejercicio 2: Cola de atención de un cajero automático
Simular una cola en un cajero automático. Las personas se agregan a la cola en el orden en que llegan y luego son 
atendidas una por una. Cada persona tiene un número de transacción.

"María", 101
"José", 102
"Raul", 103
'''

# Lógica
# 1. Crear una variable, cola_cajero
# 2. Se hace una cola, usando deque()
# 3. Agregar datos con .append()
# 4. Atender las personas, por medio de un while

# Solución

from collections import deque

cola_cajero = deque()

cola_cajero.append(("María", 101))
cola_cajero.append(("José", 102))
cola_cajero.append(("Raul", 103))

# Atender a las personas
while cola_cajero:
    cajero = cola_cajero.popleft()
    print(f"Atendiendo a {cajero[0]}, con la transacción número: {cajero[1]}")

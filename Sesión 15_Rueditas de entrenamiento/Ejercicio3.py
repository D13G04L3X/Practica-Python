'''
Ejercicio 3: Control de acceso a un evento
Simular el control de acceso a un evento, donde las personas deben hacer fila para ingresar. Cada persona se 
representa con su nombre, apellido y hora de llegada. Cada vez que una persona es autorizada a ingresar, se elimina
de la cola.

"Carlos", "Gómez", "10:00AM"
"Ana", "Martinez", "10:05AM"
"Luis", "Sánchez", "10:10AM"
"Lucía", "Jimenez", "10:20AM"
"Daniela", "Córdoba", "10:30AM"
'''

# Lógica
# 1. Llamar a la variable control_acceso
# 2. Hacer el control de acceso a un evento, se pone una lista vacía con deque()
# 3. Agregar datos con .append()
# 4. Hacemos un while, que llama a control_acceso
# 5. Imprimir en orden de llegada y eliminar por el mismo orden, con .popleft()

# Solución

from collections import deque

control_acceso = deque()

# Agregar datos
control_acceso.append(("Carlos", "Gómez", "10:00AM"))
control_acceso.append(("Ana", "Martinez", "10:05AM"))
control_acceso.append(("Luis", "Sánchez", "10:10AM"))
control_acceso.append(("Lucía", "Jimenez", "10:20AM"))
control_acceso.append(("Daniela", "Córdoba", "10:30AM"))

# Control acceso
while control_acceso:
    control = control_acceso.popleft()
    print(f"Autorizando a {control[0]} {control[1]} con hora de llegada: {control[2]}")

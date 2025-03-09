# Ejercicio 5: Simulación de una fila de atención telefónica.
#Simula una cola de atención telefónica en una empresa. Las personas que llaman se agregan a la cola en el orden
#En que llegan y se les atiende por orden de llegada. Cada persona se representa por su nombre y su número de teléfono.

#"Juan", "123-456-7890"
#"María", "234-567-8901"
#"Pedro", "345-678-9012"

# Hecho por Lorena

from collections import deque

atencion_telefonica = deque()

atencion_telefonica.append(("Juan", "123-456-7890"))
atencion_telefonica.append(("María", "234-567-8901"))
atencion_telefonica.append(("Pedro", "345-678-9012"))

while atencion_telefonica:
    atencion=atencion_telefonica.popleft()
    print(f"Atendiendo a {atencion[0]}, con número telefónico: {atencion[1]}")
'''
Ejercicio 3: Verificar si la cola está vacía
Crear una función que reciba una cola y verifique si está vacía o no
'''

# Lógica
# 1. Crear una variable: cola
# 2. Definir una función, verificamos por medio de condicionales
# 3. Con el isEmpty encontramos si está vacía o no

# Solución

from collections import deque

def esta_vacia(cola):
    if len(cola) == 0:
        return True
    else:
        return False
    
cola = deque([15, 7, 4, 20, 8])
print("¿La cola está vacía?: ", esta_vacia(cola))   # Debería devolver un False

cola.popleft()
cola.popleft()
cola.popleft()
cola.popleft()
cola.popleft()

print("¿La cola está vacía?: ", esta_vacia(cola))   # Debería devolver un True
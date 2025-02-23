# from collections import deque
'''
Cola, es una estructura de datos que sigue el principio FIFO (First in, first out), primero en entrar es el 
primero en salir
'''

cola = [1,2,3] 

# Agregar elementos por el final

print(cola)
cola.append(4)
print(cola)
cola.append(5)
print(cola)

print("Primer elemento de la cola: ", cola[0])

elemento = cola.popleft()

print("Elemento atendido: ", elemento)
print("Cola después de desencolar: ", list(cola))



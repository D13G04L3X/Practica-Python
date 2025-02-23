'''
Ejercicio 5: Simulación de un sistema de impresión
Simular una cola para imprimir documentos. Los documentos llegan en el orden en que se añaden a la cola, y la 
impresora imprime el primero que llegó.
'''

# Lógica
# 1. Definir la variable: imprimir_docs
# 2. Hacer una cola, usaremos un bucle para representar ese procedimiento cíclico
# 3. Imprimir documento entrante

# Solución

from collections import deque

imprimir_docs = deque()

# Agregar documentos
imprimir_docs.append("Documento1.pdf")
imprimir_docs.append("Documento2.pdf")
imprimir_docs.append("Documento3.pdf")
imprimir_docs.append("Documento4.pdf")

# Imprimir los documentos
while imprimir_docs:
    salir_docs = imprimir_docs.popleft()
    print(f"Se imprime el doc: {salir_docs}")
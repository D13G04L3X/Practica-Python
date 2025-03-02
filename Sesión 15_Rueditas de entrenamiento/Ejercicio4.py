'''
Ejercicio 4: Juego de cartas
Simular un juego de cartas donde las cartas se agregan a una cola. En cada turno, se toma la carta en el frente de la
cola y se muestra. Luego, la carta se coloca al final de la cola.

"As", "Rey", "Reina", "Joker", "10", "9"
'''

# Lógica
# 1. LLamar a la variable cartas
# 2. Hacer el juego de cartas, con deque() y agregarlos ahí mismo
# 3. Sacar la carta y mostrarla con el popleft()
# 4. Vamos a encolar la carta al final con append()

# Solución

from collections import deque

cartas = deque(["As", "Rey", "Reina", "Joker", "10", "9"])

# Mostrar la primera carta y moverla al final de la cola
for _ in range(len(cartas)):
    carta = cartas.popleft()
    print(f"Mostrando la: {carta}")
    cartas.append(carta)

print(cartas)
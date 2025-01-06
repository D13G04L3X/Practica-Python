# Pilas, son estructuras de datos que también se conocen por el término en inglés (Stack), se simulan en python usando
# listas. LIFO, Last in, first out. último en entrar, primero en salir

pila = [1,2,3] 

# Agregar elementos por el final

print(pila)
pila.append(4)
pila.append(5)
print(pila)

# Sacar elementos por el final

n = pila.pop()          # Método pop, también retorna el elemento que saca
print(f"Sacando el elemento {n}")
n = pila.pop()          # Método pop, también retorna el elemento que saca
print(f"Sacando el elemento {n}")

print(pila)
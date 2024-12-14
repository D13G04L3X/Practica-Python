# Colecciones - Conjuntos = Tipo de colección, los elementos que se agregan van a estar de forma desordenada, es que aquí no van haber duplicados

conjunto = set()                        # Conjunto vacío
conjunto = {}                           # Diccionario
conjunto = {1,2,3,"Hola",4.56}          # Conjunto    

print(conjunto)

# Para poder agregar datos el valor se puede poner donde quiera
conjunto.add(5)
conjunto.add("Adiós")
conjunto.add('a')
print(conjunto)

# Saber la longitud
print(len(conjunto))  

# Buscar un elemento
print(5 in conjunto)

# Eliminar un elemento
conjunto.discard(3)
print(conjunto)

# Vaciar todo el conjunto
conjunto.clear()
print(conjunto)

# También se pueden hacer operaciones aritmética con los conjuntos

# Ejemplo 1. -----

a = {1,2,3}
b = {3,4,5}

# Operaciones
# 1. Unión: Todos los elementos de los conjuntos unidos, línea
c = a | b 
print(c)

# 2. Intersección: Elementos en ambos conjuntos, ampersand
c = a & b
print(c)

# 3. Diferencia: Elementos que de a no están en b, menos
c = a - b
print(c)

# 4. Diferencia simétrica: Elementos que están en a y b, pero no ambos, elevado
c = a ^ b
print(c)

# Nota: La igualdad de dos conjuntos, se usa como verificación, para saber si son iguales
print(a == b)

# Ejemplo 2. -----

c = {1,2,3,4,5}

# Operaciones
# 5. Subconjunto: Creamos un conjunto de esos valores, para poder determinar si un conjunot es subconjunto de otro o que esté dentro del mismo
print(a.issubset(c))
print(b.issubset(c))        # Si le quito un elemento ya no es un conjunto como a

# 6. Superconjunto: Si c es un super conjunto que engloaba a un conjunto como a
print(c.issuperset(a))
print(c.issuperset(b))

# 7. Conjuntos disconexos: Que no comparten ningún elemento en común
print(a.isdisjoint(b))      # a y b comparten el elemento de 3, por lo tanto no serán disconexos

# 8. Conjuntos inmutables: Es como las tuplas que no se pueden modificar, se usa la función frozenset
a = frozenset({1,2,4})
a.add(3)
print(a)
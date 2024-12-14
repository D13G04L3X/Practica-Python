# Tuplas, colección parecida a la listas, además la diferencia es que son inmutables, que no se modifican
# nombre = ()

tupla = (4,"Hola",6.78,[1,2,3],4)
print(tupla)

# Se pueden mostrar un elemento en específico
print(tupla[1])

# Mostrar el índice del valor
print(5 in tupla)

# Mostrar un término en específico y nos dice su posición
print(tupla.index([1,2,3]))

# Mostrar la longitud de la tupla
print(len(tupla))

# Mostrar la cantidad de veces que está un valor en la tupla
print(tupla.count(4))

# Transformar una tupla en una lista y viceversa

# Tupla = Lista
lista = list(tupla)
print(lista)

# Lista - Tupla
tupla = tuple(lista)
print(tupla)

# La Ventaja que tiene la tupla, es que no consume tanto recursos en ejecución. Al momento de mostrar los datos de la tupla se van mostrar más rápido
# Se pueden unir listas,  c = a + b


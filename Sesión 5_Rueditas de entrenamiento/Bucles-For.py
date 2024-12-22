# Bucle - For = Determinado número de iteraciones o sea las veces que se va a repetir una condición
# Se utilizan colecciones, (Listas, Tuplas, Diccionarios, Conjuntos), va a recorrer los elementos de determinada colección con un iterador

# i in [lista]
for i in [2,10,3,4,"Juan"]:         # Repetir 5 veces porque es la cantidad de elementos que está recorriendo
    print("Hola mundo")

for i in [2,10,3,4,"Juan"]:
    print(f"El elemento: {i}")

# Se puede trabajar con diccionarios

coleccion = {"Diego":21,"Lorena":20,"María":23,"José":45,"Luis":12}

# Mostrar la clave
for i in coleccion:
    print(f"Elemento: {i}")

# Mostrar el valor
for i in coleccion:
    print(f"Elemento: {coleccion[i]}")            # Los [] tomar como el valor de las claves

# Mostrar clave y valor
for i in coleccion:
    print(f"elemento: {i}, {coleccion[i]}")

# Recorrer cadenas

coleccion = "Lorena"        # Número de elementos de la cadena

# Mostrar el mensaje x número de elementos
for i in coleccion:
    print(f"Hola")

# Mostrar caracter por caracter
for i in coleccion:
    print(f"{i}")

# Mostrar caracter x caracter sin salto de línea
for i in coleccion:
    print(f"{i}", end = "")

'''
# For tipo range, sin necesidad de darle caracter x caracter
for variable in range(n):
    cuerpo del bucle
'''

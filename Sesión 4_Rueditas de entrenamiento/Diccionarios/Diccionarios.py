# Colecciones - Diccionario, se guardan elementos desordenados, su principal caracteristica es que tiene 2 partes, La clave(no se epuede duplicar) y el valor
# Se usa como un dicccionario común, Traducción entre colores de español a inglés
# Clave:Valor
# Diccionario también acepta diferentes tipos de datos

diccionario = {"azul":"blue","rojo":"red","verde":"green"}      #Diccionario
print(diccionario)

# Mostrar el valor de una clave en especifico
print(diccionario["azul"])
print(diccionario["rojo"])

# Agregar nuevos elementos al diccionario, también se hace de forma desordenada
diccionario["amarillo"] = "yellow"
print(diccionario)

# Modificar un elemento
diccionario["azul"] = "BLUE"
print(diccionario)

# Eliminar un elemento del diccionario
del(diccionario["verde"])
print(diccionario)

# Crear una agenda ------
dictionary = {"Diego":{"edad":21,"estatura":1.82},"Lorena":[20,1.64],"José":[22,1.72],"María":[19,1.50]}
print(dictionary["Diego"])

# Crear un equipo ------
equipo = {6:"Richard Ríos",5:"Kevin Castaño",10:"James Rodriguez",11:"Jerry Mina"}
print(equipo)

# .get(): Para que cuando pidamos la clave y no la encuentre, coloque en pantalla un mensajito
print(equipo.get(6,"No existe en el equipo"))

# Hacer una búsqueda directa en el diccionario
print(11 in equipo)

# Mostrar solo las claves
print(equipo.keys())

# Mostrar solo los valores
print(equipo.values())

# Mostrar ambas cosas 
print(equipo.items())       # Pone dentro de paréntesis y es una tupla y luego las muestra

# Mostrar la cantidad de jugadores
print(len(equipo))

# Limpiar el diccionario
equipo.clear()
print(equipo)

# Listas - son como arreglos o vectores para otros lenguajes
# Los datos son más flexibles, que se pueda usar cualquier tipo de dato
# sentencia - instrccuón - ejecutar
# corchetes [los elementos,]

# Lista ejemplo
lista = ["Lunes","Martes","Miércoles","Jueves","Viernes",40,5.67,[1,2,3],True]
# print(lista)

# Imprimir varios elementos
print(lista[2],lista[4])
print(lista[:])

# Mostrar las listas inicio a fin o de fin a inicio
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])

# Métodos ------------------------------------------------
# Estructura base de una función o de un método: variable.función()

# 1. Len, Determinar la distancia que tiene una lista y su cantidad
print(len(lista))          

# Lista 2 ------------------------------------------------

lista2 = [1,2,4,5]

#2. Append, Insertar elementos al final de lista utilizando esta función
lista2.append(6)
print(lista2)

#3. Insert, insertar un elemento, en una posición específica: .insert(indice,valor)
lista2.insert(2,3)
print(lista2)

#4. Extend, Insertar varios elementos al final de la lista: .extend([valores,valores])
lista2.extend([7,8,9,10]) 
print(lista2)

#5. Sumar listas
lista3 = lista + lista2
print(lista3)

#6. in, Buscar elementos, se usa la función in, para saber si un dato dentro de la lista, devolver un True o un False
print(11 in lista3)

#7. Index, Buscar la ubicación exacta del elemento, retorna el índice del valor buscado, por ejemplo saber el valor de "Viernes"
print(lista3.index("Viernes"))

#8. Count, Para saber cuanta cantidad de valores hay en una lista, se le pasa el valor y nos va a mostrar la cantidad de veces que aparece en la lista
print(lista3.count(10))

#9. Pop, Eliminar el último elemento de la lista
lista3.pop()
print(lista3)

#10. Pop, para eliminar un indice exacto
lista3.pop(2)
print(lista3)

#11. Remove, sino sabemos el indice que queremos eliminar, usamos remove para el valor y eliminarlo
lista3.remove("Jueves")
print(lista3)

#12. Clear, Elimnar toda la lista
lista3.clear()
print(lista3)

#13. Reverse, Voltear la lista
lista3.reverse()
print(lista3)

#14. Copiar 2 veces los elementos de la lista
lista4 = [1,2,3,4,5]*2
print(lista4)

#15. Sort, Ordenar los valores o elementos de la lista de forma ascendente
lista5 = [5,4,-7,9,0,1,3]
lista5.sort()
print(lista5)

#16. Sort(reverse), Ordenar los valores de lista de forma descendente, el reverse altera el estado del sort por medio del booleano, True or False
lista5.sort(reverse = False)
print(lista5)








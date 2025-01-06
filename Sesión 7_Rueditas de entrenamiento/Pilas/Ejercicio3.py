'''
Ejercicio 3.
Eliminar duplicados consecutivos en una lista (pila)

Ejemplo: [1,2,2,2,3,4,4]
Salida: [1,2,3,4]
'''

# 1. Crear una pila
# 2. Insertarle valores
# 3. Recorrer la lista
# Si la pila está vacía o el elemento no es igual al tope, agregar

def eliminar_duplicados(lista):
    pila = []
    for elemento in lista:
        if not pila or pila[-1] != elemento:
            pila.append(elemento)
    return pila             # Identación necesaria con el for, no con el condicional

lista = input("Por favor, ingrese una lista: ")     # [1,2,2,2,3,4,4]         
print(eliminar_duplicados(lista))

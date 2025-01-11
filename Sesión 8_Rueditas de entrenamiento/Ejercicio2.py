'''
Ejercicio 2
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo 
de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le 
muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la 
mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es 
vegetariana o no y todos los ingredientes que lleva.
'''

# Menú
print("Bienvenido a la pizzería Bella Napoli. \n\tTipos de pizza\n\n\t- 1. Vegetariana \n\t- 2. No vegetariana\n")
tipo = input("Introduce el número del tipo de pizza que desees: ")

# Lógica
# Si elige 1, Vegetariana, lleva Pimiento, tofu, mozzarella y tomate
# Si elige 2, No vegetriana, lleva peperoni, Jamón, salmón, mozzarella y tomate

if tipo == "1":
    print("\nIngredientes de pizzas vegetarianas:\n\t - 1. Pimiento\n\t - 2. tofu\n")
    ingrediente = input("Introduce el número del tipo de ingrediente que desees: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("\nIngredientes de pizzas no vegetarianas:\n\t - 1. Peperoni\n\t - 2. Jamón\n\t - 3. Salmón\n")
    ingrediente = input("Introduce el número del tipo de ingrediente que desees: ")
    print("Pizza no vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")
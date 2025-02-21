'''
Ejercicio: Menú de restaurante
Problema: Dado un número del 1 al 3, mostrar el plato correspondiente:

1: Hamburguesa
2: Pizza
3: Pasta
Otro número: "Opción inválida"
'''

# Lógica

# 1. Definir la variable menu int
# 2. Definir el match con variable menu
# 3. Desarrollar el problema 
# 4. Cerrar con los case

# Solución

menu = int(input("Señor usuario, por favor elija entre las siguientes opciones: \n\n1: Hamburguesa \n2: Pizza \n3: Pasta\n\n"))

match menu:
    case 1:
        print("Elegiste: Hamburguesa")
    case 2:
        print("Elegiste: Pizza")
    case 3:
        print("Elegiste: Pasta")
    case _:
        print("Opción inválida")
'''
Match - case, es una estructura de control, este también emula la función que tiene un switch. Este se usa para comparar
un valor con diferentes casos y que a su vez nos permite ejecutar el código según una coincidencia.
'''

# Sintaxis básica:

'''
match variable:
    case valor1:
        # Código si variable (instrucción) == valor1
    case valor2:
        # Código si variable (instrucción) == valor1
    case _:
        # Código si vno coincide con ningún caso
'''

# Ejemplo: vamos a hacer un pequeño menú:

menu = int(input("Señor usuario, por favor ingrese un número del 1-3: "))

match menu:
    case 1:
        print("Elegiste la opción 1.")
    case 2: 
        print("Elegiste la opción 2.")   
    case 3:
        print("Elegiste la opción 3.") 
    case _:
        print("número u opción inválida.") 

'''
Ventajas: 
- Es más limpio y ordenado que por ejemplo: if-elif-else.
- Funciona con números, cadenas, u otro tipo de datos.
- Se pueden combinar valores en el mismo case.

'''
    
# Ejemplo: cual es vocal y cual no es vocal.

letra = input("Por favor ingrese una letra: ")

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("Es una vocal.")
    case _:
        print("No es una vocal, es una consonante")

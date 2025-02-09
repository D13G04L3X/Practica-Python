'''
Ejercicio 2: Conversión de notas a calificación
Dado un número del 1 al 5, imprime su equivalente en calificación, como está a continuación:

- 1 o 2: "Insuficiente"
- 3: "Aceptable"
- 4: "Bueno"
- 5: "Excelente"
- Cualquier otro número: "Nota no válida"

'''

# Lógica

# Se pide la variable nota
# Se llama al match y a la variable
# Se llama al case 1, 2, etc...
# Se cierra con el case_.

# Solución

nota = int(input("Estudiante, por favor ingresar su nota obtenida en el parcial: "))

match nota:
    case 1 | 2:
        print("Calificación insuficiente.")
    case 3:
        print("Calificación aceptable.")
    case 4:
        print("Calificación buena.")
    case 5:
        print("Calificación excelente.")
    case _:
        print("Calificación no válida.")

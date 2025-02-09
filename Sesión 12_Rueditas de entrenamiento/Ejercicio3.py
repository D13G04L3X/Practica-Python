'''
Ejercicio 3: Identificar tipo de animal
Dado el nombre de un animal, indicar si es un mamífero, ave u otro.

perro = mamífero
gato = mamífero
elefante = mamífero
águila = ave
loro = ave
paloma = ave

'''

# Lógica

# Definiendo la variable tipo_animal
# Llamar al match y a la variable
# Definimos los case 
# Cerrar con case _.

# Solución

tipo_animal = input("Señor usuario, por favor escriba el nombre de un animal: ").lower()

match tipo_animal:
    case "perro" | "gato" | "elefante":
        print("Es un mamífero.")
    case "águila" | "loro" | "paloma":
        print("Es un ave.")
    case _:
        print("Es otro tipo de especie.")
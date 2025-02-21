#Identificar dias laborables o fin de semana

#Dado un día de la semana, indicar si es laborable o fin de semana. 

# Hecho por: Lorena

dia_semana = input("Ingrese un día de la semana, por favor: ").lower()

match dia_semana:
    case "lunes" | "martes" | "miércoles" | "jueves" | "viernes":
        print ("Es día laborable")
    case "sábado" | "domingo":
        print ("Fin de semana")
    case _:
        print ("Incorrecto, ingrese un día por favor")

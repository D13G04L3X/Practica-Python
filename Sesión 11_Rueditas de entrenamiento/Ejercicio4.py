'''
Ejercicio 4.

Mensaje de saludo según la hora
El programa debe saludar de manera diferente según la hora del día. Si es antes de las 12, "¡Muy buenos días!",
entre las 12 y las 18, "¡Muy buenas tardes!", y después de las 18, "¡Muy buenas noches!".

'''

def saludo(hora):
    if hora <= 12:
        return "¡Muy buenos días!"
    elif hora > 12 & hora <= 18:
        return "¡Muy buenas tardes!"
    else:
        return "¡Muy buenas noches!"
    
hora = int(input("Ingresa una hora: "))
print(saludo(hora))    

print(saludo(7))    # ¡Muy buenos días!
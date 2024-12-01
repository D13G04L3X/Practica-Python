# Condicionales

''' 
Ejemplo: Validar si un número es positivo o negativo
Solución: Lo que sea mayor a 0, vamos a decir que es positivo, caso contrario negativo
'''
numero = float(input("Digite un número: "))

# Sentencia If, condición, instrucción
if numero > 0:  
    print("El número es positivo")              # Identación = Espaciado inicial o una tabulación o una sangría
elif numero == 0:
    print("El resultado es 0 y es positivo")
else: 
    print("El número es negativo")

# Condicionales anidados

''' 
Ejemplo: Validar si una persona es mayor de edad, y que el resultado sea decir si es mayor de edad o no
Solución: Si edad es mayor o igual a 18 es mayor de edad, caso contrario es menor de edad
'''
edad = int(input("Digite su edad: "))

if edad > 0 and edad < 100:
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor edad")
else:
    print("Edad incorrecta")
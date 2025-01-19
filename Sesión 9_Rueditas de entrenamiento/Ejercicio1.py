#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo
#como el de más abajo, de altura el número introducido
#°
#°°
#°°°
#°°°°
#°°°°°

# Hecho por Lorena
#pedir al usuario un número entero
altura=int(input("Introduce un número por favor: "))

#Generar rl triángulo rectángulo
for i in range (1, altura + 1):
    print("°" * i)
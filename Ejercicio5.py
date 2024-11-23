# Ejercicio 5
# Escribir un programa que pida al usuario su peso (en kg) y la estatura (en metros), calular el indice de masa corporal
# y lo almacenamos en una variable y mostrar por pantalla la frase "Tu índice de masa corporal es <imc>" donde <imc>
# ese es el índice de masa corporal calculado redondeado con 2 decimales

# Solución:
# pedir el peso (en kg)
# pedir la estatura (en metros)
# imc (como el resultado del índice de masa corporal)
# mostrar el siguiente resultado: Tu índice de masa corporal es <imc>

# 1. Pedir las variables
peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en? ")

# 2. Procedimiento
imc = round(float(peso)/float(estatura)**2,2)

# 3. Resultado
print ("Tu índice de masa corporal es: " + str(imc))



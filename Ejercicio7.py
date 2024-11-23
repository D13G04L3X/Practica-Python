# Ejercicio 11
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido 
# a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir 
# un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el 
# usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y 
# tercer año. Redondear cada cantidad a dos decimales.

# Solución:
# pedir la inversion inicial
# el interés = 0.04 
# Calcular el balance por año = balance 1 * (1 + intereses), balance 2 * (1 + intereses)
# (Balance 1, balance 2 y balance 3 ),2 (esto es para el redondeo)
#  Mostrar en pantalla (la cantidad de ahorros x año)

# 1. Pedir las variables
inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04

# 2. Procedimiento
balance1 = inversion * (1 + interes)
balance2 = balance1 * (1 + interes)
balance3 = balance2 * (1 + interes)

# 3. Resultado
print ("Balance tras haber pasado el 1 año es: " + str(round(balance1, 2)))
print ("Balance tras haber pasado el 2 años es: " + str(round(balance2, 2)))
print ("Balance tras haber pasado el 3 años es: " + str(round(balance3, 2)))

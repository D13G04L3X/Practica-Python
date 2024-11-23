# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la 
# empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas  
# que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el 
# número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado

# Solución:
# payaso = 112 g
# muñeca = 75 g
# Calcular el peso de cada uno
# Calular Payasos y muñecas vendidos
# Calular el peso total del paquete

# 1. Pedir las variables
peso_payaso = 112
peso_muneca = 75

payasos = int(input("Introduce el número de payasos a enviar: "))
munecas = int(input("Introduce el número de muñecas a enviar: "))

# 2. Procedimiento
peso_total = peso_payaso * payasos + peso_muneca * munecas

# 3. Resultado
print ("El peso total del paquete es: " + str(peso_total))




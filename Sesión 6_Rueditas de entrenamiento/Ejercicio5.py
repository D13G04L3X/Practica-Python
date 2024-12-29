'''
Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre 
por pantalla el capital obtenido en la inversión cada año que dura la inversión.

'''

# cant_inversion = 1000
# interes_anual = 10% = 0,1
# años = 5

# Resultado obtenido:
# 1 año = 1100
# 2 año = 1210
# 3 año = 1331
# 4 año = 1464,1
# 5 año = 1610,51

cant_inversion = float(input("Señor usuario, ¿Cuál es la cantidad que desea invertir? "))
interes_anual = float(input("Señor usuario, ¿Cuál es la interés anual? "))
años = int(input("Señor usuario, ¿A cuantos años desea hacer su inversión? "))
for i in range(años):
    cant_inversion *= 1 + interes_anual / 100           # cant_inversion * intereses 
    print("El capital tras " + str(i+1) + " años es de: " + str(round(cant_inversion, 2)))

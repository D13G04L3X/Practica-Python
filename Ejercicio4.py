#Ejercicio 5
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

# Necesitamos una variable que almacene las horas de trabajo = float horas
# Necesitamos una variable que almacene las horas de trabajo = float coste
# paga = horas * coste
# print ("Tu paga es: ", paga)
# print concatenado para numeros = , y para string = +

# 1. Pedir las variables
horas = float(input("Introduce tus horas de trabajo: ")) 
coste = float(input("Introduce lo que cobras por hora de trabajo: ")) 

# Procedimiento
paga = horas * coste

#Resultado
print("Tu paga es: $", paga)



# Ejercicios

'''
Ejercicio 1: Hacer un programa que pida 2 números y se de cuenta cuál de ellos es par,
o si ambos lo son. 
'''
# F-string = Es para poder concatenar una cadena de texto con numeros

num1 = int(input("Digite un número: "))
num2 = int(input("Digite un número: "))

if num1%2==0 and num2%2==0:                 # 4 y 4 = Ambos pares
    print("Ambos números son pares")
elif num1%2==0 and num2%2!=0:               # 4 y 5 = el 4(num1) es par
    print(f"{num1} es par")
elif num1%2!=0 and num2%2==0:               # 5 y 4 = el 5(num2) es par
    print(f"{num2} es par")
else:                                       # 5 y 5 = Ambos impares       
    print("Ambos números son impares")


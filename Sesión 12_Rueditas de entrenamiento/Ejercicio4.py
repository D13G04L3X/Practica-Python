'''
Ejercicio 4: Calculadora básica
Dado 2 números y una operación (+, -, *, /), realizar la operación correspondiente.

'''

# Lógica

# Se define una variable a, b, operador
# Llamar al match y la variable
# Definir los case
# En el case de / vamos a colocar una condición para el caso de división entre 0

# Solución

num1 = float(input("Por favor ingresa el primer número: "))
num2 = float(input("Por favor ingresa el segundo número: "))
op = input("Por favor ingresa el tipo de operación (+, -, *, /): ")

match op:
    case "+":
        print(f"Resultado: {num1 + num2}")
    case "-":
        print(f"Resultado: {num1 - num2}")
    case "*":
        print(f"Resultado: {num1 * num2}")
    case "/":
        print(f"Resultado: {num1 / num2}" if num2 != 0 else "División por cero, inválida.")
    case _:
        print("Tipo de operador erróneo.")
        

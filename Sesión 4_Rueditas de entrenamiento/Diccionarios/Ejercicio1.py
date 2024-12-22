''' 
Ejercicio 1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al 
usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''


monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}             # Diccionario
moneda = input("Introduce una divisa: ")                    # Variable

# Solución 1
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")

# Solución 2
print(monedas.get(moneda.title(), "La divisa no está."))


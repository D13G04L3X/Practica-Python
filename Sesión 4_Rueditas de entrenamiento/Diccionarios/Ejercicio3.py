'''
Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una 
fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el 
diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
'''

frutas = {'Plátano':1.35, 'Manzana':0.80, 'Pera':0.85, 'Naranja':0.70}
fruta = input("¿Qué fruta desea comprar? ").title()
kg = float(input("Por favor introduzca el peso en kilos de la fruta: "))

if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
else:
    print("Señor usuario, la fruta ", fruta, "no se encuentra registrada.")


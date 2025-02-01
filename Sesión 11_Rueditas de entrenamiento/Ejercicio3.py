'''
Ejercicio 3.

Calcular el precio según el tipo de cliente.
Escribe un programa que calcule el precio de un producto dependiendo del tipo de cliente: "normal", "vip" o "socio"

normal = 100
vip = 80
socio = 50

'''

def precio_producto(tipo_cliente):
    tip_cliente = {
        "normal": 100,
        "vip": 80,
        "socio": 1000
    }
    return tip_cliente.get(tipo_cliente, "Tipo de cliente no válido")

print(precio_producto("socio"))

'''
Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono
es <teléfono>. 
'''

nombre = input("Por favor, escriba su nombre: ")
edad = input("Por favor, escriba su edad: ")
direccion = input("Por favor, escriba su dirección: ")
telefono = input("Por favor, escriba su número de teléfono: ")

datos = {'nombre':nombre,'edad':edad,'dirección':direccion,'teléfono':telefono}

# <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>
print(datos['nombre'], 'tiene', datos['edad'], 'años, vive en', datos['dirección'], 'y su número de teléfono es', datos['teléfono'])

'''
Ejercicio 1     // Hecho por: Lorena
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma 
automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del 
cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 
18 años debe pagar 5€ y si es mayor de 18 años, 10€.
'''

# 1.Preguntar la edad y mostrar precio de la entrada
# 2. Si el cliente es menor de 4 años puede entrar gratis
# 3. Si tiene entre 4 y 18 años debe pagar 5€
# 4. Si es mayor de 18 años, 10€.

edad_cliente = int(input("Señor usuario, escriba por favor su edad: "))

if edad_cliente > 1 and edad_cliente < 4: 
    print("Entra gratis")
elif edad_cliente >= 4 and edad_cliente <= 18:
    print("Tiene ", edad_cliente, " años, por lo tanto debe pagar 5€.") 
elif edad_cliente >=18 and edad_cliente <=100:
    print ("Es mayor de 18 añor, debe pagar 10€")    
else:
    print("Edad incorrecta.")


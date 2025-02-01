'''
Switch es una estrutura de control, que nos permite ejecutar diferentes secciones de código, dependiendo de una 
condición. Ssu funcionalidad es muy similar a la de usar varios if

case = casos, que son los nosotros definimos como las condiciones que componen al switch

La estructura es:

switch ():

case 1:
    instrucción

case 2:
    instrucción

    break:
'''

# Vamos a ejecutar un if anidado, dependiendo de determinada condición 

condicion = int(input("Ingrese un número: "))

if condicion == 1:
    print("Haga a")
elif condicion == 2:
    print("Haga b")
elif condicion == 3:
    print("Haga c")
else:
    print("Haga d")

# Vamos a ejecutar un switch

'''
switch(condicion) {
       case 1:
    // haga a
        case 2:
    // haga b
        case 3:
    // haga c
        case 4:
    // haga d
    break:
    // default haga x
}
'''

# Emular un switch en python
# Hacer uso de un diccionario, para el siguiente código:

def opera1(operador, a, b):
    if operador == "suma":
        return a + b
    elif operador == "resta":
        return a - b
    elif operador == "multiplicación":
        return a * b
    elif operador == "división":
        return a / b
    else:
        return None
    
# conversión

def opera2(operador, a, b):
    return{
        'suma': lambda: a + b,
        'resta': lambda: a - b,
        'multiplicación': lambda: a * b,
        'división': lambda: a / b,
    }.get(operador, lambda: None)

opera1('suma', 5, 9)
# Salida: 14

opera2('suma', 5, 9)()
# Salida: 14
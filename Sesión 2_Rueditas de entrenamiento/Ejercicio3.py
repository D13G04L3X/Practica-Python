'''
Ejercicio 3: Hacer una calculadora con interfaz gráfica usando 
'''

from tkinter import *            #Esta es una libreria integrada de python que se usa usa para la creación de interfaces gráfica de usuario (GUI, sigla de inglés interfaz gráfica)

ventana = Tk()
ventana.title("Calculadora")
ventana.configure(bg="#2b2b2b")

# --- Hasta este punto ya tenemos una ventanita emergente ---       

i = 0               # Inicializa la variable
resultado_mostrado = False  # Bandera para verificar si se mostró un resultado

# --- Entrada de texto ---
e_texto = Entry(ventana, font = ("Calibri 15"), bg = '#eeeeee', justify = RIGHT)
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 15, pady = 15)

# --- Funciones ---
#def click_boton(valor):
#    global i           #El indice nos dice en que posición se muestran los datos, i + 1, para que se mueva
#    e_texto.insert(i, valor)            # Si queremos conectar el método a una función, usaremos el command
#    i += 1                              # Este es la función para correr el número y que copie a la derecha

def click_boton(valor):
    global i, resultado_mostrado
    if resultado_mostrado:  # Si un resultado ha sido mostrado
        e_texto.delete(0, END)  # Limpia el cuadro de texto
        i = 0  # Resetea el índice
        resultado_mostrado = False  # Reinicia la bandera
    e_texto.insert(i, valor)  # Inserta el nuevo valor
    i += 1  

def borrar():
    e_texto.delete(0, END)
    i = 0               # Con esto se resetea la cuenta y a los valores van volver al inicio

def operaciones():
    global i, resultado_mostrado
    try:
        ecuacion = e_texto.get()  # Captura la ecuación ingresada
        resultado = eval(ecuacion)  # Evalúa la ecuación
        e_texto.delete(0, END)
        e_texto.insert(0, resultado)  # Muestra el resultado
        i = len(str(resultado))  # Ajusta el índice al nuevo resultado
        resultado_mostrado = True  # Activa la bandera de resultado mostrado
    except Exception:
        e_texto.delete(0, END)
        e_texto.insert(0, "Error")  # Manejo de errores
        resultado_mostrado = True

#def operaciones():
#    ecuacion = e_texto.get()        #Coge lo que hay en el texto y luego almacena en la ecuación
#    resultado = eval(ecuacion)      #función matemática, resuelve cadenas de caracetres como ecuaciones
#    e_texto.delete(0, END)
#    e_texto.insert(0, resultado)
#    i = 0

# --- Botones ---
boton1 = Button(ventana, font = ("Calibri 12"), text = "1", width = 5, height = 2, bg = '#2196f3', command = lambda: click_boton(1))
boton2 = Button(ventana, font = ("Calibri 12"), text = "2", width = 5, height = 2, bg = '#2196f3', command = lambda: click_boton(2))
boton3 = Button(ventana, font = ("Calibri 12"), text = "3", width = 5, height = 2, bg = '#2196f3', command = lambda: click_boton(3))
boton4 = Button(ventana, font = ("Calibri 12"), text = "4", width = 5, height = 2, bg = '#2196f3', command = lambda: click_boton(4))
boton5 = Button(ventana, font = ("Calibri 12"), text = "5", width = 5, height = 2, bg = '#2196f3', command = lambda: click_boton(5))
boton6 = Button(ventana, font = ("Calibri 12"), text = "6", width = 5, height = 2, bg = '#2196f3', command = lambda: click_boton(6))
boton7 = Button(ventana, font = ("Calibri 12"), text = "7", width = 5, height = 2, bg = '#2196f3', command = lambda: click_boton(7))
boton8 = Button(ventana, font = ("Calibri 12"), text = "8", width = 5, height = 2, bg = '#2196f3', command = lambda: click_boton(8))
boton9 = Button(ventana, font = ("Calibri 12"), text = "9", width = 5, height = 2, bg = '#2196f3', command = lambda: click_boton(9))
boton0 = Button(ventana, font = ("Calibri 12"), text = "0", width = 13, height = 2, bg = '#2196f3', command = lambda: click_boton(0))

boton_borrar = Button(ventana, font = ("Calibri 12"), text = "AC", width = 5, height = 2, bg = '#f33e21', command = lambda: borrar())
boton_parentesis1 = Button(ventana, font = ("Calibri 12"), text = "(", width = 5, height = 2, bg = '#21f3f0', command = lambda: click_boton("("))
boton_parentesis2 = Button(ventana, font = ("Calibri 12"), text = ")", width = 5, height = 2, bg = '#21f3f0', command = lambda: click_boton(")"))
boton_punto = Button(ventana, font = ("Calibri 12"), text = ".", width = 5, height = 2, bg = '#21f3f0', command = lambda: click_boton("."))

boton_suma = Button(ventana, font = ("Calibri 12"), text = "+", width = 5, height = 2, bg = '#21f3f0', command = lambda: click_boton("+"))
boton_resta = Button(ventana, font = ("Calibri 12"), text = "-", width = 5, height = 2, bg = '#21f3f0', command = lambda: click_boton("-"))
boton_multipl = Button(ventana, font = ("Calibri 12"), text = "x", width = 5, height = 2, bg = '#21f3f0', command = lambda: click_boton("*"))
boton_division = Button(ventana, font = ("Calibri 12"), text = "÷", width = 5, height = 2, bg = '#21f3f0', command = lambda: click_boton("/"))
boton_igual = Button(ventana, font = ("Calibri 12"), text = "=", width = 5, height = 2, bg = '#21f371', command = lambda: operaciones())

# --- Agregar botones en pantalla ---
# - Fila 1
boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_division.grid(row = 1, column = 3, padx = 5, pady = 5)

# - Fila 2
boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_multipl.grid(row = 2, column = 3, padx = 5, pady = 5)

# - Fila 3
boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_suma.grid(row = 3, column = 3, padx = 5, pady = 5)

# - Fila 4
boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_resta.grid(row = 4, column = 3, padx = 5, pady = 5)

# - Fila 5
boton0.grid(row = 5, column = 0, columnspan = 2,  padx = 5, pady = 5)
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5)

ventana.mainloop()            # es una función que ayuda a que el aplicativo sea cíclico, entre tkinter lo reconozca y que los eventos pasen

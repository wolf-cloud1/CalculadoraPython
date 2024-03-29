from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

i = 0 # variable de indice

# Entrada de texto
e_texto = Entry (ventana, font = ("Calibri 20")) # entrada de texto
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 5) # Caja de texto

# Funciones
def click_boton(valor):
    global i
    e_texto.insert(i, valor) # Le paso indice 0 y el argumento valor
    i += 1 # cada vez que ingrese un valor se irá para la derecha del indice 0 

def borrar():
    e_texto.delete(0, END)  # Le paso la funcion delete para borrar y los parametros desde el indice 0 hasta el final (END).
    i = 0 # Resetea el indice a 0.

def hacer_operacion():
    ecuacion = e_texto.get() # Le paso todo lo que ingrese en la caja de texto
    result = eval(ecuacion) # le paso la funcion eval
    e_texto.delete(0, END) # desde el indice 0 hasta el final
    e_texto.insert(0, result) # en el indice 0 que muestre el resultado
    i = 0 # Volver a 0 el indice

# Botones
boton1 = Button(ventana, text = "1", width = 5, height = 2, command = lambda: click_boton(1)) # para conectar el boton con la funcion debo ocupar la funcion COMMAND
boton2 = Button(ventana, text = "2", width = 5, height = 2, command = lambda: click_boton(2)) # Le paso parametros a todas las funciones del 0 al 9
boton3 = Button(ventana, text = "3", width = 5, height = 2, command = lambda: click_boton(3))
boton4 = Button(ventana, text = "4", width = 5, height = 2, command = lambda: click_boton(4))
boton5 = Button(ventana, text = "5", width = 5, height = 2, command = lambda: click_boton(5))
boton6 = Button(ventana, text = "6", width = 5, height = 2, command = lambda: click_boton(6))
boton7 = Button(ventana, text = "7", width = 5, height = 2, command = lambda: click_boton(7))
boton8 = Button(ventana, text = "8", width = 5, height = 2, command = lambda: click_boton(8))
boton9 = Button(ventana, text = "9", width = 5, height = 2, command = lambda: click_boton(9))
boton0 = Button(ventana, text = "0", width = 13, height = 2, command = lambda: click_boton(0))
# Botones 
boton_borrar = Button(ventana, text = "AC", width = 5, height = 2, command = lambda: borrar()) # Le paso funcion de borrar
boton_parentesis1 = Button(ventana, text = "(", width = 5, height = 2, command = lambda: click_boton("(")) # Le paso los parametros de los simbolos math.
boton_parentesis2 = Button(ventana, text = ")", width = 5, height = 2, command = lambda: click_boton(")"))
boton_punto = Button(ventana, text = ".", width = 5, height = 2, command = lambda: click_boton("."))
# botones matematicos
boton_div = Button(ventana, text = "/", width = 5, height = 2, command = lambda: click_boton("/"))
boton_mult = Button(ventana, text = "x", width = 5, height = 2, command = lambda: click_boton("*"))
boton_sum = Button(ventana, text = "+", width = 5, height = 2, command = lambda: click_boton("+"))
boton_rest = Button(ventana, text = "-", width = 5, height = 2, command = lambda: click_boton("-"))
boton_igual = Button(ventana, text = "=", width = 5, height = 2, command = lambda: hacer_operacion())

# Agregar botones en pantalla.
boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_div.grid(row = 1, column = 3, padx = 5, pady = 5)

boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_mult.grid(row = 2, column = 3, padx = 5, pady = 5)

boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_rest.grid(row = 4, column = 3, padx = 5, pady = 5)


boton0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5)

ventana = mainloop()

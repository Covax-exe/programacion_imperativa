"""Descripción: Crea una aplicación GUI en Python utilizando Tkinter. La aplicación debe tener
las siguientes características:
Un campo de entrada donde el usuario pueda ingresar un número.
Un botón que, cuando se presione, agregue el número ingresado a una lista.
Un área de texto que muestre todos los números en la lista, cada uno en una nueva línea.
Un botón que, cuando se presione, muestre el número más grande, el más pequeño y
la suma de todos los números en la lista en un cuadro de mensaje."""

from tkinter import *


vPpal = Tk()
vPpal.geometry("500x400")
vPpal.title("Manejo Números")
numeros = []

# paneles
panelDatos = Frame(vPpal)

# funciones botones
def agregarNumero():
    global numeros
    entryNumero = int(eNumero.get())
    numeros.append(entryNumero)
    eNumero.delete(0, END) # borrar cuando se ingresa un número
    aTexto.delete('1.0',END)
    aTexto.insert(END, str(numeros))

def mostrarMaxMin():
    mayor = max(numeros)
    menor = min(numeros)
    aTexto.delete('1.0', END)
    aTexto.insert(END, f"El número más grande es: {mayor} \nEl número más pequeño es: {menor}")

def sumaNumeros():
    suma = sum(numeros)
    aTexto.delete('1.0', END)
    aTexto.insert(END, f"La suma de todos los números ingresados en la lista es: {suma}")

def mostrarLista():
    aTexto.delete('1.0',END)
    aTexto.insert(END, str(numeros))

# texto
lNumero = Label(panelDatos, text = "Ingrese un número:").grid(row = 0, column = 0)

# botones
bAgregar = Button(panelDatos, text = "Agregar número a la lista", command = agregarNumero, bg = "PaleGreen1")
bMostrar = Button(panelDatos, text = "Mostrar número más pequeño y más grande", command = mostrarMaxMin, bg = "VioletRed1")
bSuma = Button(panelDatos, text = "Mostra suma de todos los números", command = sumaNumeros, bg = "powder blue")
bLista = Button(panelDatos, text = "Mostrar lista", command = mostrarLista, bg = "papaya whip")


# entrada
eNumero = Entry(panelDatos, width = 20)

# impresion
aTexto = Text(panelDatos, height = 10, width = 50)

# ubicar
eNumero.grid(row = 0, column = 1)
bAgregar.grid(row = 1, column = 1)
bMostrar.grid(row = 2, column = 0)
bSuma.grid(row = 2, column = 1)
aTexto.grid(row = 3, column = 0, columnspan = 3)
bLista.grid(row = 1, column = 0)


# fijar
panelDatos.pack()


vPpal.mainloop()
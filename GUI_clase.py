"ELEVAR AL CUADRADO"

from tkinter import *

def calcular():
    if len(eValorA.get().strip()) != 0:
        valorA = int(eValorA.get().strip()) #.strip() quita los espacios antes y después de un string // .get() trae lo que está en la variable
        eValorA.delete(0, END) #para que borre el campo después de obtener el valor
        potencia = valorA**2
        eResultado.delete(0,END)
        eResultado.insert(0, potencia)
        
    else:
        eResultado.delete(0, END)
        eResultado.insert(0, "No ha ingresado número")
    





#------------------------------GUI------------------------------------
vPpal = Tk()
vPpal.geometry("250x140")
vPpal.title("GUI 1")

#crear componentes de la GUI
lValorA = Label(vPpal, text = "Valor a: ")
lResultado = Label(vPpal, text = "Resultado: ")
eValorA = Entry(vPpal, width = 10)
eResultado = Entry(vPpal, width = 30)
bCalcular = Button(vPpal, text = "Pow(a,2)", command = calcular) #nombre función sin parentensis

lValorA.pack()
eValorA.pack()
bCalcular.pack()
lResultado.pack()
eResultado.pack()

vPpal.mainloop()

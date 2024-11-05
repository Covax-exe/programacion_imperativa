"CALCULADORA :)"

from tkinter import *

def suma():
    eResultado.delete(0, END)
    
    if len((eNumeroA.get().strip())) != 0 and len(eNumeroB.get().strip()) != 0:
        a = float(eNumeroA.get().strip())
        b = float(eNumeroB.get().strip())
        VSuma = a + b
        eResultado.insert(0, VSuma)
    else:
        eResultado.insert(0, "Faltan datos")

def multiplicacion():
    eResultado.delete(0, END)
    
    if len((eNumeroA.get().strip())) != 0 and len(eNumeroB.get().strip()) != 0:
        a = float(eNumeroA.get().strip())
        b = float(eNumeroB.get().strip())
        VMulti = a * b
        eResultado.insert(0, VMulti)
    else:
        eResultado.insert(0, "Faltan datos")

def division():
    eResultado.delete(0, END)
    
    if len((eNumeroA.get().strip())) != 0 and len(eNumeroB.get().strip()) != 0:
        a = float(eNumeroA.get().strip())
        b = float(eNumeroB.get().strip())
        if b != 0:
            VDiv = a / b
            eResultado.insert(0, VDiv)
        else:
            eResultado.insert(0,"No se puede dividir entre 0")   
    else:
        eResultado.insert(0, "Faltan datos")
        

#componentes de la GUI

vPpal = Tk() #crear ventana
vPpal.geometry("350x150") #tamaño ventana
vPpal.title("Calculadora Sencilla") #titulo de ventana

panelDatos = Frame(vPpal)
panelBotones = Frame(vPpal)

lNumeroA = Label(panelDatos, text = "Número a: ").grid(row = 0, column = 0) #organiza las cosas como si fuera una tabla :) // fila y columna
lNumeroB = Label(panelDatos, text = "Número b: ").grid(row = 1, column = 0)
lResultado = Label(panelDatos, text = "Resultado: ").grid(row = 2, column = 0)

eNumeroA = Entry(panelDatos, width = 15)
eNumeroB = Entry(panelDatos, width = 15)
eResultado = Entry(panelDatos, width = 15)
eNumeroA.grid(row = 0, column = 1)
eNumeroB.grid(row = 1, column = 1)
eResultado.grid(row = 2, column = 1)

bSumar = Button(panelBotones, text = "     +     ",bg = "lightblue", command = suma).grid(row = 0, column = 0)
bMultiplicar = Button(panelBotones, text = "     *     ", bg = "lightblue", command = multiplicacion).grid(row = 0, column = 1)
bDividir = Button(panelBotones, text = "     /     ", bg = "lightblue", command = division).grid(row = 0, column = 2)



#fijar el panel a la ventana principal
panelDatos.pack()
panelBotones.pack()

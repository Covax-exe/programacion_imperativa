"""En un teatro se venden boletos en dos ubicaciones (Palco y Platea) y en dos modalidades (Pre-venta y
Venta Normal). Los valores unitarios de los boletos dependen de la ubicación y del tipo de venta, y se calculan usando la
siguiente tabla. Como política del teatro, se reserva de cada venta realizada el 25% como aporte para el mantenimiento
del mismo.
Considere la interfaz gráfica que se muestra en la Figura 1. Desarrolle la función asociada al botón Calcular valores
que haga el cálculo del valor de la venta y del aporte para cualquier entrada. Debe mostrar en las entradas
eValorVenta y eAporte, los valores correspondientes."""

from tkinter import *


def ventaBoletas():
    vPpal = Tk()
    vPpal.geometry("300x150")
    vPpal.title("Venta de Boletas")

    # paneles
    panelDatosUp = Frame(vPpal)
    panelDatosDown = Frame(vPpal)

    # función del botón
    def Calculo():
        entryUbicacion = str(eUbicacion.get())
        entryTipoVenta = str(eTipoVenta.get())
        entryCantidad = int(eCantidad.get())
        minusUbicacion = entryUbicacion.lower()
        minusTipoVenta = entryTipoVenta.lower()

        if minusUbicacion == "palco" and minusTipoVenta == "preventa":
            vVenta = 22000 * entryCantidad
            vAporte = vVenta * 0.25
            eAporte.delete(0, END)
            eAporte.insert(0, vAporte)
            eValorVenta.delete(0, END)
            eValorVenta.insert(0, vVenta)
        elif minusUbicacion == "palco" and minusTipoVenta == "venta normal":
            vVenta = 29000 * entryCantidad
            vAporte = vVenta * 0.25
            eAporte.delete(0, END)
            eAporte.insert(0, vAporte)
            eValorVenta.delete(0, END)
            eValorVenta.insert(0, vVenta)
        elif minusUbicacion == "platea" and minusTipoVenta == "preventa":
            vVenta = 30000 * entryCantidad
            vAporte = vVenta * 0.25
            eAporte.delete(0, END)
            eAporte.insert(0, vAporte)
            eValorVenta.delete(0, END)
            eValorVenta.insert(0, vVenta)
        elif minusUbicacion == "platea" and minusTipoVenta == "venta normal":
            vVenta = 38000 * entryCantidad
            vAporte = vVenta * 0.25
            eAporte.delete(0, END)
            eAporte.insert(0, vAporte)
            eValorVenta.delete(0, END)
            eValorVenta.insert(0, vVenta)
        else:
            eTipoVenta.delete(0, END)
            eTipoVenta.insert(0, "Valores no válidos.")


    # texto
    lUbicacion = Label(panelDatosUp, text = "Ubicación:").grid(row = 0, column = 0)
    lTipoVenta = Label(panelDatosUp, text = "Tipo:").grid(row = 1, column = 0)
    lCantidad = Label(panelDatosUp, text = "Cantidad:").grid(row = 2, column = 0)
    lValorVenta = Label(panelDatosDown, text = "Valor Venta:").grid(row = 0, column = 0)
    lAporte = Label(panelDatosDown, text = "Aporte:").grid(row = 1, column = 0)

    # botón
    bCalcular = Button(vPpal, text = "Calcular valores", bg = "MediumPurple1", command = Calculo)

    # entradas
    eUbicacion = Entry(panelDatosUp, width = 20, bg = "powder blue") # Powder / Jinx 😈🔫
    eTipoVenta = Entry(panelDatosUp, width = 20, bg = "VioletRed1") # Violet 👊💣
    eCantidad = Entry(panelDatosUp, width = 20, bg = "PaleGreen1")
    eValorVenta = Entry(panelDatosDown, width = 20, bg = "papaya whip")
    eAporte = Entry(panelDatosDown, width = 20, bg = "light goldenrod")

    # ubicar
    eUbicacion.grid(row = 0, column = 1)
    eTipoVenta.grid(row = 1, column = 1)
    eCantidad.grid(row = 2, column = 1)
    eValorVenta.grid(row = 0, column = 1)
    eAporte.grid(row = 1, column = 1)

    # fijar
    panelDatosUp.pack()
    bCalcular.pack()
    panelDatosDown.pack()

    vPpal.mainloop()


ventaBoletas()

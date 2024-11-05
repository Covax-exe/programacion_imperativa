"NOTAS ESTUDIANTES"

"""
Problema: Se requiere un programa para almacenar las calificaciones de los
estudiantes del salón, donde cada fila represente un estudiante y cada columna
una de las notas de la asignatura. En la asignatura se realizan 2 parciales y un taller.
Desarrolle un programa en Python con una GUI. Que permita:
✓ Ingresar estudiante: cuando se oprima esta opción se debe almacenar el
nombre de un estudiante en un arreglo unidimensional y almacenar las notas
del estudiante en la fila correspondiente de la matriz de notas.
✓ Listar estudiantes: cuando se oprima esta opción se debe mostrar el listado
de los estudiantes ingresados
✓ Calificaciones estudiantes: se debe mostrar un listado con toda la información
de los estudiantes y su nota definitiva (todas las notas tienen el mismo peso)
✓ Buscar estudiante: debe leer el nombre del estudiante y buscar en los
ingresados si está dicho estudiante, si está debe mostrar todas sus notas
incluida la definitiva
"""

from tkinter import *
import numpy

nombresEst = [""]*20
notas = numpy.array([[0.0]*4]*20)
contador = 0


def ingresarE():
    global contador
    if contador < 20:
        if len(eNombre.get().strip()) != 0 and len(ePar1.get().strip()) != 0 and len(ePar2.get().strip()) != 0 and len(eTall.get().strip()) != 0:
            nombresEst[contador] = eNombre.get().strip()
            notas[contador][0] = float(ePar1.get().strip())
            notas[contador][1] = float(ePar2.get().strip())
            notas[contador][2] = float(eTall.get().strip())
            notas[contador][3] = (notas[contador][0] + notas[contador][1] + notas[contador][2]) / 3
            contador = contador + 1
            areaT.delete("1.0", END)  # borrar en campos de texto
            areaT.insert(INSERT, "Se ingresó el estudiante " + str(contador) + " con éxito!")
        else:
            areaT.delete("1.0", END)
            areaT.insert(INSERT, "No se completaron los datos :(")
    else:
        areaT.delete("1.0", END)
        areaT.insert(INSERT, "No se pueden ingresar más estudiantes")

def mostrar():
    acum = ""
    for i in range(0, len(nombresEst)):
        acum += "\n" + nombresEst[i] + "\t"
        for j in range(0, len(notas[0])):
            acum += str(notas[i][j]) + "\t"
    areaT.delete("1.0", END)  
    areaT.insert(INSERT, acum)
        






ppal = Tk()
ppal.geometry("700x500")

#------------------------------ panel de datos ----------------------------------
panelIngreso = Frame(ppal, bd = 12, relief = "groove" )  #bd = borde // relief = estilo de borde
lNombre = Label(panelIngreso , text = "Nombre: ").grid(row = 0, column = 0)
lPar1 = Label(panelIngreso , text = "Parcial 1: ").grid(row = 0, column = 2)
lPar2 = Label(panelIngreso , text = "Parcial 2: ").grid(row = 1, column = 0)
lTall = Label(panelIngreso , text = "Taller: ").grid(row = 1, column = 2)

eNombre = Entry(panelIngreso, width = 25)
ePar1 = Entry(panelIngreso, width = 25)
ePar2 = Entry(panelIngreso, width = 25)
eTall = Entry(panelIngreso, width = 25)

eNombre.grid(row = 0, column = 1) #ubicarlos :)
ePar1.grid(row = 0, column = 3)
ePar2.grid(row = 1, column = 1)
eTall.grid(row = 1, column = 3)

#--------------------------------- panel de botones------------------------
pBotones = Frame(ppal)
pIngresar = Button(pBotones, command = ingresarE ,text = "Ingresar estudiante", bg = "plum2").grid(row = 0, column = 0 )
pListar = Button(pBotones, command = mostrar ,text = "Listar estudiante", bg = "pink").grid(row = 0, column = 1)
pCalcular = Button(pBotones, text = "Mostrar calificaciones", bg = "lightblue").grid(row = 0, column = 2)
pBuscar = Button(pBotones, text = "Buscar notas de estudiante", bg = "lightgreen").grid(row = 0, column = 3)

#-------------------------------- panel del area de texto --------------------------
pSalida = Frame(ppal)
bd = Scrollbar(pSalida, orient = 'vertical')
bd.pack(side = RIGHT, fill = 'y')

areaT = Text(pSalida, width = 200, height = 200, selectbackground = "DarkOrchid1", yscrollcommand = bd.set)

areaT.pack()

# fijar paneles a la ventana principal
panelIngreso.pack()
pBotones.pack()
pSalida.pack()

ppal.mainloop()

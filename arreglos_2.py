"""Segundo Punto"""

numeros = [0] * 10  # variable global


def ingresarDatos():
    print("\n--------Ingreso de datos en el arreglo--------\n")
    for i in range(0, len(numeros)):
        numeros[i] = int(input("Digite el número en la posición[" + str(i) + "]: "))


# llenar con datos aleatorios
def ingresarDatosAleatorios():
    import random

    for i in range(0, len(numeros)):
        numeros[i] = random.randint(0, 20)
    print("Arreglo lleno con éxito")


# contar la cantidad de veces que aparece el n-número en el arreglo
def cantidadNumero():
    cont = 0
    nBus = int(input("Digite el número que quiere buscar en el arreglo: "))
    for k in range(0, len(numeros)):
        if numeros[k] == nBus:
            cont = cont + 1
    print("La cantidad de", nBus, "que tiene el arreglo es:", cont)


def imprimir():
    for i in range(0, len(numeros)):
        print(numeros[i])


def listaPares():
    acumulador = "Los pares del arreglo son:\n"
    for i in range(0, len(numeros)):
        if numeros[i] % 2 == 0:
            acumulador = acumulador + str(numeros[i]) + "\n"
    print(acumulador)


def listaPosImpares():
    acumulador = "Los números en las posiciones impares del arreglo son:\n"
    for i in range(0, len(numeros)):
        if i % 2 != 0:
            acumulador = acumulador + str(numeros[i]) + "\n"
    print(acumulador)


def menu():
    opc = 0
    while opc != 8:
        print(
            "****** MENÚ DE OPCIONES ****** \n1-Ingresar Datos\n2- Imprimir Datos\n3- Cantidad de número específico\n4- Mostrar los pares\n5- Números en la posiciones impares\n6- Llenar arreglo con aleatorios\n8- Salir"
        )
        opc = int(input("Digite la opción: "))
        if opc == 1:
            ingresarDatos()
        elif opc == 2:
            imprimir()
        elif opc == 3:
            cantidadNumero()
        elif opc == 4:
            listaPares()
        elif opc == 5:
            listaPosImpares()
        elif opc == 6:
            ingresarDatosAleatorios()
        else:
            if opc != 8:
                print("Opción no válida para el menú")


menu()

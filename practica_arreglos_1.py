"""Problema 1: Arreglos Unidimensionales
Descripción: Escribe un programa en Python que lea una lista de números enteros introducidos por el usuario y
luego realice las siguientes operaciones:
Calcule y muestre la suma de todos los números.
Calcule y muestre el promedio de los números.
Encuentre y muestre el número más grande y el más pequeño de la lista."""

def puntoUno():
    tamaño = int(input("Digite el tamaño del arreglo: "))
    arreglo = [0]*tamaño
    suma = 0

    for i in range(len(arreglo)):
        arreglo[i] = int(input(f"Ingrese el número en la posición #{i+1}:"))
        suma += arreglo[i]
    promedio = suma / tamaño
    maximo = max(arreglo)
    minimo = min(arreglo)

    print(f"El arreglo es: \n{arreglo}")
    print(f"La suma de todos los números es: {suma}")
    print(f"El promedio de los números es: {promedio}")
    print(f"El número más grande es: {maximo} ")
    print(f"El número más pequeño es: {minimo}")

#puntoUno()

"""Problema 2: Arreglos Bidimensionales
Descripción: Escribe un programa en Python que cree una matriz de 3x3, lea los valores introducidos por el usuario para llenar la matriz y
luego realice las siguientes operaciones:
Calcule y muestre la suma de todos los elementos de la matriz.
Calcule y muestre el promedio de los elementos de la matriz.
Encuentre y muestre el número más grande y el más pequeño de la matriz."""

import numpy

def puntoDos():

    matriz = numpy.array([[0] * 3] * 3)
    suma = 0

    for i in range(len(matriz)):
        for u in range(len(matriz[0])):
            matriz[i][u] = int(input(f"Ingrese un número en la posición {[i]}{[u]}: "))
            suma += matriz[i][u]
    promedio = suma / len(matriz)
    maximo = matriz.max()
    minimo = matriz.min()

    print(f"El arreglo es: \n{matriz}")
    print(f"La suma de todos los números es: {suma}")
    print(f"El promedio de los números es: {promedio}")
    print(f"El número más grande es: {maximo}")
    print(f"El número más pequeño es: {minimo}")

puntoDos()
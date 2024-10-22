# importar la librería
import numpy
import random

# matrizNumeros = numpy.zeros((3, 4)) #llena las casillas con 0.

matriz2 = numpy.array([[1] * 4] * 4)  # llena las casillas con 1 entero

for col in range(0, len(matriz2[0]), 1):
    for fila in range(0, len(matriz2), 1):
        matriz2[fila][col] = random.randint(12, 65)
        # matriz2[fila][col] = int(input("Digite el valor en pos" + col + " " + fila))

# print(matrizNumeros)

"""Valores Pares"""
acum = ""
print("Los valores pares la matriz son: ")
for f in range(0, len(matriz2), 1):
    for c in range(0, len(matriz2[0]), 1):
        if matriz2[f][c] % 2 == 0:
            acum = acum + str(matriz2[f][c]) + "\n"
print(acum)

print("Los valores de la primera fila son: ")
for x in range(0, len(matriz2[0]), 1):
    print(matriz2[0][x])

print("Los datos en la diagonal son: ")
for i in range(0, len(matriz2), 1):
    for j in range(0, len(matriz2[0]), 1):
        if i == j:
            print(matriz2)

print("---------------- Segunda Matriz ---------------")
print(matriz2)

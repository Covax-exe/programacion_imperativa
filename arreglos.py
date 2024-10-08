"""
nombreArreglo = [] * n

ingresar datos en el arreglo
nombreArreglo [posición] = valor

ciclo más adecuado para recorrer arreglos es el for :)
"""

arreglosNumeros = [None] * 10
arrN = [0] * 5

arreglosNumeros[2] = "leo"
arreglosNumeros[9] = "Santiago"
# arreglosNumeros[9] = "Otro"  //Reemplaza el valor
arreglosNumeros[9] = arreglosNumeros[9] + "Otro"  # Concatena valores
# arreglosNumeros [10] = "algo"  //NO SE PUEDE, DESBORDE DE CASILLAS

for indice in range(0, len(arreglosNumeros), 1):
    print(arreglosNumeros[indice])


print("-" * 30)
print(arreglosNumeros)
print("*" * 20, "\nArreglo 2\n", arrN)

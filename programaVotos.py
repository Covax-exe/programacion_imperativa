import numpy

cand = int(input("Ingrese la cantidad de candidatos: "))
sed = int(input("Ingrese la cantidad de sedes: "))

# crear arreglos y la matriz
candidatos = [""] * cand
sedes = [""] * sed
votos = numpy.array([[0] * cand] * sed)

# Para no volver a escribirlo :)
votos = [[500, 400, 300], [250, 150, 250], [200, 250, 100], [120, 200, 210]]
sedes = ["Cali", "Palmira", "Buga", "Tulua"]
candidatos = ["Rios", "Sanchez", "Ramos"]

"""
for f in range(0, cand, 1):
    candidatos[f] = input("Digite el nombre del candidato " + str(f + 1) + ": ")

for f in range(0, sed, 1):
    sedes[f] = input("Digite el nombre de la sede " + str(f + 1) + ": ")

for f in range(0, sed, 1):
    for c in range(0, cand, 1):
        votos[f][c] = int(
            input(
                "Ingrese el voto del candidato "
                + candidatos[c]
                + " de la sede "
                + sedes[f]
                + ": "
            )
        )
"""

acum = "\t\t"  # da el espacio de los nombres :P
for k in range(0, cand, 1):
    acum = acum + candidatos[k] + "\t"
acum = acum + "\n"

for i in range(0, sed, 1):
    acum = acum + sedes[i] + "\t"
    for j in range(0, cand, 1):
        acum = acum + "\t" + str(votos[i][j])
    acum = acum + "\n"
print(acum)

votosTotales = [0] * cand

for c in range(0, cand, 1):
    suma = 0
    for f in range(0, sed, 1):
        suma = suma + votos[f][c]
    votosTotales[c] = suma
    print("La cantidad de votos del candidato", candidatos[c], "es:", votosTotales[c])


# máximo de votos totales
maximo = max(votosTotales)
print("Máximo", maximo)
# pos máximo en arreglo de votos totales
pos = votosTotales.index(maximo)
print("Posición", pos)
# imprimir candidatos en la posición que saqué
print("El candidato ganador es: ", candidatos[pos])

mayor = -1
pos1 = -1
for i in range(0, len(votosTotales), 1):
    if votosTotales[i] > mayor:
        mayor = votosTotales[i]
        pos = i
print(candidatos[pos1])

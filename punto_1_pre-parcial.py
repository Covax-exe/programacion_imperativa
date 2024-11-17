import numpy
datos = numpy.zeros((4,4))
datos[0][0]=30
datos[0][1]=12
datos[0][2]=14
datos[0][3]=92
datos[1][0]=29
datos[1][1]=65
datos[1][2]=22
datos[1][3]=21
datos[2][0]=78
datos[2][1]=35
datos[2][2]=10
datos[2][3]=22
datos[3][0]=71
datos[3][1]=53
datos[3][2]=102
datos[3][3]=38

print("--------------- MATRIZ -----------------")
print(datos)

#--------------- punto 1 -----------------
"""Realice la prueba de escritorio completa y
coloque el valor que se imprime sobre la línea: _162_"""
print("--------------- punto 1 -----------------")
s=0
for i in range(0,len(datos[0]),1):
    for j in range(0,len(datos),1):
        if (j>i and datos[i][j]%2==0):
            s = s + datos[i][j]
        #print("columna",i,"\tfila",j)
        #print(s)
print(s)


#--------------- punto 2 -----------------
"""Al ejecutar las siguientes instrucciones se
muestran los valores (coloque cada valor
separado por coma): _78, 71, 65, 35, 53, 14, 22, 10 , 102_"""
print("\n--------------- punto 2 -----------------")
for i in range(0,3,1):
    for j in range(0,4,1):
        if (i+j>=2):
            print(datos[j][i])

#--------------- punto 3 -----------------
"""Al ejecutar las siguientes instrucciones se muestra el valor: _-30_"""
print("\n--------------- punto 3 -----------------")
s=10
for i in range(0,4,1):
    for j in range(0,(i+1),1):
        if (i<=j):
            s = s + datos[i][j]
        else:
            s = s - datos[j][i]
print(s)

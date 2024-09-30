#ENTRADAS
frase1 = input("Digite la primera frase: ")
frase2 = input("Digite la segunda frase: ")
consonante = input("Digite una consonante: ")


#OPERACIONES

#Transformar texto
minusFrase1 = frase1.lower()
minusFrase2 = frase2.lower()
minusConsonante = consonante.lower()


#Longitud de frases
longitud1 = len(frase1)
longitud2 = len(frase2)


#Contar las i
contarI1 = minusFrase1.count("i")
contarI2 = minusFrase2.count("i")


#Lista de consonantes
consonanteList = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s" ,"t" ,"v" ,"w" ,"x" ,"y" , "z"]

#Contar la consonante
contarConsonante1 = minusFrase1.count(minusConsonante)
contarConsonante2 = minusFrase2.count(minusConsonante)


#Vocales 1
contarA1 = minusFrase1.count("a")
contarE1 = minusFrase1.count("e")
contarO1 = minusFrase1.count("o")
contarU1 = minusFrase1.count("u")
contarVocal1 = contarA1 + contarE1 + contarI1 + contarO1 + contarU1

#Vocales 2
contarA2 = minusFrase2.count("a")
contarE2 = minusFrase2.count("e")
contarO2 = minusFrase2.count("o")
contarU2 = minusFrase2.count("u")
contarVocal2 = contarA2 + contarE2 + contarI2 + contarO2 + contarU2

#Porcentaje vocal
porcentajeVocal1 = contarVocal1 / longitud1 * 100
porcentajeVocal2 = contarVocal2 / longitud2 * 100

#SEPARACIÓN
print("---------------------------------")

#LONGITUD
if longitud1 < longitud2:
    print("La longitud de la frase 2 es:",longitud2,"es mayor que la longitud de la frase 1 que es:",longitud1)
elif longitud1 > longitud2:
    print("La longitud de la frase 1 es:",longitud1,"es mayor que la longitud de la frase 2 que es:",longitud2)
else:
    print("La longitud de la frase 1 es:",longitud1,"es igual que la longitud de la frase 2 que es:",longitud2)

#CANTIDAD DE i
if contarI1 < contarI2:
    print("Cantidad de i de la frase 1:",contarI1)
    print("Cantidad de i de la frase 2:",contarI2)
    print("La frase 1 tiene la menor cantidad de i")
elif contarI1 > contarI2:
    print("Cantidad de i de la frase 1:",contarI1)
    print("Cantidad de i de la frase 2:",contarI2)
    print("La frase 2 tiene la menor cantidad de i")
else:
    print("Cantidad de i de la frase 1:",contarI1)
    print("Cantidad de i de la frase 2:",contarI2)
    print("La frase 1 y 2 tienen la misma cantidad de i")

#CANTIDAD DE CONSONANTE
if minusConsonante in consonanteList:
    print("Cantidad de veces que aparece:",consonante,"en la frase 1 es:",contarConsonante1)
    print("Cantidad de veces que aparece:",consonante,"en la frase 2 es:",contarConsonante2)
else:
    print("DEBE INGRESAR UNA SOLA CONSONANTE!")

#CANTIDAD DE VOCALES
print("La cantidad de vocales en la frase 1 es:",contarVocal1)
print("Porcentaje de vocales en la frase 1 es:",porcentajeVocal1,"%")

print("La cantidad de vocales en la frase 2 es:",contarVocal2)
print("Porcentaje de vocales en la frase 2 es:",porcentajeVocal2,"%")
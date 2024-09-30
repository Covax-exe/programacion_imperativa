# Definir función
def contar_impares(a, b):
    if a > b:
        return 0
    elif a % 2 != 0:
        return 1 + contar_impares(a + 1, b)
    else:
        return contar_impares(a + 1, b)


# ENTRADAS
a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))

# SALIDA
resultado = contar_impares(a, b)
print("La cantidad de impares entre", a, "y", b, "es:", resultado)

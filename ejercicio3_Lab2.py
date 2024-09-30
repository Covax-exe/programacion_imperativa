"""
Integrantes: Santiago Cerón, Lina Cosme, Stiven Diosa.
Profesor: Leoviviana Moreno.
Número de grupo: 01.
Número de laboratorio: 02.
"""

"""
Una Constructora ofrece casas de interés social, bajo las
siguientes condiciones: Si los ingresos del comprador son
menores de $3.000.000, la cuota inicial será del 20% del
costo de la casa y el resto de la deuda se le aplica un interés
del 15% y se distribuye en pagos mensuales, a pagar en diez
años.

Si los ingresos del comprador son desde $3.000.000, la cuota inicial será del 30% del costo de la
casa y el resto de la deuda se le aplica un interés del 18% y se distribuirá en pagos mensuales a
pagar en 7 años.

La empresa quiere que los estudiantes de primer semestre de programación imperativa realicen un
programa en Python, que lea la información de n interesados en comprar casa. Por cada interesado
se debe pedir el nombre, el ingreso mensual, y el valor de la casa que desea comprar. y a partir de
ella calcule y muestre el valor que debe pagar de la cuota inicial, el valor que van a pagar por
intereses, el porcentaje del interés, el saldo de la deuda y el valor de la cuota que debe pagar y la
cantidad de cuotas a pagar.

Cuando se termine el ingreso de los n interesados (donde n es un número ingresado por el usuario)
se debe imprimir la cantidad de personas con ingresos menores a 3.000.000 que consultaron, y el
nombre y el sueldo de las personas que consultaron con ingresos desde 3.000.000
"""

"""
ENTRADAS
cantidad interesados
nombre
ingresos
valor casa a comprar

SALIDAS
valor a pagar cuota inicial
valor a pagar por intereses
porcentaje del interés
saldo de la deuda
valor de cuota a pagar
cantidad de cuotas a pagar

*AL FINALIZAR
cantidad de personas con ingresos menores a 3.000.000
nombre y sueldo de personas con ingresos desde 3.000.000
"""


def constructora():
    n = int(input("Ingrese la cantidad de interesados en comprar casa: "))
    # Contador
    personas_ingreso_menor_3000000 = 0
    personas_ingreso_desde_3000000 = ""

    for i in range(0, n, 1):
        print("Interesado #", i + 1)
        nombre = input("Ingrese el nombre: ")
        ingreso = float(input("Ingrese los ingresos: "))
        valor_casa = float(input("Ingrese el valor de la casa a comprar: "))

        # Ingresos menores a 3.000.000
        if ingreso < 3000000:
            cuota_inicial = valor_casa * 0.2
            saldo_deuda = valor_casa - cuota_inicial
            porcentaje_intereses = 15
            cantidad_cuotas = 12 * 10
            intereses = saldo_deuda * (porcentaje_intereses / 100)
            cuota_mensual = (saldo_deuda + intereses) / cantidad_cuotas

            print(
                "Cuota inicial:",
                cuota_inicial,
                "\nPorcentaje de interés:",
                porcentaje_intereses,
                "%",
                "\nValor de los intereses:",
                intereses,
                "\nSaldo de la deuda:",
                saldo_deuda,
                "\nCuota mensual:",
                cuota_mensual,
                "\nCantidad de cuotas:",
                cantidad_cuotas,
            )

            personas_ingreso_menor_3000000 += 1

        # Ingresos desde 3.000.000
        else:
            cuota_inicial = valor_casa * 0.3
            saldo_deuda = valor_casa - cuota_inicial
            porcentaje_intereses = 18
            cantidad_cuotas = 12 * 7
            intereses = saldo_deuda * (porcentaje_intereses / 100)
            cuota_mensual = (saldo_deuda + intereses) / cantidad_cuotas

            print(
                "Cuota inicial:",
                cuota_inicial,
                "\nPorcentaje de interés:",
                porcentaje_intereses,
                "%",
                "\nValor de los intereses:",
                intereses,
                "\nSaldo de la deuda:",
                saldo_deuda,
                "\nCuota mensual:",
                cuota_mensual,
                "\nCantidad de cuotas:",
                cantidad_cuotas,
            )

            personas_ingreso_desde_3000000 += (
                "Nombre:" + nombre + "\nIngresos mensuales:" + str(ingreso) + "\n"
            )

    # Cantidad personas con ingresos menores a 3.000.000
    print(
        "Cantidad de personas con ingresos menores a $3.000.000:",
        personas_ingreso_menor_3000000,
    )

    # Datos personas con ingresos desde 3.000.000
    if personas_ingreso_desde_3000000:
        print(
            "Personas con ingresos desde $3.000.000:\n", personas_ingreso_desde_3000000
        )


constructora()

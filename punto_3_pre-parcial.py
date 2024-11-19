"""
Se requiere un programa en Python que realice operaciones sobre un arreglo unidimensional estático de
acuerdo a la entrada del usuario, el programa se debe ejecutar constantemente pidiéndole un número entero no negativo
al usuario y debe terminar su ejecución cuando el usuario digite un número negativo. El programa debe hacer lo siguiente:
• Si el número ingresado por el usuario es solamente múltiplo de 3: debe restarle 3 unidades a la primera mitad
de los números del arreglo.
• Si el número ingresado por el usuario es solamente múltiplo de 5: debe sumarle 1 unidad a todos los números
del arreglo.
• Si el número ingresado por el usuario es múltiplo de ambos 3 y 5: debe calcular y mostrar la suma de los números
pares del arreglo.
• Si el número ingresado por el usuario no es múltiplo de ninguno de los dos números: debe sumarle 4 unidades a
la segunda mitad de los números del arreglo.
NO DEBE HACER EL CÓDIGO PARA PEDIR LOS DATOS DEL ARREGLO, EL PROGRAMA DEBE FUNCIONAR PARA
UN ARREGLO DE CUALQUIER TAMAÑO Y PUEDE TRABAJAR PARA SUS PRUEBAS CON EL SIGUIENTE
ARREGLO:
arreglo =[5,7,8,9,15,2,3,4,7,7,12,34,56,65,73,23,14,56,86,33,21,213,45,12,3,5,198]
"""

def punto3():
    arreglo =[5,7,8,9,15,2,3,4,7,7,12,34,56,65,73,23,14,56,86,33,21,213,45,12,3,5,198]

    print("*"*7, "PROGAMA NÚMEROS", "*"*7)
    print(arreglo)
    print("*"*100)

    numero = int(input("-----Digite un entero positivo  [ó digite un número negativo para finalizar]: "))

    while numero >= 0:

        suma_pares = 0
        mitad = len(arreglo)//2 # mitad del arreglo.

        if numero % 3 == 0 and numero % 5 == 0:
            for i in range(len(arreglo)):
                if arreglo[i] % 2 == 0:
                    suma_pares += arreglo[i]
            print(f"El dato registrado es multiplo de 3 y 5. \nLa suma de los datos pares del arreglo son: \n{suma_pares}")

        elif numero % 3 == 0:
            for i in range(mitad):
                arreglo[i] -= 3
            print(f"El número ingresado era multiplo de 3, se le restaron 3 unidades a la primera mitad de los datos del arreglo. \nLos datos del arreglo son: \n{arreglo}")

        elif numero % 5 == 0:
            for i in range(len(arreglo)):
                arreglo[i] += 1
            print(f"El número ingresado era multiplo de 5, se le sumó 1 a cada dato del arreglo. \nLos datos del arreglo son: \n{arreglo}")

        else:
            for i in range(mitad, len(arreglo)):
                arreglo[i] += 4
            print(f"El número ingresado NO es multiplo ni de 3 ni de 5, se le sumó 4 a cada dato de la segunda mitad del arreglo. \nLos datos del arreglo son: \n{arreglo}")

        numero = int(input("-----Digite un entero positivo  [ó digite un número negativo para finalizar]: "))

print("Fin del programa.")


punto3()
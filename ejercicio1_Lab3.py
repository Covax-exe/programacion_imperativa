"""
La Universidad del Valle requiere un programa que le permita
conocer cómo califican los estudiantes la comida de la cafetería. Para ello definió una escala de 1 a 10 (1 denota horrible y
10 denota excelente).
El programa debe ser capaz capturar la calificación de cualquier número de estudiantes (no
se sabe cuántos estudiantes se encuestarán, así que cuando el encuestador ingrese el
número cero en la calificación se sabrá que la encuesta habrá concluido). Si la nota
ingresada es mayor a 10 o un número negativo se le debe mostrar un mensaje de nota
inválida y se le debe volver a pedir la calificación.
El programa deberá mostrar cuando se termine el ingreso de calificaciones la cantidad de
estudiantes que fueron encuestados así como el resumen de la encuesta con histograma.
"""


def calificacionesRestaurante():
    cant_estudiantes = int(input("Ingrese la cantidad de estudiantes a encuestar: "))

    calificaciones = [0] * cant_estudiantes
    frecuencia = [0] * 10  # Arreglo estático de 10 elementos para las frecuencias 

    for i in range(0, cant_estudiantes, 1):
        nota = int(input(f"Estudiante {i + 1}. Digite la calificación de 1 a 10 (0 para salir): "))
        if nota == 0:
            break
        while nota < 1 or nota > 10:
            print("Nota inválida. Ingrese una calificación entre 1 y 10.")
            nota = int(input(f"Estudiante {i + 1}. Digite la calificación de 1 a 10 (0 para salir): "))

        calificaciones[i] = nota
        frecuencia[nota - 1] += 1  # Incrementar la frecuencia de la calificación // Es -1 porque empieza en 0 

    # FINAL
    print(f"\nCantidad de estudiantes encuestados: {cant_estudiantes}")
    print("***** FRECUENCIA DE LAS CALIFICACIONES *****")
    print("Calificación    Num estud    Histograma")

    for i in range(10):
        # Mostrar la calificación, el número de estudiantes y el histograma 
        print(f"{i + 1:<15} {int(frecuencia[i]):<12} {'*' * int(frecuencia[i])}")  #:<15 y :<12 para acomodarlos en las columnas 


calificacionesRestaurante()

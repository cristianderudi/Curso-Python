""" Ejercicio 029
Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. 
Si el valor de la nota no esta entre 0 y 10, debe informar un error.
Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Se debe recuperar cuando al menos una de las dos notas es menor a 4. """


# Pedir al usuario que ingrese las notas de los dos parciales
nota1 = float(input("Ingrese la nota del primer parcial: "))
nota2 = float(input("Ingrese la nota del segundo parcial: "))

# Verificar si las notas están en el rango válido
if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print("Error: Las notas deben estar entre 0 y 10")
else:
    # Determinar si el alumno promocionó, aprobó o debe recuperar
    if nota1 >= 7 and nota2 >= 7:
        print("El alumno promocionó")
    elif nota1 >= 4 and nota2 >= 4:
        print("El alumno aprobó")
    else:
        print("El alumno debe recuperar")
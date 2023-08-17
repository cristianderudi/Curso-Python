""" Ejercicio 029
Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. 
Si el valor de la nota no esta entre 0 y 10, debe informar un error.
Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Se debe recuperar cuando al menos una de las dos notas es menor a 4. """


NOTA_MENOR = 0
NOTA_MAYOR = 10
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

while True:
    if nota1 < NOTA_MENOR or nota1 > NOTA_MAYOR or nota2 < NOTA_MENOR or nota2 > NOTA_MAYOR:
        print("Nota invalida, vuelva a ingresarlas")
        nota1= float(input("Nota 1: "))
        nota2= float(input("Nota 2: "))
    else:
        if nota1 >= 7 and nota2 >= 7:
            print("Promociona!")

        elif nota1 >= 4 and nota2 >=4:
            print("Aprobo!")
        else:
            print("Recupera")
        break
    
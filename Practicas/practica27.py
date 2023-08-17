""" Ejercicio 027
Escribir un programa que permita ingresar una edad (entre 1 y 120 años), 
un género ('F'para mujeres, 'M' para hombres) y un nombre. 
En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), informar tal situación indicando el nombre de la persona. 
Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, 
si la persona está en edad de jubilarse. """


EDAD_MINIMA = 1
EDAD_MAXIMA = 120
JUBILACION_MUJERES = 60
JUBILACION_HOMBRES = 65

GENERO_FEMENINO = "F"
GENERO_MASCULINO = "M"

continuar = "S"
while continuar == "S":
    nombre = input("Nombre: ").title()
    genero = input("Genero (F/M): ").upper()

    while genero != GENERO_MASCULINO and genero != GENERO_FEMENINO:
        print("Genero incorrecto, vuelva a ingresarlo")
        genero = input("Genero (F/M): ").upper()

    edad = int(input("Edad: "))
    while edad < EDAD_MINIMA or edad > EDAD_MAXIMA:
        print("Edad incorrecta, vuelva a ingresarla")
        edad = int(input("Edad: "))

    if genero == GENERO_MASCULINO:
        se_jubila = edad >= JUBILACION_HOMBRES
    else:
        se_jubila = edad >= JUBILACION_MUJERES
    if se_jubila:
        print(f"{nombre} Genero: {genero} Se jubila")
    else:
        print(f"{nombre} Genero: ({genero}) No se jubila")
    
    continuar = input("Desea ingresar otra persona? (S/N): ").upper()
print("Hasta luego!")


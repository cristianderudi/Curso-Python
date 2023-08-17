"""
Ejercicio 006
Escribir un programa que solicite al usuario ingresar tres notas de un alumno. 
El programa debe mostrar por pantalla las notas separadas por comas en un renglón y el promedio de las notas en el siguiente renglon.
Ejemplo de ejecución:

    Ingrese la nota 1: 7
    Ingrese la nota 2: 8
    Ingrese la nota 3: 9
    Notas: 7, 8, 9
    Promedio: 8.0"""



nota1 = int(input("Ingrese la nota 1: "))
nota2 = int(input("Ingrese la nota 2: "))
nota3 = int(input("Ingrese la nota 3: "))

print(f"{nota1}, {nota2}, {nota3}")
print(f"Promedio:",(nota1 + nota2 + nota3)/3)
""" Ejercicio 022
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor. """


num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
num3 = int(input("Ingrese tercerer numero: "))

mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3
print(f"Mayor", mayor)

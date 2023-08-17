""" Ejercicio 021
Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor, menor o igual al segundo. """


num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num1} Es menor que {num2}")
else:
    print(f"Ambos son iguales")

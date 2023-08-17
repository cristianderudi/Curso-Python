"""
Ejercicio 042
Escribir un programa que lea números enteros hasta que se ingrese un 0, 
y muestre el promedio de los números ingresados.
"""

import random

sumador = 0
contador = 0
numero = random.randint(0,3)
while numero != 0:

    sumador += numero
    contador += 1
    numero = random.randint(0,100)

if contador != 0:
    promedio =  sumador/contador
else:
    promedio = None




print(f"Promedio: {promedio}")


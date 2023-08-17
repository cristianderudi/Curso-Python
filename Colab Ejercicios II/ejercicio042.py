""" Ejercicio 042
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el promedio de los números ingresados. """



enteros = []
while True:
    num = int(input("Ingrese un numero: "))
    if num == 0:
        break
    enteros.append(num)
suma = sum(enteros)
cantidad = len(enteros)
promedio = suma / cantidad
print(f"El promedio de los numeros ingresados es: {promedio}")

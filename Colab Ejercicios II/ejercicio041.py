""" Ejercicio 041
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el máximo. """



enteros = []
while True:
    num = int(input("Ingrese un numero: "))
    if num == 0:
        break
    enteros.append(num)
print(f"El Numero maximo ingresado es el: {max(enteros)}")
""" Ejercicio 040
Escribir un programa que permita ingresar dos numeros enteros a y b. 
El programa debe mostrar:
La suma de los numeros pares entre a y b.
El producto de los numeros impares entre a y b. """

suma = 0
producto = 1

a = int(input("Ingrese primer numero entero: "))
b = int(input("Ingrese segundo numero entero: "))

for i in range(a, b+1):
    if i % 2 == 0:
        suma += i
    if i % 2 != 0:
        producto *= i

print(f"La suma de los numeros pares entre a y b es: {suma}")
print(f"El producto de los numeros impares entre a y b es : {producto}")
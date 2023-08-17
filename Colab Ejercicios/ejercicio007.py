"""
Ejercicio 007
Escribir un programa que permita ingresar un número entero. Debe mostrarse el número ingresado:
a. Multiplicado por 10. (utilizar el operador *)
b. Dividido por 10. (utilizar el operador /)
c. Elevado al cuadrado. (utilizar el operador **)
Cada resultado debe mostrarse en una línea distinta.
Ejemplo de ejecución:

Ingrese un número entero: 5
5 * 10 = 50
5 / 10 = 0.5
5 ** 2 = 25
"""

num = int(input("Ingrese un número entero: "))
print(f"{num} * 10 = {num * 10}")
print(f"{num} / 10 = {num / 10}")
print(f"{num} ** 2 = {num ** 2}")
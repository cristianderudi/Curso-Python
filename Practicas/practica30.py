""" Ejercicio 030
Escribir un programa que permita al usuario ingresar dos números enteros. 
La computadora debe indicar si el mayor es divisible por el menor.
(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0) """


num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))

if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

if menor == 0:
    print("No se puede dividir por 0")
elif mayor % menor == 0:
    print(f"{mayor} es divisible por {menor}")

else:
    print(f"{mayor} no es divisible por {menor}")

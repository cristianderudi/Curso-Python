""" Ejercicio 030
Escribir un programa que permita al usuario ingresar dos números enteros. 
La computadora debe indicar si el mayor es divisible por el menor.
(Un número entero A es divisible por un número entero B cuando el resto de la división entre A y B es 0) """

# Tomar dos números como entrada del usuario
num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))

# Determinar cuál número es mayor y cuál es menor
if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

# Verificar si el número mayor es divisible por el número menor
if mayor % menor == 0:
    # Imprimir que el número mayor es divisible por el número menor
    print(f"{mayor} es divisible de {menor}")
    
else:
    # Imprimir que el número mayor no es divisible por el número menor
    print(f"{mayor} no es divisible de {menor}")
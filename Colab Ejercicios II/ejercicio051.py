""" Ejercicio 051
Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.
La computadora debe mostrar el número máximo y el número mínimo. """


numeros_ingresados = []
while True:
    numero = int(input("Ingrese un numero [0 para salir]: "))
    if numero == 0:
        print("Hasta luego")
        break
    numeros_ingresados.append(numero)
print(f"El numero maximo ingresado es: {max(numeros_ingresados)}")
print(f"El numero minimo ingresado es: {min(numeros_ingresados)}")




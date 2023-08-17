"""
Ejercicio 003
Escribir un programa que solicite al usuario su nombre y su edad, después pida 
una cantidad de años y muestre por pantalla un mensaje que indique cuántos años 
tendrá la persona después de sumarle a su edad la cantidad de años ingresada. 
El mensaje debe tener el siguiente formato: 
'Hola, [nombre]. Dentro de [cantidad] años tendrás [edad + cantidad] años'".
Ejemplo: Si el usuario ingresa "Juan" y "20" y luego ingresa "5", el programa debe 
mostrar por pantalla "Hola, Juan. Dentro de 5 años tendrás 25 años".
"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
cantidad = int(input("Ingrese cantidad de años: "))

print(f"Hola, {nombre}. Dentro de {cantidad} años, tendrás {edad + cantidad} años.")
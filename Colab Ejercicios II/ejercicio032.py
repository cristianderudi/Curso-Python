""" Ejercicio 032
Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.
Tiene la siguiente tarifa:
Viaje mínimo $50

Si recorre entre 0 y 10km: $20/km

Si recorre 10km o más: $15/km

Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje. """


VIAJE_MINIMO = 50
ENTRE_0_10_KM = 20
MAS_DE_10_KM = 15

cantidad_km = int(input("Ingrese cantidad de Km: "))

if cantidad_km <= 10:
    precio = cantidad_km * ENTRE_0_10_KM
elif cantidad_km >= 10:
    precio = cantidad_km * MAS_DE_10_KM

if precio < VIAJE_MINIMO:
    precio = VIAJE_MINIMO

print(f"El precio del viaje es de: $ {precio}")

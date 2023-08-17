"""Ejercicio 026
Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon. 
Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse."""


invitados = int(input("Ingrese cantidad de invitados: "))
asientos = int(input("¿Cantidad de asientos?:" ))
faltantes = invitados - asientos

if invitados <= asientos:
    print("Los asientos alcanzan.")
if invitados > asientos:
    print(f"No alcanzan, faltan {faltantes} asientos!.")
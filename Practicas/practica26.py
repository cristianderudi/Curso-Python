""" Ejercicio 026
Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon. 
Debes indicar si alcanzan los asientos. 
Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse. """



invitados = int(input("Cantidad de invitados: "))
asientos = int(input("Cantidad de asientos: "))
total_asientos = invitados - asientos

if invitados <= asientos:
    print("Los asientos alcanzan para todos")
else:
    print(f"Faltan {total_asientos} asientos")
    